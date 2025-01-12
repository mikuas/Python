# encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QPropertyAnimation, QPoint, Qt, QEasingCurve
from qfluentwidgets import PrimaryPushButton, LineEdit
from FluentWidgets import VerticalScrollWidget


class Window(VerticalScrollWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.resize(800, 500)

        self.moveBt = PrimaryPushButton('Move', self)
        self.moveBt.setFixedSize(100, 50)

        self.lineEdit = LineEdit(self)
        self.lineEdit.setPlaceholderText('输入移动的位置(x, y), 用逗号隔开')
        self.button = PrimaryPushButton("点击我移动上面的按钮", self)
        self.vBoxLayout.addWidgets([self.lineEdit, self.button], alignment=Qt.AlignmentFlag.AlignBottom)

        self.connectSignalSlot()

    def connectSignalSlot(self):
        self.lineEdit.textChanged.connect(lambda text: print(text.split(',')))
        self.button.clicked.connect(self.createPosAni)

    
    def createPosAni(self):
        self.posAni = QPropertyAnimation(self.moveBt, b'pos') # 动画类型
        self.posAni.setDuration(1000) # 持续事件
        self.posAni.setStartValue(self.moveBt.pos()) # 起始位置
        position = self.lineEdit.text().split(',')
        self.posAni.setEndValue(QPoint(int(position[0]), int(position[1]))) # 结束位置
        self.posAni.setEasingCurve(QEasingCurve.Type.InOutBack) # 动画曲线
        self.posAni.start() # 开始动画
        self.posAni.finished.connect(lambda: print('Animation Finished!')) # 动画结束信号


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())