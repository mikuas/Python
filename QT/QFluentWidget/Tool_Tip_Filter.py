import sys

from PySide6.QtCore import Qt, QEasingCurve, QTimer
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QApplication
from qfluentwidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        '''工具提示'''
        self.resize(800, 450)
        button = PushButton("Hello", self)
        button.resize(100, 50)
        button.move(100, 100)
        button.setToolTip('这个你好')
        button.setToolTipDuration(1000)

        # 给按钮安装工具提示过滤器
        button.installEventFilter(ToolTipFilter(button, showDelay=300, position=ToolTipPosition.TOP))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
