import math
# Import PyQt 
from PyQt5.QtWidgets import QVBoxLayout, QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import QTimer, QTime, Qt
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

# Global test variables
counter_rpm = 0
counter_A = 0

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
        staticLabel(self)
        
        # QTIMER
        self.timerrpm = QTimer()
        self.timerrpm.timeout.connect(self.updaterpm)
        self.timerrpm.start(1)

        # QTIMER
        self.timerA = QTimer()
        self.timerA.timeout.connect(self.updateA)
        self.timerA.start(25)

        self.show() 
        self.InitWindow()

    # UPDATE PROGRESS BAR 
    def updaterpm(self):
        # SET VALUE TO PROGRESS BAR
        self.can_data.setMotorRpm(counter_rpm)
        # CLOSE SPLASH SCREEN AND OPEN MAIN APP
        if self.can_data.MotorRpm >= 6000:
            # STOP TIMER
            self.can_data.MotorRpm = 0
        # INCRESE COUNTER
        self.can_data.MotorRpm += 1

    # UPDATE PROGRESS BAR 
    def updateA(self):
        # SET VALUE TO PROGRESS BAR
        self.can_data.setMotorCurrent(counter_A)
        # CLOSE SPLASH SCREEN AND OPEN MAIN APP
        if self.can_data.MotorCurrent >= 350:
            # STOP TIMER
            self.can_data.MotorCurrent = 0
        # INCRESE COUNTER
        self.can_data.MotorCurrent += 1

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()                 

    def paintEvent(self, event):
        if self.can_data.Charging == False:
            #### Indicator for screen size
            frameCircle = QPainter()
            frameCircle.begin(self)
            frameCircle.setPen(Qt.red)
            frameCircle.setBrush(Qt.red)
            frameCircle.drawArc(0, 0, self.circle_parameters.WindowSize, self.circle_parameters.WindowSize, 0, 360 * 16)
            #####
            
            paintBackground(self, self.circle_parameters)
            self.progressBar = circularGauge()
            self.progressBar.circularProgressBar(self, self.can_data, self.circle_parameters)

            # staticLabel(self, self.circle_parameters)

            # #Blinker
            blinkerLeft(self, self.circle_parameters) 
            blinkerRight(self, self.circle_parameters)
            self.show() 
    

        # https://www.geeksforgeeks.org/pyqt5-create-a-digital-clock/