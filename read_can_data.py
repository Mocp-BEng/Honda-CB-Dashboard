from dataclasses import dataclass
import math
@dataclass
class CanValues:
    MotorCurrent: float
    MotorRpm: float
    Charging: bool
    
def readCanData():
    # To-Do read values from can 
    MotorCurrent = 200 # [A]
    MotorRpm = 5000 # [1/min]
    Charging = False 

    return CanValues(
    MotorCurrent,
    MotorRpm,
    Charging,
    )