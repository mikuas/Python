import sys
from symtable import Function

from PySide6.QtCore import QSize, QUrl, QEasingCurve
from PySide6.QtWidgets import QPushButton, QMainWindow, QApplication, QVBoxLayout, QWidget
from PySide6.QtGui import Qt
from qfluentwidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        '''流式布局'''
        layout = FlowLayout(self, needAni=True)  # 启用动画

        # 自定义动画参数
        layout.setAnimation(250, QEasingCurve.OutQuad)

        layout.setContentsMargins(30, 30, 30, 30)
        layout.setVerticalSpacing(20)
        layout.setHorizontalSpacing(10)

        self.button1 = PushButton('aiko')
        self.button2 = PushButton('刘静爱')
        self.button3 = PushButton('柳井爱子')
        self.button4 = PushButton('aiko 赛高')
        self.button5 = PushButton('aiko 太爱啦😘')

        # self.button1.setFixedWidth(self.width() * 0.8)
        # self.button2.setFixedWidth(self.width() * 0.8)
        # self.button3.setFixedWidth(self.width() * 0.8)
        # self.button4.setFixedWidth(self.width() * 0.8)
        # self.button5.setFixedWidth(self.width() * 0.8)

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)

        self.resize(250, 300)

    # def resizeEvent(self, event):
    #     w = self.width() * 0.8
    #     self.button1.setFixedWidth(w)
    #     self.button2.setFixedWidth(w)
    #     self.button3.setFixedWidth(w)
    #     self.button4.setFixedWidth(w)
    #     self.button5.setFixedWidth(w)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())