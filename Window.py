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
        # self.label_1 = QLabel('30', self)
        # self.label_1.move(300, 300)
        # self.label_1.setStyleSheet("background-color : none; color : white; font:12pt Arial")
        self.show() 
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        staticLabel(self, self.circle_parameters)
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
            circularGauge(self, self.can_data, self.circle_parameters)
            # staticLabel(self, self.circle_parameters)

            # creating a vertical layout
            layout = QVBoxLayout()
    
            # creating font object
            font = QFont('Arial', 120, QFont.Bold)
    
            # creating a label object
            self.label = QLabel()
    
            # setting centre alignment to the label
            self.label.setAlignment(Qt.AlignCenter)
    
            # setting font to the label
            self.label.setFont(font)
    
            # adding label to the layout
            layout.addWidget(self.label)
    
            # setting the layout to main window
            self.setLayout(layout)
    
            # creating a timer object
            timer = QTimer(self)
    
            # adding action to timer
            timer.timeout.connect(self.showTime)
    
            # update the timer every second
            timer.start(1000)

            # #Blinker
            blinkerLeft(self, self.circle_parameters) 
            blinkerRight(self, self.circle_parameters)

            self.show() 
    
    # method called by timer
    def showTime(self):
 
        # getting current time
        current_time = QTime.currentTime()
 
        # converting QTime object to string
        label_time = current_time.toString('hh:mm:ss')
 
        # showing it to the label
        self.label.setText(label_time)
        https://www.geeksforgeeks.org/pyqt5-create-a-digital-clock/