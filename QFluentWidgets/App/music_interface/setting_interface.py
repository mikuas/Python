import json

from FluentWidgets import VerticalScrollWidget, FolderListCard, ColorSelectCard, SwitchButtonCard, ComboBoxCard
from PySide6.QtGui import Qt
from qfluentwidgets import SettingCardGroup, FluentIcon, InfoBar, InfoBarPosition


class SettingInterface(VerticalScrollWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setObjectName(text.replace(" ", "_"))
        self.vBoxLayout.setContentsMargins(20, 50, 20, 0)
        with open('./config/path.json', 'r') as f:
            self.path = json.load(f)["folderPath"]
        self.folderCardGroup = SettingCardGroup("路径", self)
        self.styleCardGroup = SettingCardGroup("系统样式", self)
        self.sysSetCardGroup = SettingCardGroup('系统设置', self)

        self.initCard()
        self.initCardGroup()
        self.initLayout()
        self.connectSignalSlots()

    @staticmethod
    def updatePath(path):
        with open('./config/path.json', 'w', encoding='utf-8') as f:
            json.dump({"folderPath": path}, f, indent=4)

    def initLayout(self):
        self.vBoxLayout.addWidgets([
            self.folderCardGroup,
            self.styleCardGroup,
            self.sysSetCardGroup
        ], alignment=Qt.AlignmentFlag.AlignTop)

    def initCardGroup(self):
        self.folderCardGroup.addSettingCards([
            self.folder,
            self.pathCard
        ])
        self.styleCardGroup.addSettingCards([
            self.micaEffectCard,
            self.themeColorCard
        ])
        self.sysSetCardGroup.addSettingCards([
            self.sysTrayCard
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
        self.micaEffectCard = SwitchButtonCard(
            FluentIcon.TRANSPARENT,
            '云母效果',
            '窗口和表面显示半透明',
            True,
            self
        )
        self.themeColorCard = ColorSelectCard(
            "主题色",
            '设置主题颜色',
            self,
            FluentIcon.PALETTE
        )
        self.sysTrayCard = ComboBoxCard(
            FluentIcon.DEVELOPER_TOOLS,
            "系统托盘",
            "设置是否最小化到系统托盘",
            ['最小化到系统托盘', '退出程序'],
            parent=self
        )
        # self.themeCard = OptionsSettingCard(
        #     qconfig.themeMode,
        #     FluentIcon.BRUSH,
        #     "应用主题色",
        #     "调整你的主题外观",
        #     ["浅色", '深色', '跟随系统设置'],
        #     self.parent
        # )

    def connectSignalSlots(self):
        self.folder.folderChanged.connect(
            lambda folder: (
                self.pathCard.comboBoxButton.clear(),
                self.pathCard.comboBoxButton.addItems([self.path] + folder)
            )
        )
        self.pathCard.comboBoxButton.currentTextChanged.connect(
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
        self.micaEffectCard.button.checkedChanged.connect(
            lambda b: self.parent.setMicaEffectEnabled(b)
        )
        self.sysTrayCard.comboBoxButton.currentTextChanged.connect(
            lambda: self.setTray(self.sysTrayCard.comboBoxButton.currentIndex())
        )

    def setTray(self, index):
        self.parent.closeEvent = None if index == 1 else self.closeEvent

    def closeEvent(self, event):
        super().closeEvent(event)
        event.ignore()
        self.parent.hide()