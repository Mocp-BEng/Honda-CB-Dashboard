from dataclasses import dataclass
import math
@dataclass
class CircleParameters:
    WindowSize: int
    dMain: float
    dSmall: float
    rMain: float
    rSmall: float
    arcwidth: float
    spanAngleMain: float
    spanAngleSmall: float
    xyPosMain: float
    calcAngleMain: float
    alpha: float
    beta: float
    xSmallCircle: float
    ySmallCircle: float
    xLineStart: float
    yLineStart: float
    xLineEnd: float
    yLineEnd: float
    offset: float

def calculateCircleParameters():
    ## Parameter 
    # Windows size 
    WindowSize = 800

    # Line thickness 
    arcwidth = 5

    # Diameter circles
    dMain = 500
    rMain = dMain / 2

    dSmall = 60
    rSmall = dSmall / 2

    # Angle main circles
    spanAngleMain = math.radians(240)
    spanAngleSmall = math.radians(90)

    xyPosMain = 400 - rMain
    calcAngleMain = (math.radians(360) - spanAngleMain) / 2

    alpha = (spanAngleMain - math.radians(180)) / 2
    beta = alpha - spanAngleSmall

    lengthC = math.sin(alpha) * rMain
    lengthD = math.cos(alpha) * rMain
    lengthE = math.sin(alpha) * rSmall
    lengthF = math.cos(alpha) * rSmall
    lengthG = math.sin(math.radians(90) - beta) * rSmall
    lengthH = math.cos(math.radians(90) - beta) * rSmall

    xSmallCircle = xyPosMain + rMain - lengthD - lengthF - rSmall
    ySmallCircle = xyPosMain + rMain + lengthC + lengthE - rSmall

    xLineStart = xSmallCircle + rSmall + lengthG
    yLineStart = ySmallCircle + rSmall - lengthH

    xLineEnd = 0
    yLineEnd = yLineStart + math.sin(math.radians(90) - beta) * xLineStart 
    offset = 0.0

    return CircleParameters(
        WindowSize,
        dMain,
        dSmall,
        rMain,
        rSmall,
        arcwidth,
        spanAngleMain,
        spanAngleSmall,
        xyPosMain,
        calcAngleMain,
        alpha,
        beta,
        xSmallCircle,
        ySmallCircle,
        xLineStart,
        yLineStart,
        xLineEnd,
        yLineEnd,
        offset,
    )