#!/usr/bin/env python3
import rospy
from four_wheel_drive.msg import Drives_command

from rospy.exceptions import ROSInterruptException
import constants

def command_publisher():
    pub = rospy.Publisher("drives_commander", Drives_command, queue_size=10)
    rospy.init_node("dummy_commander", anonymous=True)
    rate = rospy.Rate(1)


    msg = Drives_command()
    
    msg.command.data = constants.FORWARD
    msg.speed_val.data = 0.5

    flag = 0
    while not rospy.is_shutdown():
        rospy.loginfo("In Loop")
        if flag == 0:
            pub.publish(msg)
            flag =1
        rate.sleep()
        msg.speed_val.data = 0.2



def main():
    try:
        command_publisher()
    except rospy.ROSInterruptException:
        pass


if __name__ == '__main__':
    main()