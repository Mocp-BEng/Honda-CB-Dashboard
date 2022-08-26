# mainWindow.py>

#import
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

# function mainWindow
def setMainWindow():
    window = QWidget()
    window.setWindowTitle('HondaCB200e')
    window.setGeometry(0, 0, 800, 800)
    window.move(60, 15)
    window.setStyleSheet("background-color: black;")
    return window
