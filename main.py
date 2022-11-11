# Import math Library
import math
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
import sys
import plotly.graph_objects as go
from circle_parameters import calculateCircleParameters
from back_ground_window import BackGroundWindow
      

App = QApplication(sys.argv)
window = BackGroundWindow()

sys.exit(App.exec())