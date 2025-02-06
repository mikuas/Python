# coding:utf-8


"""
    事件过滤器
"""
import sys

from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout
from PySide6.QtCore import QEvent


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.installEventFilter(self)

    """ 事件过滤器 """
    def eventFilter(self, watched, event):
        super().eventFilter(watched, event)
        if watched == self and event.type() in [QEvent.Type.Resize, QEvent.Type.Move]:
            self.count += 1
            print(self.count)
            return True # 拦截事件, 不继续传播
        return super().eventFilter(watched, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.resize(800, 500)
    window.show()
    sys.exit(app.exec())