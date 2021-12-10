import time
from adafruit_motorkit import MotorKit
import board



SPEED_VAL:float = 1

def forward(motors:list, value:float):
    for motor in motors:
        motor.throttle = value

def left_angular(motors:list, value:float):
    motors[0].throttle = value
    motors[1].throttle = -value
    motors[2].throttle = value
    motors[3].throttle = -value


def right_angular(motors:list, value:float):
    motors[0].throttle = -value
    motors[1].throttle = value
    motors[2].throttle = -value
    motors[3].throttle = value

    
def turn_right(motors:list, value:float):
    motors[0].throttle = value/3
    motors[1].throttle = value
    motors[2].throttle = value/3
    motors[3].throttle = value
    

def stop(motors):
    for motor in motors:
        motor.throttle = 0

def get_motors() ->list :
    kit = MotorKit(i2c=board.I2C())
    
    m_vr = kit.motor1
    m_vl = kit.motor2
    m_hr = kit.motor3
    m_hl = kit.motor4

    return [m_vr, m_vl, m_hr, m_hl]

def main():
    
    
    motors = get_motors()
    
    while 1:

        counter = 1
        speed = (counter%10)/10
        forward(motors, counter%10)
        time.sleep(0.1)


    

        
    


if __name__ == '__main__':
    main()
    


