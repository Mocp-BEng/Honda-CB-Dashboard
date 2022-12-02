# Import Python Library
import math
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
import sys
from Window import Window
from PyQt5 import QtWidgets

# Import Functions
from circle_parameters import calculateCircleParameters
from charging_gif import chargingGif
from read_can_data import readCanData

can_data = readCanData()

App = QApplication(sys.argv)
window = Window()

if can_data.Charging == True:
    ui = chargingGif()
    ui.setupUi(window)
    window.show()


sys.exit(App.exec())

