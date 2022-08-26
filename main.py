import sys
from mainWindow import *

# 1. Import `QApplication` and all the required widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

# 2. Create an instance of QApplication
app = QApplication(sys.argv)

# 3. Create an instance of your application's GUI
mainWindow = setMainWindow()

# 4. Show your application's GUI
mainWindow.show()

# 5. Run your application's event loop (or main loop)
sys.exit(app.exec_())