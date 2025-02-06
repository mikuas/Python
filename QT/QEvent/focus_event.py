# coding:utf-8


"""
    焦点事件
"""
import sys

from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout
from PySide6.QtGui import QKeySequence, Qt


class LineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 设置焦点策略
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    """ 获得焦点事件 """
    def focusInEvent(self, event):
        super().focusInEvent(event)
        print("获得焦点")

    """ 失去焦点事件 """
    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        print("失去焦点")


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.lineEdit = LineEdit(self)
        self.layout.addWidget(self.lineEdit)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.resize(800, 500)
    window.show()
    sys.exit(app.exec())