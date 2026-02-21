import sys
from PyQt6.QtWidgets import (QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,
                             QHBoxLayout)
from PyQt6.QtCore import QTimer,QTime,Qt

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec())