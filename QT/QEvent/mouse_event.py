# coding:utf-8


"""
    鼠标事件
"""
import sys

from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout
from PySide6.QtGui import Qt


class LineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

    """ 鼠标按下事件 """
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if event.button() == Qt.MouseButton.LeftButton:
            print("鼠标左键按下")
        elif event.button() == Qt.MouseButton.RightButton:
            print("鼠标右键按下")
        elif event.button() == Qt.MouseButton.MiddleButton:
            print("鼠标中键按下")

        # 阻止事件传递到父控件
        event.accept() # 事件被接受，停止传播

        event.ignore() # 事件被忽略，继续传递

    """ 鼠标释放事件 """
    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        if event.button() == Qt.MouseButton.LeftButton:
            print("鼠标左键释放")
        elif event.button() == Qt.MouseButton.RightButton:
            print("鼠标右键释放")
        elif event.button() == Qt.MouseButton.MiddleButton:
            print("鼠标中键释放")

    """ 鼠标双击事件 """
    def mouseDoubleClickEvent(self, event):
        super().mouseDoubleClickEvent(event)
        if event.button() == Qt.MouseButton.LeftButton:
            print("鼠标左键双击")
        elif event.button() == Qt.MouseButton.RightButton:
            print("鼠标右键双击")
        elif event.button() == Qt.MouseButton.MiddleButton:
            print("鼠标中键双击")

    """ 鼠标移动事件 """
    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        print(f'鼠标移动, 位置: {event.pos()}')
        # event.globalPos()

    """ 鼠标滚动事件 """
    def wheelEvent(self, event):
        super().wheelEvent(event)
        delta = event.angleDelta()
        print(f'鼠标滚动, 位置: {delta}')
        if delta.y() > 0:
            print('滚轮向上滚动')
        else:
            print('滚轮向下滚动')


    """ 鼠标进入事件 """
    def enterEvent(self, event):
        super().enterEvent(event)
        print('鼠标进入')

    """ 鼠标离开事件 """
    def leaveEvent(self, event):
        super().leaveEvent(event)
        print('鼠标离开')


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