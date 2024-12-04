import os

from FluentWidgets import VerticalScrollWidget, SwitchButtonCard, CustomColorCard
from PySide6.QtWidgets import QSystemTrayIcon
from qfluentwidgets import FluentWindow, SettingCardGroup, FluentIcon, OptionsSettingCard, qconfig

from QFluentWidgets.FluentWidgetModule.FluentWidgets import ComboBoxCard, PrimaryButtonCard


class SettingWidget(VerticalScrollWidget):
    def __init__(self, text: str, parent: FluentWindow = None):
        super().__init__(parent)
        self.parent = parent
        # self.parent.closeEvent = self.closeEvent
        self.setObjectName(text.replace(' ', '_'))
        self.styleCardGroup = SettingCardGroup("个性化", self)
        self.sysCardGroup = SettingCardGroup("系统设置", self)
        self.__initCard()
        self.__initCardGroup()
        self.__initLayout()
        self.__connectSignalSlot()

    def __initLayout(self):
        self.vLayout.addWidget(self.styleCardGroup)
        self.vLayout.addWidget(self.sysCardGroup)

    def __initCard(self):
        self.micaEffectCard = SwitchButtonCard(
            FluentIcon.TRANSPARENT,
            '云母效果',
            '窗口和表面显示半透明',
            True,
            self
        )
        self.colorCard = CustomColorCard(
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
        self.bt = PrimaryButtonCard(
            FluentIcon.MUSIC,
            '音乐',
            '下载音乐',
            '打开',
            parent=self
        )
        self.themeCard = OptionsSettingCard(
            qconfig.themeMode,
            FluentIcon.BRUSH,
            "应用主题色",
            "调整你的主题外观",
            ["浅色", '深色', '跟随系统设置'],
            self.parent
        )

    def __initCardGroup(self):
        self.styleCardGroup.addSettingCards([
            self.micaEffectCard,
            self.colorCard,
            self.themeCard
        ])
        self.sysCardGroup.addSettingCards([
            self.sysTrayCard,
            self.bt
        ])

    def __connectSignalSlot(self):
        self.micaEffectCard.button.checkedChanged.connect(lambda b: self.parent.setMicaEffectEnabled(b))
        self.sysTrayCard.comboBox.currentIndexChanged.connect(lambda index: self.setTray(index))
        self.bt.button.clicked.connect(
            lambda: os.system(r"start D:\DownloadMusic\小汪音乐.exe")
        )

    def setTray(self, index):
        self.parent.closeEvent = None if index == 1 else self.closeEvent

    def closeEvent(self, event):
        super().closeEvent(event)
        event.ignore()
        self.parent.hide()
        self.parent.systemTrayIcon.showMessage(
            "Title",
            "程序已最小化到系统托盘",
            QSystemTrayIcon.MessageIcon.Information,
            2000
        )
