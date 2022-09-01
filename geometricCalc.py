# Import math Library
import math
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import sys

# Return the sine of different values
# Diameter circles
dMain = 500
dSmall = 60

# Angle main circles
spanAngleMain = 260
spanAngleLeft = 120

# Calculation postion and start angle
xyPosMain = 400 - (dMain / 2)
calcAngleMain = (360 - spanAngleMain) / 2
startAngleMain = calcAngleMain - 90

# calculation enpoints and slopes 
GMain = math.sin(math.radians(calcAngleMain)) * (dMain/2)
AMain = math.cos(math.radians(calcAngleMain)) * (dMain/2)

GLeft = math.sin(math.radians(calcAngleMain)) * (dSmall/2)
ALeft = math.cos(math.radians(calcAngleMain)) * (dSmall/2)

xPosLeft = 400 - GMain - GLeft - (dSmall/2)
yPosLeft = 400 + AMain + (ALeft - dSmall/2)


GEndLeft = math.sin(math.radians(startAngleMain)) * (dSmall/2)
AEndLeft = math.cos(math.radians(startAngleMain)) * (dSmall/2)

startAngleLeft = 90 - calcAngleMain

xPosLineStart = 400 - GMain - GLeft - GEndLeft
yPosLineStart = 400 + AMain + ALeft + AEndLeft

GEnd = math.sin(math.radians(startAngleMain)) * (dSmall/2)
AEndLeft = math.cos(math.radians(startAngleMain)) * (dSmall/2)

xPosLineEnd = 0
yPosLineEnd = yPosLineStart + xPosLineStart * (AEndLeft/GEndLeft)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Drawing Tutorial"
        self.top= 150
        self.left= 150
        self.width = 800
        self.height = 800
        self.setStyleSheet("background-color: black;")
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
    
    def paintEvent(self, event):
        mainCircle = QPainter()
        mainCircle.begin(self)
        mainCircle.setRenderHint(QPainter.Antialiasing)
        mainCircle.setPen(Qt.red)
        mainCircle.setBrush(Qt.red)
        mainCircle.drawArc(0, 0, 800, 800, 0 * 16, 360 * 16)
        innerCircle = QPainter()
        innerCircle.begin(self)
        innerCircle.setRenderHint(QPainter.Antialiasing)
        innerCircle.setPen(Qt.white)
        innerCircle.setBrush(Qt.white)
        innerCircle.drawArc(int(xyPosMain), int(xyPosMain), int(dMain), int(dMain), int(startAngleMain) * 16, int(spanAngleMain) * 16)
        leftCircle = QPainter()
        leftCircle.begin(self)
        leftCircle.setRenderHint(QPainter.Antialiasing)
        leftCircle.setPen(Qt.white)
        leftCircle.setBrush(Qt.white)
        leftCircle.drawArc(int(xPosLeft), int(yPosLeft), int(dSmall), int(dSmall), int(startAngleLeft) * 16, int(-spanAngleLeft) * 16)
        leftLine = QPainter()
        leftLine.begin(self)
        leftLine.setRenderHint(QPainter.Antialiasing)
        leftLine.setPen(Qt.white)
        leftLine.setBrush(Qt.white)
        leftLine.drawLine(int(xPosLineStart), int(yPosLineStart), int(xPosLineEnd), int(yPosLineEnd))
        rightCircle = QPainter()
        rightCircle.begin(self)
        rightCircle.setRenderHint(QPainter.Antialiasing)
        rightCircle.setPen(Qt.white)
        rightCircle.setBrush(Qt.white)
        rightCircle.drawArc(800-195-30, 589, 30, 30, 120 * 16, 120 * 16)
        rightLine = QPainter()
        rightLine.begin(self)
        rightLine.setRenderHint(QPainter.Antialiasing)
        rightLine.setPen(Qt.white)
        rightLine.setBrush(Qt.white)
        rightLine.drawLine(800-195, 589+30, 800, 700)
    

App = QApplication(sys.argv)
window = Window()

sys.exit(App.exec())