import json
import os
import random

from FluentWidgets import ListWidget
from PySide6.QtCore import QSize, QUrl
from PySide6.QtGui import Qt, QColor
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtWidgets import QWidget
from qfluentwidgets import TitleLabel, TransparentToolButton, FluentIcon, BodyLabel, TransparentToggleToolButton
from qfluentwidgets.multimedia import StandardMediaPlayBar

from FluentWidgets import VBoxLayout, setToolTipInfos


class MusicListWidget(QWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent)
        self.label = TitleLabel('音乐列表', self)
        self.setObjectName(text.replace(" ", "_"))
        self.vLayout = VBoxLayout(self)
        self.list = ListWidget()
        self.media = StandardMediaPlayBar(self)
        with open('./config/path.json', 'r', encoding='utf-8') as f:
            jsonData = json.load(f)
        self.path = jsonData['folderPath']
        music, img = self.getMusicData(self.path)
        self.items = self.list.addIconItem(
            img,
            [m.split('\\')[-1].split('.')[0] for m in music],
            64
        )
        self.list.setIconSize(QSize(40, 40))
        self.list.setSelectRightClickedRow(True)
        self.list.setCurrentItem(self.items[0])

        self.initLayout()
        self.initMedia()
        self.setTip()
        self.connectSignals()

    def initMedia(self):
        self.titleLabel = BodyLabel("暂无歌曲信息", self)
        self.titleLabel.setTextColor(QColor(0, 191, 255), QColor(255, 0, 255))
        self.previousButton = TransparentToolButton(FluentIcon.CARE_LEFT_SOLID, self)
        self.nextButton = TransparentToolButton(FluentIcon.CARE_RIGHT_SOLID, self)
        self.randomButton = TransparentToggleToolButton(FluentIcon.SYNC, self)
        self.media.centerButtonLayout.insertWidget(0, self.previousButton)
        self.media.centerButtonLayout.insertWidget(0, self.randomButton)
        self.media.centerButtonLayout.insertWidget(-1, self.nextButton)
        self.media.rightButtonLayout.addWidget(self.media.volumeButton)
        self.media.leftButtonLayout.addWidget(self.titleLabel)

    def setTip(self):
        setToolTipInfos(
            [self.previousButton, self.nextButton, self.randomButton, self.media.volumeButton],
            ["上一首", '下一首', '随机播放', '音量'],
            3000
        )

    def initLayout(self):
        self.vLayout.addWidgets_(
            [self.label, self.list, self.media],
            alignment=[Qt.AlignmentFlag.AlignTop, Qt.AlignmentFlag.AlignVCenter, Qt.AlignmentFlag.AlignBottom]
        )

    def connectSignals(self):
        self.list.itemClicked.connect(lambda value: self.play(f"{self.path}\\{value.text()}\\{value.text()}"))
        self.media.player.mediaStatusChanged.connect(lambda status: self.endPlay(status))
        self.previousButton.clicked.connect(lambda: self.updatePlay(-1))
        self.nextButton.clicked.connect(lambda: self.updatePlay(1))

    def play(self, path: str):
        path = f"{path}.flac" if os.path.exists(f"{path}.flac") else f"{path}.mp3"
        self.titleLabel.setText(self.list.currentItem().text())
        self.media.player.setSource(QUrl.fromLocalFile(path))
        self.media.player.play()

    def endPlay(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.updatePlay(1)

    def updatePlay(self, index):
        if self.randomButton.isChecked():
            self.list.setCurrentItem(self.items[random.randint(0, len(self.items) - 1)])
        try:
            self.list.setCurrentItem(self.items[self.findIndex(self.list.currentItem(), self.items) + index])
        except IndexError:
            self.list.setCurrentItem(self.items[0])
        item = self.list.currentItem()
        self.play(f"{self.path}\\{item.text()}\\{item.text()}")

    @staticmethod
    def findIndex(value, item):
        for i in range(len(item)):
            if item[i] == value:
                return i

    @staticmethod
    def getMusicData(path: str):
        musicPath = []
        imagePath = []
        files = os.listdir(path)
        for file in files:
            _path = f"{path}\\{file}"
            try:
                for item in os.listdir(_path):
                    suffix = item.split('.')[-1]
                    print(suffix)
                    if suffix in ['jpg', 'png']:
                        imagePath.append(f"{_path}\\{item}")
                        # print(f"图片路径: {_path}\\{item}")
                    elif suffix in ['mp3', 'flac', 'ogg']:
                        musicPath.append(f"{_path}\\{item}")
                        # print(f"音乐路径: {_path}\\{item}")
            except Exception:
                continue
        return musicPath, imagePath

