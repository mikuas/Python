# encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QPropertyAnimation, QPoint, Qt, QEasingCurve, QSize, QRect
from qfluentwidgets import PrimaryPushButton, LineEdit
from FluentWidgets import VerticalScrollWidget


class Window(VerticalScrollWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.resize(800, 500)

        self.moveBt = PrimaryPushButton('Move', self)
        self.moveBt.move(self.width() // 2 - 50, 50)

        self.lineEdit = LineEdit(self)
        self.lineEdit.setPlaceholderText('依次输入x, y, width, height, 用空格隔开')
        self.lineEdit.raise_()
        self.button = PrimaryPushButton("点击我改变上面按钮的按钮", self)
        self.vBoxLayout.addWidgets([self.lineEdit, self.button], alignment=Qt.AlignmentFlag.AlignBottom)

        self.connectSignalSlot()

    def connectSignalSlot(self):
        self.lineEdit.textChanged.connect(lambda text: print(text.split(' ')))
        self.button.clicked.connect(self.createGeometryAni)

    
    def createGeometryAni(self):
        self.posAni = QPropertyAnimation(self.moveBt, b'geometry') # 动画类型
        self.posAni.setDuration(1000) # 持续事件
        self.posAni.setStartValue(self.moveBt.geometry()) # 起始位置
        # self.posAni.setStartValue(QRect(self.moveBt.x(), self.moveBt.y(), self.moveBt.width(), self.moveBt.height()))# 起始位置
        rect = self.lineEdit.text().split(' ')
        print(rect)
        # 参数
        """
        改变位置, 大小:     QRect(x, y, width, height)
        改变位置:           QPoint(x, y)
        改变大小:           QSize(width, height)
        """
        # self.posAni.setEndValue(QRect(int(rect[0]), int(rect[1]), int(rect[2]), int(rect[3])))# 结束位置
        self.posAni.setEndValue(QSize(int(rect[0]), int(rect[1])))
        self.posAni.setEasingCurve(QEasingCurve.Type.InOutBack)
        self.posAni.start() # 开始动画
        self.posAni.finished.connect(lambda: print('Animation Finished!')) # 动画结束信号


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())