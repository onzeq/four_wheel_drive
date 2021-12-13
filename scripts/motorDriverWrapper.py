#!/usr/bin/env python3
import rospy
from std_srvs.srv import Trigger
from four_wheel_drive.msg import Drives_command
from drives import Drives
import constants as constants




class MotorDriver:
    def __init__(self):
        
        sub = rospy.Subscriber('drives_commander', Drives_command, self.callback_command)
        self.__drives = Drives()
        rospy.Service("stop_motor", Trigger, self.callback_stop)


    def callback_command(self, msg:Drives_command):
        rospy.loginfo("Command received")
        rospy.logdebug(msg)
        if(msg.command.data == constants.FORWARD):
            self.__drives.forward(msg.speed_val.data)
            rospy.loginfo("Forward command executed")
        elif(msg.command.data == constants.BACKWARD):
            self.__drives.backward(msg.speed_val.data)
            rospy.loginfo("Backward command executed")
        elif(msg.command.data == constants.LEFT_ANGULAR):
            self.__drives.left_angular(msg.speed_val.data)
            rospy.loginfo("Left angular command executed")
        elif(msg.command.data == constants.RIGHT_ANGULAR):
            self.__drives.right_angular(msg.speed_val.data)
            rospy.loginfo("Right angular command executed")
        elif(msg.command.data == constants.TURN_LEFT):
            self.__drives.turn_left(msg.speed_val.data)
            rospy.loginfo("Turn left command executed")
        elif(msg.command.data == constants.TURN_RIGHT):
            self.__drives.turn_right(msg.speed_val.data)
            rospy.loginfo("Turn right command executed")
        else:
            rospy.logwarn("Command not recogniced, stop motors")
            self.__drives.stop()
        
    def callback_stop(self, req):
        self.__drives.stop()
        return {"success": True, "message": "Motors have been stopped"}
    def stop(self):
        self.__drives.stop()
    


def main():
    rospy.init_node("motor_driver")
    motor_driver = MotorDriver()

    rospy.on_shutdown(motor_driver.stop) 
    rospy.loginfo("Motor driver is now started, ready to get commands.")
    rospy.spin()

if __name__ == '__main__':
    main()