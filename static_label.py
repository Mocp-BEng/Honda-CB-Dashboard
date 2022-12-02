from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
import sys

def staticLabel(self, circlePar):
    # creating a label widget
    # by default label will display at top left corner
    self.label_1 = QLabel('Arial font', self)
  
    # moving position
    self.label_1.move(300, 300)
  
    # setting font and size
    self.label_1.setFont(QFont('Arial', 10))