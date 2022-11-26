# Import math Library
import math
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
import sys
from circle_parameters import calculateCircleParameters
from Window import Window
from PyQt5.QtWidgets import QWidget

App = QApplication(sys.argv)
window = Window()

sys.exit(App.exec())