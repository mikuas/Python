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

        '''滑动条'''
        # 垂直 Qt.Vertical
        # 水平
        self.slier = Slider(Qt.Horizontal)
        self.slier.setFixedWidth(200)
        # 设置取值范围和当前值
        self.slier.setRange(0, 50)
        self.slier.setValue(20)


        mainLayout.addWidget(self.slier)
        self.setCentralWidget(centerWindget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())