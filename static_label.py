from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
import sys

def staticLabel(self):
    self.label_1 = QLabel('30', self)
    self.label_1.move(300, 300)
    self.label_1.setStyleSheet("background-color : none; color : white; font:28pt Arial")