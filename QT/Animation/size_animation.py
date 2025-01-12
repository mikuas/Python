# encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QPropertyAnimation, QPoint, Qt, QEasingCurve, QSize
from qfluentwidgets import PrimaryPushButton, LineEdit
from FluentWidgets import VerticalScrollWidget


class Window(VerticalScrollWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.resize(800, 500)

        self.moveBt = PrimaryPushButton('Move', self)
        self.moveBt.move(self.width() // 2 - 50, 50)

        self.lineEdit = LineEdit(self)
        self.lineEdit.setPlaceholderText('输入最终大小, 用空格隔开')
        self.button = PrimaryPushButton("点击我改变上面按钮的按钮", self)
        self.vBoxLayout.addWidgets([self.lineEdit, self.button], alignment=Qt.AlignmentFlag.AlignBottom)

        self.connectSignalSlot()

    def connectSignalSlot(self):
        self.lineEdit.textChanged.connect(lambda text: print(text.split(' ')))
        self.button.clicked.connect(self.createSizeAni)

    
    def createSizeAni(self):
        self.posAni = QPropertyAnimation(self.moveBt, b'size') # 动画类型
        self.posAni.setDuration(1000) # 持续事件
        self.posAni.setStartValue(self.moveBt.size()) # 起始位置
        size = self.lineEdit.text().split(' ')
        print(size)
        self.posAni.setEasingCurve(QEasingCurve.Type.OutBack)
        self.posAni.setEndValue(QSize(int(size[0]), int(size[1])))# 结束位置
        self.posAni.start() # 开始动画
        self.posAni.finished.connect(lambda: print('Animation Finished!')) # 动画结束信号

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())