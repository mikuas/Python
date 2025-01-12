# encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QGraphicsOpacityEffect, QPushButton
from PySide6.QtGui import QColor, QPalette
from PySide6.QtCore import QPropertyAnimation, QPoint, Qt, QEasingCurve, QSize, QRect
from qfluentwidgets import PrimaryPushButton, LineEdit, PushButton
from FluentWidgets import VerticalScrollWidget


class Window(VerticalScrollWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.resize(800, 500)
        self.opacity = 1.0
        self.color = QColor('skyblue')

        self.moveBt = QPushButton('Move', self)
        self.moveBt.setGeometry(self.width() // 2 - 50, 50, 100, 50)

        # 获取按钮调色板
        self.palette = self.moveBt.palette()

        self.lineEdit = LineEdit(self)
        self.lineEdit.setPlaceholderText('输入颜色')
        self.lineEdit.raise_()
        self.button = PrimaryPushButton("点击我改变上面按钮的按钮", self)
        self.vBoxLayout.addWidgets([self.lineEdit, self.button], alignment=Qt.AlignmentFlag.AlignBottom)

        self.connectSignalSlot()

    def updatePalette(self, value):
        self.palette.setColor(QPalette.Button, value)
        self.moveBt.setPalette(self.palette)

    def connectSignalSlot(self):
        self.lineEdit.textChanged.connect(lambda text: print(text.split(' ')))
        self.button.clicked.connect(self.createColorAni)

    
    def createColorAni(self):
        """ ERROR """
        self.posAni = QPropertyAnimation(self.moveBt, b'color') # 动画类型
        self.posAni.setDuration(1000) # 持续事件
        self.posAni.setStartValue(self.color) # 起始位置
        self.color = QColor(self.lineEdit.text())
        self.posAni.setEndValue(self.color) # 结束位置
        self.posAni.valueChanged.connect(lambda value: self.updatePalette(value))
        self.posAni.start() # 开始动画
        self.posAni.finished.connect(lambda: print('Animation Finished!')) # 动画结束信号


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())