from dataclasses import dataclass
import math
@dataclass
class CanValues:
    MotorCurrent: float
    MotorRpm: float
    
def readCanData():
    # To-Do read values from can 
    MotorCurrent = 200 # [A]
    MotorRpm = 5000 # [1/min]

    return CanValues(
    MotorCurrent,
    MotorRpm,
    )