# encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QGraphicsOpacityEffect, QPushButton
from PySide6.QtGui import QColor, QPalette
from PySide6.QtCore import QPropertyAnimation, QPoint, Qt, QEasingCurve, QSize, QRect, QParallelAnimationGroup, QSequentialAnimationGroup
from qfluentwidgets import PrimaryPushButton, LineEdit, PushButton
from FluentWidgets import VerticalScrollWidget


class Window(VerticalScrollWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.resize(800, 500)
        self.opacity = 1.0
        self.color = QColor('skyblue')

        self.bt1 = PrimaryPushButton("Move", self)
        self.bt1.move(50, 50)

        self.bt2 = PrimaryPushButton("Move", self)
        self.bt2.move(50, 100)

        self.lineEdit = LineEdit(self)
        self.lineEdit.setPlaceholderText('输入x, y, x, y 用空格隔开')
        self.lineEdit.raise_()
        self.button = PrimaryPushButton("移动", self)
        self.vBoxLayout.addWidgets([self.lineEdit, self.button], alignment=Qt.AlignmentFlag.AlignBottom)

        self.connectSignalSlot()

    def connectSignalSlot(self):
        self.lineEdit.textChanged.connect(lambda text: print(text.split(' ')))
        self.button.clicked.connect(self.createColorAni)

    def createColorAni(self):
        """ ERROR """
        posAni1 = QPropertyAnimation(self.bt1, b"pos")
        posAni1.setDuration(1000)
        posAni1.setStartValue(self.bt1.pos())
        position = self.lineEdit.text().split(' ')
        posAni1.setEndValue(QPoint(int(position[0]), int(position[1])))

        posAni2 = QPropertyAnimation(self.bt2, b"pos")
        posAni2.setDuration(1000)
        posAni2.setStartValue(self.bt2.pos())
        posAni2.setEndValue(QPoint(int(position[2]), int(position[3])))

        # 并行动画组
        animationGroup = QSequentialAnimationGroup(self)
        animationGroup.addAnimation(posAni1)
        animationGroup.addAnimation(posAni2)

        posAni1.finished.connect(lambda: print('ani1 end'))
        posAni2.finished.connect(lambda: print('ani2 end'))

        animationGroup.start()
        animationGroup.finished.connect(lambda: print("Animation finished"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())