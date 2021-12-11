#!/usr/bin/env python3
import rospy
from driver_scripts.drives import Drives
from driver_scripts.drives import Commands

from four_wheel_drive.msg import Drives_command
from std_srvs.srv import Trigger

class MotorDriver:
    def __init__(self):
        
        ub = rospy.Subscriber('drives_commander', Drives_command, self.callback_command)
        self.drives = Drives()
        rospy.Service("stop_motor", Trigger, self.callback_stop)


    def callback_command(self, msg:Drives_command):
        rospy.loginfo("Command received")
<<<<<<< HEAD
        if(msg.command.data == Commands.FORWARD):
=======
        rospy.loginfo(msg)
        if(msg.command.data == drives.FORWARD):
>>>>>>> beb6683458314383b8f1228649455ab90e948824
            self.drives.forward(msg.speed_val.data)
            rospy.loginfo("Forward command executed")
        elif(msg.command.data == Commands.BACKWARD):
            self.drives.backward(msg.speed_val.data)
            rospy.loginfo("Backward command executed")
        elif(msg.command.data == Commands.LEFT_ANGULAR):
            self.drives.left_angular(msg.speed_val.data)
            rospy.loginfo("Left angular command executed")
        elif(msg.command.data == Commands.RIGHT_ANGULAR):
            self.drives.right_angular(msg.speed_val.data)
            rospy.loginfo("Right angular command executed")
        elif(msg.command.data == Commands.TURN_LEFT):
            self.drives.turn_left(msg.speed_val.data)
            rospy.loginfo("Turn left command executed")
        elif(msg.command.data == Commands.TURN_RIGHT):
            self.drives.turn_right(msg.speed_val.data)
            rospy.loginfo("Turn right command executed")
        else:
            rospy.logwarn("Command not recogniced, stop motors")
            self.drives.stop()
        
    def callback_stop(self, req):
        self.drives.stop()
        return {"success": True, "message": "Motors have been stopped"}
    def stop(self):
        self.drives.stop()
    


def main():
    rospy.init_node("motor_driver")
    motor_driver = MotorDriver()

    rospy.on_shutdown(motor_driver.stop) 
    rospy.loginfo("Motor driver is now started, ready to get commands.")
    rospy.spin()

if __name__ == '__main__':
    main()