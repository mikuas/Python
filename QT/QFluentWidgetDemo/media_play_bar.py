import sys
from symtable import Function

from PySide6.QtCore import QSize, QUrl, QDate
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget
from PySide6.QtGui import Qt
from qfluentwidgets import *
from qfluentwidgets.multimedia import SimpleMediaPlayBar, MediaPlayBarButton, StandardMediaPlayBar


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 450)
        centerWindget = QWidget(self)
        mainLayout = QVBoxLayout(centerWindget)

        '''媒体'''
        # player = SimpleMediaPlayBar()
        # # 添加按钮
        # player.hBoxLayout.addWidget(MediaPlayBarButton(FluentIcon.FULL_SCREEN))
        #
        # # 在线音乐
        # url = QUrl("https://files.cnblogs.com/files/blogs/677826/beat.zip?t=1693900324")
        # player.player.setSource(url)
        '''
        调用下述方法可以改变播放状态：

        pause()：暂停播放
        play()：继续播放
        stop()：结束播放
        togglePlayState()：开始 / 暂停播放
        setPosition()：设置播放进度
        setVolume()：设置音量
        '''
        # 本地音乐
        # url = QUrl.fromLocalFile(str(Path("resource/aiko - beat.flac").absolute()))
        # player.player.setSource(url)

        # 包含前进后退
        bar = StandardMediaPlayBar()
        # bar.player.setSource(url)

        # bar.rightButtonLayout.addLayout()


        # mainLayout.addWidget(player)
        mainLayout.addWidget(bar)
        self.setCentralWidget(centerWindget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())