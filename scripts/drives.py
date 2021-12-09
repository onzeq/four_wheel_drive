import time
from adafruit_motorkit import MotorKit
import board


def forward(motor, value:float):
    motor.throttle = value
    

def stop(motor):
    motor.throttle = 0



def main():
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
    

        
    


if __name__ == '__main__':
    main()
    


