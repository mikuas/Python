import sys
from symtable import Function

from PySide6.QtCore import QSize, QUrl, QDate
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget
from PySide6.QtGui import Qt
from qfluentwidgets import *
from qfluentwidgets.multimedia import VideoWidget


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 450)
        centerWindget = QWidget(self)
        mainLayout = QVBoxLayout(centerWindget)

        '''视频播放器'''
        video = VideoWidget(self)
        video.setVideo((QUrl.fromLocalFile(r"C:\Users\Administrator\Downloads\Bili_Download\【补档】素颜-如果再肘你一遍是否还会有感觉-BV1vy411i7ai.mp4")))

        button = PushButton("Start")
        button.clicked.connect(video.play)
        mainLayout.addWidget(video)
        mainLayout.addWidget(button)
        self.setCentralWidget(centerWindget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())