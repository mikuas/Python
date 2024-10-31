import time

from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QHBoxLayout, QPushButton
from PySide6.QtCore import QUrl, Qt, QSize
from PySide6.QtGui import QIcon
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget

from .fileControl import File


class VideoWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.startIcon = r'../../data/images/icon/start.png'
        self.stopIcon = r'../../data/images/icon/stop.png'

        mainLayout = QVBoxLayout(self)

        self.media = QMediaPlayer(self)
        video = QVideoWidget(self)
        video.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        video.setGeometry(self.rect())
        audio = QAudioOutput(self)
        self.media.setVideoOutput(video)
        self.media.setAudioOutput(audio)
        self.media.setSource(QUrl("../../data/videos/0.mp4"))

        buttonLayout = QHBoxLayout()
        btm = ["上一个", "播放", "下一个"]
        functions = [
            lambda: (self.unVideo(-1), self.updateBIT('暂停', self.startIcon)),
            self.updateVideoButton,
            lambda: (self.unVideo(1), self.updateBIT('暂停', self.startIcon))
        ]
        icons = [
            r'../../data/images/icon/up.png',
            r'../../data/images/icon/stop.png',
            r'../../data/images/icon/next.png'
        ]
        with open('../data/styles/Button.qss', 'r', encoding='utf-8') as f:
            style = f.read()
        for b, fc, icon in zip(btm, functions, icons):
            button = QPushButton(b)
            if b == '播放':
                self.videoButton = button
            button.setIcon(QIcon(icon))
            button.setIconSize(QSize(40, 40))
            button.setStyleSheet(style)
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            button.setFixedHeight(100)
            button.clicked.connect(fc)
            buttonLayout.addWidget(button)

        mainLayout.addWidget(video)
        mainLayout.addLayout(buttonLayout)

    def updateVideoButton(self):
        if self.videoButton.text() == '播放':
            self.updateBIT('暂停', self.startIcon)
            self.media.play()
        else:
            self.updateBIT('播放', self.stopIcon)
            self.media.pause()

    def updateBIT(self, text, icon):
        self.videoButton.setText(text)
        self.videoButton.setIcon(QIcon(icon))

    def unVideo(self, num):
        data = File.readJsonFile('../data/json/videoPath.json')
        self.media.stop()
        time.sleep(0.1)
        key = int(self.media.source().url().split('/')[-1].split('.')[-2][-1]) + num
        length = len(data)
        if key >= length:
            key = 0
        elif key < 0:
            key = str(length - 1)
        self.media.setSource(QUrl(data[str(key)]))
        print(data[str(key)])
        time.sleep(0.1)
        self.media.play()