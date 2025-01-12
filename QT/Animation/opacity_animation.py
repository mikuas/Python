# encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QGraphicsOpacityEffect
from PySide6.QtCore import QPropertyAnimation, QPoint, Qt, QEasingCurve, QSize, QRect
from qfluentwidgets import PrimaryPushButton, LineEdit
from FluentWidgets import VerticalScrollWidget


class Window(VerticalScrollWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.resize(800, 500)
        self.opacity = 1.0

        self.moveBt = PrimaryPushButton('Move', self)
        self.moveBt.move(self.width() // 2 - 50, 50)

        self.lineEdit = LineEdit(self)
        self.lineEdit.setPlaceholderText('输入透明度(0-1)')
        self.lineEdit.raise_()
        self.button = PrimaryPushButton("点击我改变上面按钮的按钮", self)
        self.vBoxLayout.addWidgets([self.lineEdit, self.button], alignment=Qt.AlignmentFlag.AlignBottom)

        self.connectSignalSlot()

        # 创建透明度效果
        self.opacityEffect = QGraphicsOpacityEffect(self.moveBt)
        self.moveBt.setGraphicsEffect(self.opacityEffect)
        self.opacityEffect.setOpacity(self.opacity)


    def connectSignalSlot(self):
        self.lineEdit.textChanged.connect(lambda text: print(text.split(' ')))
        self.button.clicked.connect(self.createOpacityAni)

    
    def createOpacityAni(self):
        self.posAni = QPropertyAnimation(self.opacityEffect, b'opacity') # 动画类型
        self.posAni.setDuration(1000) # 持续事件
        self.posAni.setStartValue(self.opacity) # 起始位置
        self.opacity = float(self.lineEdit.text())
        self.posAni.setEndValue(self.opacity) # 结束位置
        self.posAni.setEasingCurve(QEasingCurve.Type.InOutBack)
        self.posAni.start() # 开始动画
        self.posAni.finished.connect(lambda: print('Animation Finished!')) # 动画结束信号


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())