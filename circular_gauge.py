from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
import math
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

#Calculation 
currentScaling = 0.5 # Scaling factor to 90 degrees 
CurrentArcWidth = 100

def CircularGauge(self, CanValues, circle_parameters):

    leftSmallCircle = QPainter()
    leftSmallCircle.begin(self)
    leftSmallCircle.setPen(QPen(Qt.white, CurrentArcWidth, cap=Qt.FlatCap))
    leftSmallCircle.setBrush(Qt.white)
    leftSmallCircle.drawArc(int(circle_parameters.xyPosMain), int(circle_parameters.xyPosMain), int(circle_parameters.dMain), 
    int(circle_parameters.dMain), int(math.degrees(circle_parameters.spanAngleMain)+180) * 16, int(-CanValues.MotorCurrent*currentScaling) * 16)