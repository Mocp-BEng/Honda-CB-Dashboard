import math
# Import PyQt 
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5 import QtCore

# Import Functions
from circle_parameters import calculateCircleParameters
from read_can_data import readCanData
from circular_gauge import circularGauge
from blinker_left import blinkerLeft, blinkerRight
from paint_background import paintBackground
from static_label import staticLabel
# from charging_gif import chargingGif

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Honda 200e Dashboard"
        self.top= 0
        self.left= 0
        self.setStyleSheet("background-color: black;")
        self.circle_parameters = calculateCircleParameters()
        self.can_data = readCanData()
        self.width = self.circle_parameters.WindowSize
        self.height = self.circle_parameters.WindowSize
        # creating a label widget
        # by default label will display at top left corner
        self.label_1 = QLabel('Light green', self)
    
        # moving position
        self.label_1.move(300, 300)
    
        # setting up background color
        self.label_1.setStyleSheet("background-color: lightgreen")
        self.show() 
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        staticLabel(self, self.circle_parameters)
        self.show()                 

    def paintEvent(self, event):
        if self.can_data.Charging == False:
            frameCircle = QPainter()
            frameCircle.begin(self)
            frameCircle.setPen(Qt.red)
            frameCircle.setBrush(Qt.red)
            frameCircle.drawArc(0, 0, self.circle_parameters.WindowSize, self.circle_parameters.WindowSize, 0, 360 * 16)
    
            paintBackground(self, self.circle_parameters)
            circularGauge(self, self.can_data, self.circle_parameters)
            # staticLabel(self, self.circle_parameters)


            # #Blinker
            blinkerLeft(self, self.circle_parameters) 
            blinkerRight(self, self.circle_parameters)

            # creating a label widget
            # by default label will display at top left corner
            self.label_1 = QLabel('Light green', self)
    
            # moving position
            self.label_1.move(300, 300)
    
            # setting up background color
            self.label_1.setStyleSheet("background-color: lightgreen")
            self.show() 