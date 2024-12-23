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

        '''图标组件'''
        w = IconWidget(FluentIcon.AIRPLANE)
        # 更换图标  类型为 FluentIconBase 子类

        w.setIcon(InfoBarIcon.SUCCESS)
        # colored 亮色 暗色 主题颜色
        w.setIcon(FluentIcon.AIRPLANE.colored(Qt.red, Qt.blue))

        w.setFixedSize(20, 20)


        mainLayout.addWidget(w)
        self.setCentralWidget(centerWindget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())