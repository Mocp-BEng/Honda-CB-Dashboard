from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
import math
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter, QPen, QConicalGradient
from PyQt5.QtCore import *


## Scaling
maxAngle = 90
arcWidth = 150
startAngle = 28
maxAmp = 400
maxRpm = 7000
amp2deg = maxAngle / maxAmp
rpm2deg = maxAngle / maxRpm

def circularGauge(self, CanValues, circlePar):
        # Arc background
        ampArcBg = QPainter()
        ampArcBg.begin(self)
        ampArcBg.setRenderHint(QPainter.Antialiasing) # remove pixelared edges
        ampArcBg.setPen(QPen(Qt.white, arcWidth, cap=Qt.FlatCap))
        ampArcBg.drawArc(int(arcWidth/2), int(arcWidth/2), int(circlePar.WindowSize-arcWidth), int(self.circle_parameters.WindowSize-arcWidth), 
        int(startAngle + 180 ) * 16, int(-maxAmp * amp2deg) * 16)

        rpmArcBg = QPainter()
        rpmArcBg.begin(self)
        rpmArcBg.setRenderHint(QPainter.Antialiasing)
        rpmArcBg.setPen(QPen(Qt.white, arcWidth, cap=Qt.FlatCap))
        rpmArcBg.drawArc(int(arcWidth/2), int(arcWidth/2), int(self.circle_parameters.WindowSize-arcWidth), int(self.circle_parameters.WindowSize-arcWidth), 
        int(-startAngle) * 16, int(maxRpm * rpm2deg) * 16)
        
        #Value
        ampArc = QPainter()
        ampArc.begin(self)
        ampArc.setRenderHint(QPainter.Antialiasing)
        ampArc.setPen(QPen(Qt.red, arcWidth, cap=Qt.FlatCap))
        ampArc.drawArc(int(arcWidth/2), int(arcWidth/2), int(self.circle_parameters.WindowSize-arcWidth), int(self.circle_parameters.WindowSize-arcWidth), 
        int(startAngle + 180 ) * 16, int(-CanValues.MotorCurrent * amp2deg) * 16)

        rpmArc = QPainter()
        rpmArc.begin(self)
        rpmArc.setRenderHint(QPainter.Antialiasing)
        rpmArc.setPen(QPen(Qt.red, arcWidth, cap=Qt.FlatCap))
        rpmArc.drawArc(int(arcWidth/2), int(arcWidth/2), int(self.circle_parameters.WindowSize-arcWidth), int(self.circle_parameters.WindowSize-arcWidth), 
        int(-startAngle) * 16, int(CanValues.MotorRpm * rpm2deg) * 16)