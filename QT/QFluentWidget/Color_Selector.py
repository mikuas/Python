import sys
from symtable import Function

from PySide6.QtCore import QSize, QUrl
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget
from PySide6.QtGui import Qt
from networkx.algorithms.bipartite.basic import color
from qfluentwidgets import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 450)
        centerWindget = QWidget(self)
        mainLayout = QVBoxLayout(centerWindget)

        '''颜色选择器'''
        self.button = ColorPickerButton(QColor("#5012aaa2"), 'Background Color', self, enableAlpha=True)
        self.resize(800, 720)
        self.button.move(352, 312)
        self.setStyleSheet("demo{background:white}")

        w = ColorDialog(QColor(0, 255, 255), "Select Color", self, enableAlpha=False)
        w.colorChanged.connect(lambda color : print(color.name))

        self.setStyleSheet("demo{background:white}")

        # button = PushButton('Select Color')
        # button.clicked.connect(w.exec)
        mainLayout.addWidget(self.button)
        self.setCentralWidget(centerWindget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())