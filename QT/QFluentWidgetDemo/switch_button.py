import sys
from symtable import Function

from PySide6.QtCore import QSize, QUrl
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget
from PySide6.QtGui import Qt
from qfluentwidgets import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 450)
        centerWindget = QWidget(self)
        mainLayout = QVBoxLayout(centerWindget)

        '''开关按钮'''
        self.button = SwitchButton(self)
        # 覆盖默认文本
        self.button.setOffText("关闭")
        self.button.setOnText("开启")

        self.button.checkedChanged.connect(lambda checked: print("是否选中按钮：", checked))

        mainLayout.addWidget(self.button)
        self.setCentralWidget(centerWindget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())