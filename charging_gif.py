from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import sys

class chargingGif(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # create label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0,0, 800, 800))
        self.label.setMinimumSize(QtCore.QSize(800, 800))
        self.label.setMaximumSize(QtCore.QSize(800, 800))
        self.label.setObjectName("label")

        # add label to main window
        MainWindow.setCentralWidget(self.centralwidget)

        # set qmovie as label
        self.movie = QMovie("charging.gif")
        self.label.setMovie(self.movie)
        self.movie.start()