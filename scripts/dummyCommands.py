#!/usr/bin/env python3
import rospy
from four_wheel_drive.msg import Drives_command

from rospy.exceptions import ROSInterruptException
import constants

def command_publisher():
    pub = rospy.Publisher("drives_commander", Drives_command, queue_size=10)
    rospy.init_node("dummy_commander")
    rate = rospy.Rate(1)


    msg = Drives_command()
    
    msg.command.data = constants.FORWARD
    msg.speed_val.data = 0.3

    flag = 0
    while not rospy.is_shutdown():
        rospy.loginfo("In Loop")
        
        pub.publish(msg)
        rospy.loginfo("Published message:")
        rospy.loginfo(msg)
        
        rate.sleep()
        msg.speed_val.data = 0.3



def main():
    try:
        command_publisher()
    except rospy.ROSInterruptException:
        rospy.logwarn("ROSInterruptException")


if __name__ == '__main__':
    main()