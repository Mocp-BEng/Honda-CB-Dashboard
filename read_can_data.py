from dataclasses import dataclass
import math
@dataclass
class CanValues:
    MotorCurrent: float
    
def readCanData():
    # To-Do read values from can 
    MotorCurrent = 222.2 # [A]

    return CanValues(
    MotorCurrent,
    )