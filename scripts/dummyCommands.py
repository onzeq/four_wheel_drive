#!/usr/bin/env python
import rospy
from four_wheel_drive.msg import Drives_command
from rospy.exceptions import ROSInterruptException
import driver_scripts.drives as drives

def command_publisher():
    pub = rospy.Publisher("drives_commander", Drives_command, queue_size=10)
    rospy.init_node("dummy_commander")
    
    msg = Drives_command()
    msg.command = drives.FORWARD
    msg.speed_val = 0.7

    counter = 0
    while not rospy.is_shutdown() and counter == 0:
        counter = 1
        pub.publish(msg)


def main():
    try:
        command_publisher()
    except rospy.ROSInterruptException:
        pass
