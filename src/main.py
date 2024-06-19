import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon

from main_app import HeartFailurePredictor

try:
    from ctypes import windll  # Only exists on Windows
    myappid = 'com.moodreflect.v1'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('assets/images/logo-1024px.png'))
    window = HeartFailurePredictor()
    window.show()

    sys.exit(app.exec())
