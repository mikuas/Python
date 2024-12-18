import json
import os
import random

from PySide6.QtCore import QUrl
from PySide6.QtGui import QColor
from PySide6.QtMultimedia import QMediaPlayer
from qfluentwidgets import TransparentToolButton, FluentIcon, BodyLabel, TransparentToggleToolButton
from qfluentwidgets.multimedia import StandardMediaPlayBar

from FluentWidgets import VBoxLayout, setToolTipInfos, TableWidget

from QtFluentWidgets.demo.demo15 import MusicListWidget, MusicWidget


class MusicListInterface(MusicListWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent)
        self.setObjectName(text.replace(" ", "_"))
        self.vLayout = VBoxLayout(self)
        self.media = StandardMediaPlayBar(self)

        with open('./config/path.json', 'r', encoding='utf-8') as f:
            self.path = json.load(f)['folderPath']
        music, img = self.getMusicData(self.path)
        music = [temp.split('\\')[-1].split('.')[0] for temp in music]

        self.table = TableWidget(self)
        self.table.verticalHeader().hide()
        self.table.horizontalHeader().hide()
        self.table.setItemMinHeight(58)

        self.items = [[MusicWidget(i, t)] for t, i in zip(music, img)]
        self.table.addTabWidget(self.items)

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
        # self.vLayout.addWidget(self.media)
        self.vBoxLayout.addWidget(self.table)

    def connectSignals(self):
        # self.list.itemClicked.connect(lambda value: self.play(f"{self.path}\\{value.text()}\\{value.text()}"))
        self.media.player.mediaStatusChanged.connect(lambda status: self.endPlay(status))
        self.previousButton.clicked.connect(lambda: self.updatePlay(-1))
        self.nextButton.clicked.connect(lambda: self.updatePlay(1))

        self.table.cellClicked.connect(
            lambda c, r: print(self.getText(self.table.cellWidget(c, r)))
        )

        for item, row in zip(self.items, [i for i in range(len(self.items))]):
            for i in item:
                i.playButton.clicked.connect(
                    lambda: (
                        print(i),
                        self.table.selectRow(row)
                    )
                )

    def play(self, path: str):
        path = f"{path}.flac" if os.path.exists(f"{path}.flac") else f"{path}.mp3"
        # self.titleLabel.setText(self.list.currentItem().text())
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
        except Exception:
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

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.table.setItemMinWidth(self.table.width() - 5)

    def contextMenuEvent(self, event):
        super().contextMenuEvent(event)
        self.menu.exec(event.globalPos())