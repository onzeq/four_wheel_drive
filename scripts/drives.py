import time
from adafruit_motorkit import MotorKit
import board



SPEED_VAL:float = 0.5

def forward(motors:list, value:float = 0.5):
    """Powers motors to drive forward.
    Output Voltage between 0V and 12V

    Positional arguments:
    motors -- List of adafruit motor object 
    value  -- percentage of output voltage 0.0-1.0 (Default = 0.5)
    """
    for motor in motors:
        motor.throttle = value

def backward(motors:list, value:float):
    """Powers motors to drive backward.
    Output Voltage between 0V and -12V

    Positional arguments:
    motors -- List of adafruit motor object 
    value  -- percentage of output voltage 0.0-1.0 (Default = 0.5)
    """
    if value > 0:
        value = -1.0 * value
    
    for motor in motors:
        motor.throttle = value

def left_angular(motors:list, value:float):
    """Powers motors to drive left without moving forward.
    Output Voltage between 0V and 12V

    Positional arguments:
    motors -- List of adafruit motor object 
    value  -- percentage of output voltage 0.0-1.0 (Default = 0.5)
    """
    motors[0].throttle = value
    motors[1].throttle = -value
    motors[2].throttle = value
    motors[3].throttle = -value


def right_angular(motors:list, value:float):
    """Powers motors to drive right without moving forward.
    Output Voltage between 0V and 12V

    Positional arguments:
    motors -- List of adafruit motor object 
    value  -- percentage of output voltage 0.0-1.0 (Default = 0.5)
    """
    
    motors[0].throttle = -value
    motors[1].throttle = value
    motors[2].throttle = -value
    motors[3].throttle = value

    
def turn_right(motors:list, value:float):
    """Powers motors to drive right moving forward.
    Output Voltage between 0V and 12V

    Positional arguments:
    motors -- List of adafruit motor object 
    value  -- percentage of output voltage 0.0-1.0 (Default = 0.5)
    """

    motors[0].throttle = value/3
    motors[1].throttle = value
    motors[2].throttle = value/3
    motors[3].throttle = value


def turn_right(motors:list, value:float):
    """Powers motors to drive left moving forward.
    Output Voltage between 0V and 12V

    Positional arguments:
    motors -- List of adafruit motor object 
    value  -- percentage of output voltage 0.0-1.0 (Default = 0.5)
    """

    motors[0].throttle = value
    motors[1].throttle = value/3
    motors[2].throttle = value
    motors[3].throttle = value/3
    

def stop(motors):
    """Sets output voltage to 0V and stop 
    Output Voltage between 0V and 12V

    Positional arguments:
    motors -- List of adafruit motor object 
    """
    for motor in motors:
        motor.throttle = 0

def get_motors() ->list :
    """Returns list with four motor objects of adafruit board
    list[0] = m1: front right motor
    list[1] = m2: front left motor
    list[2] = m3: back right motor
    list[3] = m4: back left motor

    Return:
    list of motors
    """
    kit = MotorKit(i2c=board.I2C())
    
    m_vr = kit.motor1
    m_vl = kit.motor2
    m_hr = kit.motor3
    m_hl = kit.motor4

    return [m_vr, m_vl, m_hr, m_hl]



    


