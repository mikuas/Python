# coding:utf-8


"""
    窗口事件
"""
import sys

from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout
from PySide6.QtGui import QKeySequence, Qt



class Window(QWidget):
    def __init__(self):
        super().__init__()

    """ 窗口大小改变事件 """
    def resizeEvent(self, event):
        super().resizeEvent(event)
        print('窗口大小改变')

    """ 窗口移动事件 """
    def moveEvent(self, event):
        super().moveEvent(event)
        print('窗口移动')

    """ 关闭事件 """
    def closeEvent(self, event):
        super().closeEvent(event)
        event.ignore()
        print('窗口关闭')

    """ 窗口隐藏事件 """
    def hideEvent(self, event):
        super().hideEvent(event)
        print('窗口隐藏')

    """ 窗口显示事件 """
    def showEvent(self, event):
        super().showEvent(event)
        print('窗口显示')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.resize(800, 500)
    window.show()
    sys.exit(app.exec())