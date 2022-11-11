# Import math Library
import math
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
import sys
import plotly.graph_objects as go

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

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Honda 200e Dashboard"
        self.top= 0
        self.left= 0
        self.width = WindowSize
        self.height = WindowSize
        self.setStyleSheet("background-color: black;")
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
    
    def paintEvent(self, event):
        frameCircle = QPainter()
        frameCircle.begin(self)
        frameCircle.setPen(Qt.red)
        frameCircle.setBrush(Qt.red)
        frameCircle.drawArc(0, 0, WindowSize, WindowSize, 0, 360 * 16)
        
        mainCircle = QPainter()
        mainCircle.begin(self)
        mainCircle.setPen(QPen(Qt.white, arcwidth, cap=Qt.FlatCap))
        mainCircle.setBrush(Qt.white)
        mainCircle.drawArc(int(xyPosMain), int(xyPosMain), int(dMain), int(dMain), int(math.degrees(-alpha)) * 16, int(math.degrees(spanAngleMain)) * 16)
        
        leftSmallCircle = QPainter()
        leftSmallCircle.begin(self)
        leftSmallCircle.setPen(QPen(Qt.white, arcwidth, cap=Qt.FlatCap))
        leftSmallCircle.setBrush(Qt.white)
        leftSmallCircle.drawArc(int(xSmallCircle), int(ySmallCircle), int(dSmall), int(dSmall), int(math.degrees(beta)) * 16, int(math.degrees(spanAngleSmall)) * 16)
        
        rightSmallCircle = QPainter()
        rightSmallCircle.begin(self)
        rightSmallCircle.setPen(QPen(Qt.white, arcwidth, cap=Qt.FlatCap))
        rightSmallCircle.setBrush(Qt.white)
        rightSmallCircle.drawArc(int(WindowSize - xSmallCircle - 2 * rSmall), int(ySmallCircle), int(dSmall), int(dSmall), int(180 - math.degrees(beta)) * 16, int(-math.degrees(spanAngleSmall)) * 16)
        
        leftLine = QPainter()
        leftLine.begin(self)
        leftLine.setPen(QPen(Qt.white, arcwidth, cap=Qt.FlatCap))
        leftLine.setBrush(Qt.white)
        leftLine.drawLine(int(xLineStart+offset), int(yLineStart + offset), int(xLineEnd + offset), int(yLineEnd+offset))
        
        rightLine = QPainter()
        rightLine.begin(self)
        rightLine.setPen(QPen(Qt.white, arcwidth, cap=Qt.FlatCap))
        rightLine.setBrush(Qt.white)
        rightLine.drawLine(int(WindowSize-xLineStart), int(yLineStart+offset), int(WindowSize), int(yLineEnd+offset))
        

App = QApplication(sys.argv)
window = Window()

sys.exit(App.exec())