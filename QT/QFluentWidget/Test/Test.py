import time
from tkinter.ttk import Label

from PySide6.QtGui import QColor, QFont, Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel
from prettytable.colortable import Theme
from pyperclip import paste
from pywin.debugger import close
from qfluentwidgets import SettingCardGroup, OptionsSettingCard, FluentIcon, ConfigItem, OptionsConfigItem, \
    OptionsValidator, ExpandGroupSettingCard, PushSettingCard, ColorDialog, PrimaryPushSettingCard, ColorSettingCard, \
    CustomColorSettingCard, ColorConfigItem, setThemeColor, themeColor, RangeSettingCard, RangeValidator, \
    RangeConfigItem, SwitchSettingCard, HyperlinkCard, SingleDirectionScrollArea, ScrollArea, SmoothScrollArea, \
    ExpandLayout

from PyMyMethod.Method import SystemCtl


class SettingWidget(ScrollArea):
    def __init__(self, text, themeMode, parent):
        super().__init__()
        self.parent = parent
        self.scrollWidget = QWidget()
        self.expandLayout = ExpandLayout(self.scrollWidget)

        # 主组
        # self.MainGroup = SettingCardGroup("设置", self.scrollWidget)
        # self.MainGroup.titleLabel.setFont(QFont('', 40))
        self.setLabel = QLabel("设置", self)
        # 样式组
        self.styleGroup = SettingCardGroup("个性化", self.scrollWidget)
        # 系统设置组
        self.sysGroup = SettingCardGroup('系统设置', self.scrollWidget)
        # 关于组
        self.aboutGroup = SettingCardGroup("关于", self.scrollWidget)

        self.yumCard = SwitchSettingCard(
            FluentIcon.TRANSPARENT,
            "云母效果",
            '窗口和表面显示半透明'
        )
        self.themeCard = OptionsSettingCard(
            themeMode,
            FluentIcon.BRUSH,
            "应用主题",
            "调整你的应用外观",
            ['浅色', '深色', '跟随系统']
        )
        # ---------------------
        cfItem = ColorConfigItem("Color", 'setColor', themeColor())
        self.colorPushCard = CustomColorSettingCard(
            cfItem,
            FluentIcon.PALETTE,
            "主题色",
            "设置应用主题颜色",
        )
        self.colorPushCard.chooseColorButton.setText("选择")
        # --------------------
        self.audioCard = RangeSettingCard(
            RangeConfigItem('Audio', 'SetAudio', SystemCtl().getAudioEndpointVolume()[1] * 100, RangeValidator(0, 100)),
            FluentIcon.VOLUME,
            "设置音量",
            '设置当前音量'
        )

        self.helpCard = HyperlinkCard(
            "https://www.github.com",
            "打开帮助页面",
            FluentIcon.HELP,
            "帮助",
            "发现新功能并了解有关QT的使用"
        )

        self.puCard = PrimaryPushSettingCard(
            "提供反馈",
            FluentIcon.FEEDBACK,
            "提供反馈",
            "通过反馈帮助我们改进"
        )

        self.mnyCard = PrimaryPushSettingCard(
            '点击有惊喜',
            FluentIcon.QRCODE,
            "资助",
            'Give Me Money'
        )

        self.initGroup()
        self.connectSignalSlots()
        self.setObjectName(text.replace(' ', '_'))

    def connectSignalSlots(self):
        # 连接信号插槽
        self.yumCard.setChecked(True)
        self.yumCard.checkedChanged.connect(lambda b: self.parent.setMicaEffectEnabled(b))

        self.colorPushCard.colorChanged.connect(lambda color: (print(color), setThemeColor(color)))

        self.audioCard.valueChanged.connect(lambda value: SystemCtl().setAudio(value / 100))

    def initGroup(self):
        self.styleGroup.addSettingCard(self.yumCard)
        self.styleGroup.addSettingCard(self.themeCard)
        self.styleGroup.addSettingCard(self.colorPushCard)

        self.sysGroup.addSettingCard(self.audioCard)

        self.aboutGroup.addSettingCard(self.helpCard)
        self.aboutGroup.addSettingCard(self.puCard)
        self.aboutGroup.addSettingCard(self.mnyCard)

        self.MainGroup.addSettingCard(self.styleGroup)
        self.MainGroup.addSettingCard(self.sysGroup)
        self.MainGroup.addSettingCard(self.aboutGroup)

        self.expandLayout.setSpacing(28)
        self.expandLayout.setContentsMargins(60, 10, 60, 0)
        self.expandLayout.addWidget(self.MainGroup)

    def getThemeCard(self):
        return self.themeCard

    def resizeEvent(self, event):
        pass