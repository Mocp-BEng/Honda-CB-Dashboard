from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class CircularProgress(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # CUSTOM PROPERTIES
        self.value = 0
        self.width = 800
        self.height = 800
        self.progress_width = 100
        self.progress_rounded_cap = True
        self.progress_color = 0xAD0000
        self.max_value = 100
        self.font_family = "Segoe UI"
        self.font_size = 80
        self.suffix = "%"
        self.text_color = 0xFFFFFF
        self.innercircle_color = 0xAD0000 
        #BG
        self.enable_bg = True
        self.bg_color = 0x44475a

        # SET DEFAULT SIZE WITHOUT LAYOUT
        self.resize(self.width, self.height)
    
    # ADD DROPSHADOW
    def add_shadow(self, enable):
        if enable:
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(15)
            self.shadow.setXOffset(0)
            self.shadow.setXOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 120))
            self.setGraphicsEffect(self.shadow)

    # SET VALUE
    def set_value(self, value):
        self.value = value
        self.repaint() # Render progress bar after change value

    # PAINT EVENT (DESIGN YOUR CIRCULAR PROGRESS HERE)
    def paintEvent(self, event):
        # SET PROGRESS PARAMETERS
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = self.progress_width / 2
        value = self.value * 120 / self.max_value

        # PAINTER
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing) # remove pixelared edges
        paint.setFont(QFont(self.font_family, self.font_size))

        # CREATE RECTANGLE
        rect = QRect(0, 0, self.width, self.height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)

        # PEN
        pen = QPen()
        pen.setColor(QColor(self.progress_color))
        pen.setWidth(self.progress_width)
        # Set Round Cap
        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)

        # CREATE INNERCIRCLE
        pen.setColor(QColor(self.innercircle_color))
        paint.setPen(QPen(Qt.black, 4, Qt.SolidLine))
        radialGradient = QRadialGradient(QPoint(400,400), 160)# center point and radious
        radialGradient.setColorAt(0.7, self.innercircle_color)
        radialGradient.setColorAt(1.0, Qt.black)
        paint.setBrush(QBrush(radialGradient))
        paint.drawRect(200, 200, 400, 400)

        # ENABLE BG
        if self.enable_bg:
            pen.setColor(QColor(self.bg_color))
            paint.setPen(pen)
            paint.drawArc(margin, margin, width, height, -120 * 16, -120 * 16)
            paint.drawArc(margin, margin, width, height, -60 * 16, 120 * 16)

        # CREATE ARC / CIRCULAR PROGRESS
        pen.setColor(QColor(self.progress_color))
        paint.setPen(pen)
        paint.drawArc(margin, margin, width, height, -120 * 16, -value * 16)
        paint.drawArc(margin, margin, width, height, -60 * 16, value * 16)

        # CREATE TEXT
        pen.setColor(QColor(self.text_color))
        paint.setPen(pen)
        paint.drawText(rect, Qt.AlignCenter, f"{self.value}{self.suffix}")

        # END
        paint.end()

    