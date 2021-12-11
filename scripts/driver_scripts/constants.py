from enum import Enum

class Commands(Enum):
    FORWARD         = 0
    BACKWARD        = 2
    LEFT_ANGULAR    = 4
    RIGHT_ANGULAR   = 8
    TURN_LEFT       = 16
    TURN_RIGHT      = 32
    STOP            = 64


SPEED_VAL:float = 0.5