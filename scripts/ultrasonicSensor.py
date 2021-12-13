#!/usr/bin/env python3
import RPi.GPIO as GPIO
import rospy

from four_wheel_drive.msg import Drives_command
import constants


TRIG = 21
ECHO = 20
SONAR_SPEED = 17150.0


def GPIO_setup():
    rospy.loginfo("Setup GPIO for Sonar Sensor")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.output(TRIG, False) 
    rospy.loginfo("Setup Sonar Sensor finished. Settle Sensor")
    rospy.sleep(0.2)



def distance_calculation():
    #send burst
    
    GPIO.output(TRIG, True)
    rospy.sleep(1e-5)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO) == 0:
        pulse_start = rospy.get_time()
    while GPIO.input(ECHO) == 1:
        pulse_end = rospy.get_time()
    
    pulse_duration = pulse_end-pulse_start
    return pulse_duration*SONAR_SPEED

def callback_shutdown():
    GPIO.output(TRIG, False)
    print("PIN low")


def main():
    rospy.init_node("sonar_sensor")
    
    pub_sensor = rospy.Publisher("drives_commander", Drives_command)

    rospy.on_shutdown(callback_shutdown)
    GPIO_setup()

    rate = rospy.Rate(15)
    msg = Drives_command()
    msg.command.data = constants.STOP
    msg.speed_val.data = 0.0
    while not rospy.is_shutdown():
        distance = distance_calculation()
        rospy.loginfo("Distance in cm: %f", distance)
        if(distance < constants.MIN_DISTANCE):
            pub_sensor.publish(msg)
        rate.sleep()





if __name__ == '__main__':
    main()
