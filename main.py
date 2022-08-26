from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import sys

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
        innerCircle.drawArc(150, 150, 500, 500, 320 * 16, 260 * 16)
        leftCircle = QPainter()
        leftCircle.begin(self)
        leftCircle.setRenderHint(QPainter.Antialiasing)
        leftCircle.setPen(Qt.white)
        leftCircle.setBrush(Qt.white)
        leftCircle.drawArc(159, 555, 60, 60, 290 * 16, 120 * 16)
        leftLine = QPainter()
        leftLine.begin(self)
        leftLine.setRenderHint(QPainter.Antialiasing)
        leftLine.setPen(Qt.white)
        leftLine.setBrush(Qt.white)
        leftLine.drawLine(200, 553+60, 0, 700)
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