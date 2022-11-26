from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen
from PyQt5 import QtCore
import sys

#define
yPos = 650
xPos = 150
length = 50 
height = 30
ratio = 0.5
lineWidth = 15

def blinkerLeft(self, circlePar):
        bLeft = QPainter()
        bLeft.begin(self)
        bLeft.setRenderHint(QPainter.Antialiasing)
        bLeft.setPen(QPen(QtCore.Qt.green, lineWidth, cap=QtCore.Qt.RoundCap))
        bLeft.setBrush(QtCore.Qt.red)
        bLeft.drawLine(xPos+length, yPos, xPos, yPos)
        bLeft.drawLine(xPos+ int(length*ratio), yPos+height, xPos, yPos)
        bLeft.drawLine(xPos+ int(length*ratio), yPos-height, xPos, yPos)

def blinkerRight(self, circlePar):
        bRight = QPainter()
        bRight.begin(self)
        bRight.setRenderHint(QPainter.Antialiasing)
        bRight.setPen(QPen(QtCore.Qt.green, lineWidth, cap=QtCore.Qt.RoundCap))
        bRight.setBrush(QtCore.Qt.white)
        bRight.drawLine(self.circle_parameters.WindowSize-xPos-length, yPos, self.circle_parameters.WindowSize-xPos, yPos)
        bRight.drawLine(self.circle_parameters.WindowSize-xPos- int(length*ratio), yPos+height, self.circle_parameters.WindowSize-xPos, yPos)
        bRight.drawLine(self.circle_parameters.WindowSize-xPos- int(length*ratio), yPos-height, self.circle_parameters.WindowSize-xPos, yPos)