import time
from adafruit_motorkit import MotorKit
import board



SPEED_VAL:float = 0.5

class Drives:
    """Motor drives class with methods to power and steer the motors
        self.motors[0] = m1: front right motor
        self.motors[1] = m2: front left motor
        self.motors[2] = m3: back right motor
        self.motors[3] = m4: back left motor"""
    
    def __init__(self) -> None:
        self.motors = [
            MotorKit(i2c=board.I2C()).motor1,
            MotorKit(i2c=board.I2C()).motor2,
            MotorKit(i2c=board.I2C()).motor3,
            MotorKit(i2c=board.I2C()).motor4]

    def forward(self, value:float = 0.5):
        """Powers motors to drive forward.
        Output Voltage between 0V and 12V

        Positional arguments:
        motors -- List of adafruit motor object 
        value  -- percentage of output voltage 0.0-1.0 (Default = 0.5)
        """
        self.motors[0].throttle = value
        self.motors[1].throttle = value
        self.motors[2].throttle = value
        self.motors[3].throttle = value

    def backward(self, value:float):
        """Powers motors to drive backward.
        Output Voltage between 0V and -12V

        Positional arguments:
        motors -- List of adafruit motor object 
        value  -- percentage of output voltage 0.0-1.0 (Default = 0.5)
        """
        if value > 0:
            value = -1.0 * value
        
        self.motors[0].throttle = value
        self.motors[1].throttle = value
        self.motors[2].throttle = value
        self.motors[3].throttle = value

    def left_angular(self, value:float):
        """Powers motors to drive left without moving forward.
        Output Voltage between 0V and 12V

        Positional arguments:
        value  -- percentage of output voltage 0.0-1.0 (Default = 0.5)
        """
        self.motors[0].throttle = value
        self.motors[1].throttle = -value
        self.motors[2].throttle = value
        self.motors[3].throttle = -value


    def right_angular(self, value:float):
        """Powers motors to drive right without moving forward.
        Output Voltage between 0V and 12V

        Positional arguments:
        value  -- percentage of output voltage 0.0-1.0 (Default = 0.5)
        """
        
        self.motors[0].throttle = -value
        self.motors[1].throttle = value
        self.motors[2].throttle = -value
        self.motors[3].throttle = value

        
    def turn_right(self, value:float):
        """Powers motors to drive right moving forward.
        Output Voltage between 0V and 12V

        Positional arguments: 
        value  -- percentage of output voltage 0.0-1.0 (Default = 0.5)
        """

        self.motors[0].throttle = value/3
        self.motors[1].throttle = value
        self.motors[2].throttle = value/3
        self.motors[3].throttle = value


    def turn_right(self, value:float):
        """Powers motors to drive left moving forward.
        Output Voltage between 0V and 12V

        Positional arguments:
        motors -- List of adafruit motor object 
        value  -- percentage of output voltage 0.0-1.0 (Default = 0.5)
        """

        self.motors[0].throttle = value
        self.motors[1].throttle = value/3
        self.motors[2].throttle = value
        self.motors[3].throttle = value/3
        

    def stop(self):
        """Sets output voltage to 0V and stop 
        Output Voltage between 0V and 12V"""
        for motor in self.motors:
            motor.throttle = 0




    


