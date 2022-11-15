import math
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from circle_parameters import calculateCircleParameters
from read_can_data import readCanData
from circular_gauge import CircularGauge

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
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def paintBackground(self):
        mainCircle = QPainter()
        mainCircle.begin(self)
        mainCircle.setPen(QPen(Qt.white, self.circle_parameters.arcwidth, cap=Qt.FlatCap))
        mainCircle.setBrush(Qt.white)
        mainCircle.drawArc(int(self.circle_parameters.xyPosMain), int(self.circle_parameters.xyPosMain), int(self.circle_parameters.dMain), 
        int(self.circle_parameters.dMain), int(math.degrees(-self.circle_parameters.alpha)) * 16, int(math.degrees(self.circle_parameters.spanAngleMain)) * 16)

        leftSmallCircle = QPainter()
        leftSmallCircle.begin(self)
        leftSmallCircle.setPen(QPen(Qt.white, self.circle_parameters.arcwidth, cap=Qt.FlatCap))
        leftSmallCircle.setBrush(Qt.white)
        leftSmallCircle.drawArc(int(self.circle_parameters.xSmallCircle), int(self.circle_parameters.ySmallCircle), int(self.circle_parameters.dSmall), 
        int(self.circle_parameters.dSmall), int(math.degrees(self.circle_parameters.beta)) * 16, int(math.degrees(self.circle_parameters.spanAngleSmall)) * 16)

        rightSmallCircle = QPainter()
        rightSmallCircle.begin(self)
        rightSmallCircle.setPen(QPen(Qt.white, self.circle_parameters.arcwidth, cap=Qt.FlatCap))
        rightSmallCircle.setBrush(Qt.white)
        rightSmallCircle.drawArc(int(self.circle_parameters.WindowSize - self.circle_parameters.xSmallCircle - 2 * self.circle_parameters.rSmall), 
        int(self.circle_parameters.ySmallCircle), int(self.circle_parameters.dSmall), int(self.circle_parameters.dSmall), 
        int(180 - math.degrees(self.circle_parameters.beta)) * 16, int(-math.degrees(self.circle_parameters.spanAngleSmall)) * 16)
        
        leftLine = QPainter()
        leftLine.begin(self)
        leftLine.setPen(QPen(Qt.white,self.circle_parameters. arcwidth, cap=Qt.FlatCap))
        leftLine.setBrush(Qt.white)
        leftLine.drawLine(int(self.circle_parameters.xLineStart+self.circle_parameters.offset), int(self.circle_parameters.yLineStart + self.circle_parameters.offset), 
        int(self.circle_parameters.xLineEnd + self.circle_parameters.offset), int(self.circle_parameters.yLineEnd + self.circle_parameters.offset))
        
        rightLine = QPainter()
        rightLine.begin(self)
        rightLine.setPen(QPen(Qt.white, self.circle_parameters.arcwidth, cap=Qt.FlatCap))
        rightLine.setBrush(Qt.white)
        rightLine.drawLine(int(self.circle_parameters.WindowSize - self.circle_parameters.offset), int(self.circle_parameters.yLineEnd + self.circle_parameters.offset), 
        int(self.circle_parameters.WindowSize - self.circle_parameters.xLineStart), int(self.circle_parameters.yLineStart + self.circle_parameters.offset)) 

        CircularGauge(self, self.can_data)   

    def paintEvent(self, event):
        frameCircle = QPainter()
        frameCircle.begin(self)
        frameCircle.setPen(Qt.red)
        frameCircle.setBrush(Qt.red)
        frameCircle.drawArc(0, 0, self.circle_parameters.WindowSize, self.circle_parameters.WindowSize, 0, 360 * 16)
        
        self.paintBackground()