#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import time
from adafruit_motorkit import MotorKit
import board

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def forward(motor, value:float):
    motor.throttle = value
    

def stop(motor):
    motor.throttle = 0
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", String, callback)

    kit = MotorKit(i2c=board.I2C())
    
    m1 = kit.motor1
    m2 = kit.motor2
    m3 = kit.motor3
    m4 = kit.motor4

    motors = [m1, m2, m3, m4]
    
    while 1:

        for motor in motors:
            forward(motor, 1.0)
    
        time.sleep(2)
    
        for motor in motors:
            stop(motor)

        time.sleep(2)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()