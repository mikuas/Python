import sys
from tkinter import Spinbox

from PySide6.QtCore import Qt, QEasingCurve, QTimer
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QApplication
from qfluentwidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        '''微调框'''
        # DoubleSpinBox()
        # TimeEdit()
        # DateEdit()
        # DateTimeEdit()
        sp = SpinBox(self)
        sp.setFixedWidth(100)
        # 设置范围
        sp.setRange(0, 100)
        # 设置当前值
        sp.setValue(50),
        # 监听数值改变信号
        sp.valueChanged.connect(lambda value: print(value))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
