import sys
from symtable import Function

from PySide6.QtCore import QSize, QUrl, QTime
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget
from PySide6.QtGui import Qt
from qfluentwidgets import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 450)
        centerWindget = QWidget(self)
        mainLayout = QVBoxLayout(centerWindget)

        '''时间选择器'''
        # timePicker = TimePicker()
        # 显示 AM/PM
        timePicker = AMTimePicker()

        # 设置当前时间
        timePicker.setTime(QTime(13, 53, 26))

        # 获取当前时间
        print(timePicker.time)

        # 时间发生改变
        timePicker.timeChanged.connect(lambda time: print(time.toString()))

        mainLayout.addWidget(timePicker)
        self.setCentralWidget(centerWindget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())