from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
import math
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt


def CircularGauge(self, CanValues):
    rightLine = QPainter()
    rightLine.begin(self)
    rightLine.setPen(QPen(Qt.white, self.circle_parameters.arcwidth, cap=Qt.FlatCap))
    rightLine.setBrush(Qt.white)
    rightLine.drawLine(int(300), int(CanValues.MotorCurrent), int(500), int(500))  