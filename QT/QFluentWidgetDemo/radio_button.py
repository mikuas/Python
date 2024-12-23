import sys
from symtable import Function

from PySide6.QtCore import QSize, QUrl
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QButtonGroup
from PySide6.QtGui import Qt
from qfluentwidgets import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 450)
        centerWindget = QWidget(self)
        mainLayout = QVBoxLayout(centerWindget)

        '''单选按钮'''
        button1 = RadioButton()
        button1.setText('Option 1')
        button2 = RadioButton()
        button2.setText('Option 2')
        button3 = RadioButton()
        button3.setText('Option 3')

        buttonGroup = QButtonGroup(self)
        buttonGroup.addButton(button1)
        buttonGroup.addButton(button2)
        buttonGroup.addButton(button3)

        # 当前选中的按钮发生改变
        buttonGroup.buttonToggled.connect(lambda button: print(button.text()))

        mainLayout.addWidget(button1)
        mainLayout.addWidget(button2)
        mainLayout.addWidget(button3)
        self.setCentralWidget(centerWindget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())