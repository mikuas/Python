import json
import sys

from PySide6.QtWidgets import QApplication
from qfluentwidgets import SettingCardGroup, FluentIcon, setTheme, Theme, Action

from QFluentWidgets.FluentWidgetModule.FluentWidgets import (
    VerticalScrollWidget, WinFluentIcon, ButtonCard, PrimaryButtonCard, TransparentButtonCard, ToolButtonCard,
    PrimaryToolButtonCard, TransparentToolButtonCard, SwitchButtonCard, CheckBoxCard, HyperLinkCard, DropDownCard,
    PrimaryDropDownCard, TransparentDropDownCard, DropDownToolCard, PrimaryDropDownToolCard,
    TransparentDropDownToolCard,
    SplitCard, PrimarySplitCard, ExpandGroupCard, ComboBoxCard, EditComboBoxCard, OptionsCard, Dialog, Menu,
    MoreButtonCard, CustomColorCard
)

from QFluentWidgets.FluentWidgetModule.FluentWidgets.widgets.acrylic_cards import AcrylicComboBoxCard, AcrylicEditComboBoxCard


class CardWidget(VerticalScrollWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("DEMO")
        self.initCard()
        self.initCardGroup()
        self.initLayout()

    def initLayout(self):
        self.vLayout.addWidget(self.btCardGroup)

    def initCardGroup(self):
        self.btCardGroup = SettingCardGroup("Card Group", self)
        self.btCardGroup.addSettingCards([
            self.buttonCard,
            self.primaryButtonCard,
            self.transparentButtonCard,
            self.toolButtonCard,
            self.primaryToolButtonCard,
            self.transparentToolButtonCard,
            self.switchButtonCard,
            self.checkButtonCard,
            self.hyperLinkCard,
            self.dropDownCard,
            self.primaryDropDownCard,
            self.transparentDropDownCard,
            self.dropDownToolCard,
            self.primaryDropDownToolCard,
            self.transparentDropDownToolCard,
            self.splitCard,
            self.primarySplitCard
        ])

    def initCard(self):
        self.buttonCard = ButtonCard(
            WinFluentIcon.HOME,
            "ButtonCard",
            "None",
            "确定",
            parent=self
        )
        self.primaryButtonCard = PrimaryButtonCard(
            WinFluentIcon.WIN_11_LOG,
            "PrimaryButtonCard",
            "None",
            "确定",
            parent=self
        )
        self.transparentButtonCard = TransparentButtonCard(
            WinFluentIcon.XIN_HAO,
            "TransparentButtonCard",
            "None",
            "确定",
            parent=self
        )
        self.toolButtonCard = ToolButtonCard(
            WinFluentIcon.EMAILO_MESSAGE,
            "ToolButtonCard",
            "None",
            FluentIcon.SEND,
            self
        )
        self.primaryToolButtonCard = PrimaryToolButtonCard(
            WinFluentIcon.MAN_USER,
            "PrimaryToolButtonCard",
            "None",
            FluentIcon.MORE,
            self
        )
        self.transparentToolButtonCard = TransparentToolButtonCard(
            WinFluentIcon.MUSIC,
            "TransparentToolButtonCard",
            "None",
            FluentIcon.MENU,
            self
        )
        self.switchButtonCard = SwitchButtonCard(
            WinFluentIcon.EXPLORER,
            "SwitchButtonCard",
            "None",
            True,
            self
        )
        self.checkButtonCard = CheckBoxCard(
            WinFluentIcon.MORE,
            "CheckBoxCard",
            "None",
            True,
            parent=self
        )
        self.hyperLinkCard = HyperLinkCard(
            "https://www.bilibili.com",
            WinFluentIcon.VIDEO_FOLDER,
            "HyperLinkCard",
            "None",
            "BiliBili",
            parent=self
        )
        self.dropDownCard = DropDownCard(
            WinFluentIcon.GAME_FOLDER,
            "DropDownCard",
            "None",
            "Xia La",
            menuTexts=["Item1", "Item2", "Item3"],
            parent=self
        )
        self.dropDownCard.button.setMenu(self.dropDownCard.menu)
        self.primaryDropDownCard = PrimaryDropDownCard(
            WinFluentIcon.ADD_CHAT,
            "PrimaryDropDownCard",
            "None",
            btIcon=FluentIcon.MORE,
            menuTexts=["Item1", "Item2", "Item3"],
            parent=self
        )
        self.transparentDropDownCard = TransparentDropDownCard(
            WinFluentIcon.RADIUS_WIN_11_LOG,
            "TransparentDropDownCard",
            "None",
            "Xia La",
            FluentIcon.MORE,
            ["Item1", "Item2", "Item3"],
            parent=self
        )
        self.dropDownToolCard = DropDownToolCard(
            WinFluentIcon.RE_BOOT,
            "DropDownToolCard",
            "None",
            FluentIcon.MORE,
            ["Item1", "Item2", "Item3"],
            parent=self
        )
        self.primaryDropDownToolCard = PrimaryDropDownToolCard(
            WinFluentIcon.SHI_ZHON,
            "PrimaryDropDownToolCard",
            "None",
            FluentIcon.MORE,
            ["Item1", "Item2", "Item3"],
            [FluentIcon.COPY, FluentIcon.PASTE, FluentIcon.CUT],
            parent=self
        )
        self.transparentDropDownToolCard = TransparentDropDownToolCard(
            WinFluentIcon.HELP,
            "TransparentDropDownToolCard",
            "None",
            FluentIcon.MORE,
            ["Item1", "Item2", "Item3"],
            [FluentIcon.COPY, FluentIcon.PASTE, FluentIcon.CUT],
            parent=self
        )
        self.splitCard = SplitCard(
            WinFluentIcon.IMAGE_FILE,
            "SplitCard",
            "None",
            "Xia La",
            FluentIcon.MORE,
            ["Item1", "Item2", "Item3"],
            parent=self
        )
        self.primarySplitCard = PrimarySplitCard(
            WinFluentIcon.PAINT,
            "PrimarySplitCard",
            "None",
            "Xia La",
            FluentIcon.MORE,
            ["Item1", "Item2", "Item3"],
            [FluentIcon.COPY, FluentIcon.PASTE, FluentIcon.CUT],
            parent=self
        )


class ExpandCardWidget(VerticalScrollWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initCardGroup()
        self.initCard()
        self.initLayout()

    def initLayout(self):
        self.vLayout.addWidget(self.expandCardGroup)

    def initCardGroup(self):
        self.expandCardGroup = ExpandGroupCard(WinFluentIcon.SETTING, "光翼--展开", '', self)

    def initCard(self):
        self.expandCardGroup.addButtonCard(
            "ButtonCard",
            FluentIcon.HOME,
            '确定',
            self
        ).clicked.connect(
            lambda: Dialog("222", "111", self).exec()
        )
        self.expandCardGroup.addPrimaryButtonCard(
            "PrimaryButtonCard",
            FluentIcon.HELP,
            '确定',
            self
        )
        self.expandCardGroup.addTransparentButtonCard(
            "TransparentButtonCard",
            FluentIcon.MUSIC,
            '确定',
            self
        )
        self.expandCardGroup.addSliderCard(
            "SliderCard",
            (0, 100),
            20,
            parent=self
        )


class ComboBoxCardWidget(VerticalScrollWidget):
    def __init__(self):
        super().__init__()
        with open("./data/json/data.json", 'r', encoding='utf-8') as f:
            self.girls = json.load(f)["GirlName"]
        self.initCard()
        self.initCardGroup()
        self.initLayout()

    def initLayout(self):
        self.vLayout.addWidget(self.comboBoxCardGroup)

    def initCardGroup(self):
        self.comboBoxCardGroup = SettingCardGroup("ComBoBoxCard")
        self.comboBoxCardGroup.addSettingCards([
            self.comboBoxCard,
            self.editComboBoxCard,
            self.optionCard,
            self.acrylicComboBoxCard,
            self.acrylicEditComboBoxCard
        ])

    def initCard(self):
        self.comboBoxCard = ComboBoxCard(
            WinFluentIcon.LIKE,
            "ComboBoxCard",
            "None",
            self.girls,
            parent=self
        )
        self.editComboBoxCard = EditComboBoxCard(
            WinFluentIcon.RADIUS_WIN_11_LOG,
            "EditComboBoxCard",
            "None",
            self.girls,
            parent=self
        )
        self.optionCard = OptionsCard(
            WinFluentIcon.EDIT_FILE,
            "OptionsCard",
            "None",
            self.girls,
            "Selected"
        )
        self.acrylicComboBoxCard = AcrylicComboBoxCard(
            WinFluentIcon.DOWNLOAD_FROM_THE_CLOUD,
            "AcrylicComboBoxCard",
            "None",
            self.girls,
            parent=self
        )
        self.acrylicEditComboBoxCard = AcrylicEditComboBoxCard(
            WinFluentIcon.CHAT_MESSAGE,
            "AcrylicEditComboBoxCard",
            "None",
            self.girls,
            parent=self
        )


class MenuWidget(VerticalScrollWidget):
    def __init__(self):
        super().__init__()
        self.initCard()
        self.initMenu()
        self.initCardGroup()
        self.initLayout()
        self.initLayout()
        self.connectSignalSlots()

    def initMenu(self):
        self.menu = Menu(self)
        self.menu.addMenus([
            Action(FluentIcon.COPY, "Copy"),
            Action(FluentIcon.PASTE, "Paste"),
            Action(FluentIcon.CUT, "Cut"),
        ])

    def initLayout(self):
        self.vLayout.addWidget(self.twoButtonCardGroup)

    def initCardGroup(self):
        self.twoButtonCardGroup = SettingCardGroup("More ButtonCard")
        self.twoButtonCardGroup.addSettingCards([
            self.twoButtonCard,
            CustomColorCard(
                '设置主题色',
                "选择主题色",
                self
            )
        ])

    def initCard(self):
        self.twoButtonCard = MoreButtonCard(
            FluentIcon.MORE,
            "MoreButtonCard",
            "None",
            "确定",
            parent=self
        )

    def connectSignalSlots(self):
        self.twoButtonCard.moreButton.clicked.connect(
            lambda: self.menu.execWidget(self.twoButtonCard.moreButton)
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MenuWidget()
    window.resize(1000, 550)
    setTheme(Theme.AUTO)
    window.show()
    sys.exit(app.exec())