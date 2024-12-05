import json

from FluentWidgets import VerticalScrollWidget, FolderListCard
from PySide6.QtGui import Qt
from qfluentwidgets import SettingCardGroup, FluentIcon, Flyout, InfoBar, InfoBarPosition

from FluentWidgets import ComboBoxCard


class SettingInterface(VerticalScrollWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent)
        self.setObjectName(text.replace(" ", "_"))
        self.vLayout.setContentsMargins(20, 50, 20, 0)
        with open('./config/path.json', 'r') as f:
            self.path = json.load(f)["folderPath"]
        self.folderCardGroup = SettingCardGroup("路径", self)

        self.initCard()
        self.initCardGroup()
        self.initLayout()

        self.folder.folderChanged.connect(
            lambda folder: (
                self.pathCard.comboBox.clear(),
                self.pathCard.comboBox.addItems([self.path] + folder)
            )
        )
        self.pathCard.comboBox.currentTextChanged.connect(
            lambda path: (
                self.updatePath(path),
                InfoBar.success(
                    '重启程序后生效',
                    '',
                    isClosable=False,
                    duration=3000,
                    position=InfoBarPosition.TOP,
                    parent=self
                ).show()
            )
        )

    @staticmethod
    def updatePath(path):
        with open('./config/path.json', 'w', encoding='utf-8') as f:
            json.dump({"folderPath": path}, f, indent=4)

    def initLayout(self):
        self.vLayout.addWidgets([
            self.folderCardGroup,
        ], alignment=Qt.AlignmentFlag.AlignTop)

    def initCardGroup(self):
        self.folderCardGroup.addSettingCards([
            self.folder,
            self.pathCard
        ])

    def initCard(self):
        self.folder = FolderListCard(
            "音乐文件夹",
            "添加要播放的音乐文件夹",
            '',
            self
        )
        self.pathCard = ComboBoxCard(
            FluentIcon.MUSIC,
            '选择音乐文件夹',
            '选择要播放音乐的文件夹',
            [self.path]
        )