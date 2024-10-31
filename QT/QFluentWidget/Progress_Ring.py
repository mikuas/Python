import sys

from PySide6.QtCore import Qt, QEasingCurve, QTimer
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QApplication, QVBoxLayout
from qfluentwidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        '''进度环'''
        hLayout = QHBoxLayout(self)
        layout = QVBoxLayout()
        hLayout.addLayout(layout)
        self.ring = ProgressRing(self, useAni=True)

        # 设置范围 当前值
        self.ring.setRange(0, 100)
        self.ring.setValue(20)

        # 显示进度环文本
        self.ring.setTextVisible(True)
        # 调整大小
        self.ring.setFixedSize(80, 80)
        # 调整厚度
        self.ring.setStrokeWidth(4)

        # 调整文本格式,比如温度
        # self.ring.setFormat("%v℃")

        self.ring.isPaused()
        self.ring.resume()

        time = QTimer(self)
        time.timeout.connect(self.updateRing)
        time.start(1000)

        layout.addWidget(self.ring)

        # 不确定进进度环
        ipr = IndeterminateProgressRing()
        layout.addWidget(ipr)

        bt = TransparentToolButton(FluentIcon.PAUSE_BOLD, self)
        bt.clicked.connect(lambda : (self.ring.pause(), time.stop()) if not self.ring.isPaused() else (self.ring.resume(), time.start(1000)))
        layout.addWidget(bt)

    def updateRing(self):
        print(self.ring.value())
        self.ring.setValue(self.ring.getVal() + 1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
