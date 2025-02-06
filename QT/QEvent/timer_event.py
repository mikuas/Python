# coding:utf-8


"""
    计时器事件
"""
import sys

from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout
from PySide6.QtCore import QTimer
from PySide6.QtGui import QKeySequence, Qt



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.timer = QTimer(self)

        self.startTimer(1000)

    def timerEvent(self, event):
        super().timerEvent(event)
        self.count += 1
        print(self.count)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.resize(800, 500)
    window.show()
    sys.exit(app.exec())