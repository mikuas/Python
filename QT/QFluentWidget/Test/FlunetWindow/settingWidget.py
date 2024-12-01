import sys

from PySide6.QtCore import QTimer
from PySide6.QtGui import QFont, Qt
from PySide6.QtWidgets import QWidget, QLabel, QApplication
from qfluentwidgets import SettingCardGroup, OptionsSettingCard, FluentIcon, PrimaryPushSettingCard, \
    CustomColorSettingCard, ColorConfigItem, setThemeColor, themeColor, RangeSettingCard, RangeValidator, \
    RangeConfigItem, SwitchSettingCard, HyperlinkCard, ScrollArea, ExpandLayout, Flyout, FlyoutAnimationType, \
    ExpandGroupSettingCard, ConfigItem, BoolValidator, InfoBar, InfoBarPosition, OptionsValidator, ComboBoxSettingCard, \
    OptionsConfigItem, qconfig, Theme, setTheme

from PyMyMethod import SystemCtl, FileControl
from qfluentwidgets.components.material import AcrylicComboBoxSettingCard


class SettingWidget(ScrollArea):
    def __init__(self, text, themeMode, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.scrollWidget = QWidget()
        self.expandLayout = ExpandLayout(self.scrollWidget)
        # self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setViewportMargins(20, 55, 20, 20)
        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)

        self.setLabel = QLabel("设置", self)
        self.setLabel.setFont(QFont('', 40))

        # 样式组
        self.styleGroup = SettingCardGroup("个性化", self.scrollWidget)
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
        cfItem = ColorConfigItem("Color", 'setColor', themeColor())
        self.colorPushCard = CustomColorSettingCard(
            cfItem,
            FluentIcon.PALETTE,
            "主题色",
            "设置应用主题颜色",
        )
        self.colorPushCard.chooseColorButton.setText("选择")
        self.colorPushCard.defaultRadioButton.setText("默认颜色")
        self.colorPushCard.customRadioButton.setText("自定义颜色")
        self.colorPushCard.choiceLabel.setText("默认颜色")
        self.colorPushCard.customLabel.setText("选择颜色")
        # --------------------------------------------------------------------------------------------
        # 系统设置组
        self.sysGroup = SettingCardGroup('系统设置', self.scrollWidget)
        self.audioCard = RangeSettingCard(
            RangeConfigItem('Audio', 'SetAudio', int(SystemCtl().getAudioEndpointVolume()[1] * 100 + 0.1), RangeValidator(0, 100)),
            FluentIcon.VOLUME,
            "设置音量",
            '设置当前音量'
        )
        self.flyCard = SwitchSettingCard(
            FluentIcon.AIRPLANE,
            "飞行模式",
            "开启飞行模式电脑会飞走哦🙃",
            ConfigItem(
                "Button",
                'FlyButton',
                False,
                BoolValidator()
            )
        )
        self.flyCard.switchButton.setText('关')
        self.powerCard = ExpandGroupSettingCard(
            FluentIcon.SPEED_OFF,
            "省电模式",
            "调整电源选项",
        )
        self.cItem = OptionsConfigItem("Power", 'Down', '无', OptionsValidator(['无', '关机', '重启', '锁定', '注销']))
        self.subCard = ComboBoxSettingCard(
            self.cItem,
            FluentIcon.POWER_BUTTON,
            "电源选项",
            '选着模式',
            ['无', '关机', '重启', '锁定', '注销']
        )
        self.powerCard.addGroupWidget(self.subCard)
        self.tItem = OptionsConfigItem("Tray", 'Tray', '最小化到系统托盘', OptionsValidator(['关闭窗口退出程序', '最小化到系统托盘']))
        self.trayCard = AcrylicComboBoxSettingCard(
            self.tItem,
            FluentIcon.INFO,
            "系统托盘",
            '关闭出口是否退出程序',
            texts=['关闭窗口退出程序', '最小化到系统托盘']
        )
        # --------------------------------------------------------------------------------------------
        # 关于组
        self.aboutGroup = SettingCardGroup("关于", self.scrollWidget)
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

        # self.initStyle()
        self.initGroup()
        # self.connectSignalSlots()
        self.setObjectName(text.replace(' ', '_'))

    def connectSignalSlots(self):
        td = {'Theme.DARK': '深', "Theme.LIGHT": "浅", "Theme.AUTO": '跟随系统'}
        # 连接信号插槽
        self.yumCard.setChecked(True)
        self.yumCard.switchButton.setText('开')
        self.yumCard.checkedChanged.connect(
            lambda b: (
                self.parent.setMicaEffectEnabled(b),
                self.yumCard.switchButton.setText('开') if b else self.yumCard.switchButton.setText('关')
            )
        )
        self.themeCard.optionChanged.connect(
            lambda theme:
            InfoBar.success(
                "主题",
                f'成功设置为{td[str(theme.value)]}色主题',
                duration=2500,
                parent=self
            )
        )
        self.colorPushCard.colorChanged.connect(lambda color: (setThemeColor(color)))

        qconfig.themeChanged.connect(lambda theme: self.applyStyle(theme))
        self.themeCard.optionChanged.connect(
            lambda theme: setTheme(theme.value)
        )

        self.tItem.valueChanged.connect(lambda value: self.updateCloseEvent(value))
        self.audioCard.valueChanged.connect(lambda value: SystemCtl().setAudio(value / 100))
        self.flyCard.checkedChanged.connect(
            lambda b: (
                self.showWaringInfo('✈️飞机模式已开启,你的电脑马上就要飞走了喵~~') if b else self.showWaringInfo('✈️飞机模式关闭,你的电脑不会飞走了喵~~'),
                self.flyCard.switchButton.setText('开') if b else self.flyCard.switchButton.setText('关')
            )
        )
        self.cItem.valueChanged.connect(lambda value: self.showErrorInfo(f'你的电脑还有10秒就{value}了喵~~😱', 10000, value))

        self.puCard.clicked.connect(
            lambda:
            InfoBar.warning(
                "SB",
                "就凭你也配让我改进, 啊~ 🤡👎👎🙌",
                position=InfoBarPosition.TOP_RIGHT,
                duration=5000,
                parent=self
            )
        )
        self.mnyCard.clicked.connect(
            lambda:
            Flyout.create(
                "Mikuas",
                "资助一下好不好喵~~😘🥰",
                image='./data/images/icon/money.jpg',
                isClosable=False,
                target=self.mnyCard,
                aniType=FlyoutAnimationType.PULL_UP
            )
        )

    def initGroup(self):
        self.styleGroup.addSettingCard(self.yumCard)
        self.styleGroup.addSettingCard(self.themeCard)
        self.styleGroup.addSettingCard(self.colorPushCard)

        self.sysGroup.addSettingCard(self.audioCard)
        self.sysGroup.addSettingCard(self.flyCard)
        self.sysGroup.addSettingCard(self.powerCard)
        self.sysGroup.addSettingCard(self.trayCard)

        self.aboutGroup.addSettingCard(self.helpCard)
        self.aboutGroup.addSettingCard(self.puCard)
        self.aboutGroup.addSettingCard(self.mnyCard)

        self.expandLayout.addWidget(self.styleGroup)
        self.expandLayout.addWidget(self.sysGroup)
        self.expandLayout.addWidget(self.aboutGroup)

        self.expandLayout.setSpacing(28)
        # self.expandLayout.setContentsMargins(0, 0, 0, 0)

    def showWaringInfo(self, content):
        InfoBar.warning(
            "飞机模式",
            content,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2500,
            parent=self
        )

    def showErrorInfo(self, content, time, value):
        t = QTimer(self)
        if value == "无":
            InfoBar.success(
                "取消",
                '这是个假的按钮,你还真的点啊🤡',
                duration=3000,
                parent=self
            )
        else:
            InfoBar.error(
                value,
                content,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=-1,
                parent=self
            )
            t.timeout.connect(lambda: (SystemCtl().systemOption(0, value), t.stop()))
            t.start(time)

    def initStyle(self, theme="LIGHT_Set"):
        self.setStyleSheet(FileControl().readQssFile(f'./data/styles/{theme}.qss'))
        print(f'SetTheme: {theme}')

    def applyStyle(self, theme):
        if theme == Theme.DARK:
            theme = 'DARK_Set'
        else:
            theme = 'LIGHT_Set'
        self.initStyle(theme)

    def updateCloseEvent(self, value):
        if value == '最小化到系统托盘':
            self.parent.closeEvent = self.closeEvent
        else:
            self.parent.closeEvent = None

    def closeEvent(self, event):
        event.ignore()
        self.parent.hide()

    def getThemeCard(self):
        return self.themeCard

    def resizeEvent(self, event):
        self.scrollWidget.resize(self.width(), self.height())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SettingWidget("SETTING", qconfig.themeMode)
    setTheme(Theme.AUTO)
    window.show()
    sys.exit(app.exec())