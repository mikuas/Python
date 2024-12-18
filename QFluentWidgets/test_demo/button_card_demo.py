import sys

from PySide6.QtWidgets import QWidget, QApplication
from qfluentwidgets import SettingCardGroup, FluentIcon, setTheme, Theme

from QtFluentWidgets.FluentWidgetModule.FluentWidgets import (
    VerticalScrollWidget,
    ButtonCard, PrimaryButtonCard, TransparentButtonCard,
    ToolButtonCard, PrimaryToolButtonCard, TransparentToolButtonCard,
    SwitchButtonCard, CheckBoxCard, HyperLinkCard,
    DropDownCard, PrimaryDropDownCard, TransparentDropDownCard,
    DropDownToolCard, PrimaryDropDownToolCard, TransparentDropDownToolCard,
    WinFluentIcon
)


class Demo(VerticalScrollWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 650)
        self.buttonCardGroup = SettingCardGroup("按钮卡片", self)
        self.toolButtonCardGroup = SettingCardGroup("工具按钮卡片", self)
        self.otherButtonCardGroup = SettingCardGroup("其它按钮卡片", self)
        self.dropDownButtonCardGroup = SettingCardGroup("下拉按钮卡片", self)
        self.dropDownToolButtonCardGroup = SettingCardGroup("下拉工具按钮卡片", self)
        self.initCard()
        self.initGroupCard()
        self.initLayout()

    def initLayout(self):
        self.vBoxLayout.addWidgets([
            self.buttonCardGroup,
            self.toolButtonCardGroup,
            self.otherButtonCardGroup,
            self.dropDownButtonCardGroup,
            self.dropDownToolButtonCardGroup,
        ])

    def initCard(self):
        #################################
        self.buttonCard = ButtonCard(
            FluentIcon.HOME,
            'ButtonCard',
            '',
            "确定",
            parent=self
        )
        self.primaryButtonCard = PrimaryButtonCard(
            FluentIcon.SEND,
            'PrimaryButtonCard',
            '',
            "确定",
            parent=self
        )
        self.transparentButtonCard = TransparentButtonCard(
            FluentIcon.GITHUB,
            'TransparentButtonCard',
            '',
            "确定",
            parent=self
        )
        ###############################
        self.toolButtonCard = ToolButtonCard(
            FluentIcon.MORE,
            'ToolButtonCard',
            '',
            FluentIcon.SEND,
            parent=self
        )
        self.primaryToolButtonCard = PrimaryToolButtonCard(
            WinFluentIcon.WIFI,
            'PrimaryToolButtonCard',
            '',
            WinFluentIcon.MORE,
            parent=self
        )
        self.transparentToolButtonCard = TransparentToolButtonCard(
            WinFluentIcon.WIN_11_LOG,
            'TransparentToolButtonCard',
            '',
            WinFluentIcon.XIN_HAO,
            parent=self
        )
        #########################
        self.switchButtonCard = SwitchButtonCard(
            WinFluentIcon.CLOUD,
            'SwitchButtonCard',
            '',
            True,
            self
        )
        self.checkBoxCard = CheckBoxCard(
            FluentIcon.PLAY,
            'CheckBoxCard',
            '',
            True,
            '同意用户协议',
            parent=self
        )
        self.hyperLinkCard = HyperLinkCard(
            'https://www.bilibili.com',
            FluentIcon.VIDEO,
            'HyperLinkCard',
            '',
            'target bilibili',
            parent=self
        )
        #########################
        self.dropDownCard = DropDownCard(
            FluentIcon.WIFI,
            'DropDownCard',
            '',
            '更多',
            menuTexts=['item1', 'item2', 'item3'],
            menuIcons=[FluentIcon.PLAY, FluentIcon.PAUSE, FluentIcon.SEND],
            triggered=[lambda: print('itme1'), lambda: print('itme2'), lambda: print('itme3')],
            parent=self
        )
        self.primaryDropDownCard = PrimaryDropDownCard(
            FluentIcon.GITHUB,
            "PrimaryDropDownCard",
            '',
            '更多',
            menuTexts=['item1', 'item2', 'item3'],
            menuIcons=[FluentIcon.PLAY, FluentIcon.PAUSE, FluentIcon.SEND],
            triggered=[lambda: print('itme1'), lambda: print('itme2'), lambda: print('itme3')],
            parent=self
        )
        self.transparentDropDownCard = TransparentDropDownCard(
            FluentIcon.ALIGNMENT,
            'TransparentDropDownCard',
            '',
            btIcon=FluentIcon.MORE,
            menuTexts=['item1', 'item2', 'item3'],
            menuIcons=[FluentIcon.PLAY, FluentIcon.PAUSE, FluentIcon.SEND],
            triggered=[lambda: print('itme1'), lambda: print('itme2'), lambda: print('itme3')],
            parent=self
        )
        ########################
        self.dropDownToolCard = DropDownToolCard(
            FluentIcon.WIFI,
            'DropDownToolCard',
            '',
            FluentIcon.MORE,
            menuTexts=['item1', 'item2', 'item3'],
            menuIcons=[FluentIcon.PLAY, FluentIcon.PAUSE, FluentIcon.SEND],
            triggered=[lambda: print('itme1'), lambda: print('itme2'), lambda: print('itme3')],
            parent=self
        )
        self.primaryDropDownToolCard = PrimaryDropDownToolCard(
            WinFluentIcon.RETURN,
            'PrimaryDropToolCard',
            '',
            WinFluentIcon.MORE,
            menuTexts=['item1', 'item2', 'item3'],
            menuIcons=[FluentIcon.PLAY, FluentIcon.PAUSE, FluentIcon.SEND],
            triggered=[lambda: print('itme1'), lambda: print('itme2'), lambda: print('itme3')],
            parent=self
        )
        self.transparentDropDownToolCard = TransparentDropDownToolCard(
            WinFluentIcon.SEND,
            'PrimaryDropToolCard',
            '',
            WinFluentIcon.MORE,
            menuTexts=['item1', 'item2', 'item3'],
            menuIcons=[FluentIcon.PLAY, FluentIcon.PAUSE, FluentIcon.SEND],
            triggered=[lambda: print('itme1'), lambda: print('itme2'), lambda: print('itme3')],
            parent=self
        )

    def initGroupCard(self):
        self.buttonCardGroup.addSettingCards([
            self.buttonCard,
            self.primaryButtonCard,
            self.transparentButtonCard
        ])
        self.toolButtonCardGroup.addSettingCards([
            self.toolButtonCard,
            self.primaryToolButtonCard,
            self.transparentToolButtonCard
        ])
        self.otherButtonCardGroup.addSettingCards([
            self.switchButtonCard,
            self.checkBoxCard,
            self.hyperLinkCard
        ])
        self.dropDownButtonCardGroup.addSettingCards([
            self.dropDownCard,
            self.primaryDropDownCard,
            self.transparentDropDownCard
        ])
        self.dropDownToolButtonCardGroup.addSettingCards([
            self.dropDownToolCard,
            self.primaryDropDownToolCard,
            self.transparentDropDownToolCard
        ])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    setTheme(Theme.AUTO)
    demo.show()
    sys.exit(app.exec())