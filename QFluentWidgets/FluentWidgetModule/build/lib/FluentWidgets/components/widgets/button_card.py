# coding:utf-8
from typing import Union

from PySide6.QtCore import QSize, QUrl
from PySide6.QtGui import Qt, QIcon
from PySide6.QtWidgets import QWidget
from qfluentwidgets import (
    PushButton, PrimaryPushButton, TransparentPushButton, ToolButton, PrimaryToolButton, TransparentToolButton,
    DropDownPushButton, PrimaryDropDownPushButton, FluentIconBase, TransparentDropDownPushButton, DropDownToolButton,
    PrimaryDropDownToolButton, TransparentDropDownToolButton, SplitPushButton, PrimarySplitPushButton, HyperlinkButton,
    CheckBox, Action, SwitchButton
)
from qfluentwidgets.components.material import AcrylicMenu

from .custom_card import CardBase


class ButtonCardBase(CardBase):
    # noinspection PyUnusedLocal
    def __init__(
            self,
            icon,
            title=None,
            content=None,
            parent=None,
            btText: str = None,
            btIcon: Union[QIcon, str, FluentIconBase] = None
    ):
        super().__init__()
        self.button = None
        self.initIcon(icon).initTitle(title).initContent(content).initLayout()

    def initButton(self):
        self.hBoxLayout.addWidget(self.button, 0, Qt.AlignmentFlag.AlignRight)
        return self

    def insertWidget(self, index: int, widget: QWidget, stretch: int = 0, alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignRight):
        self.hBoxLayout.insertWidget(index, widget, stretch, alignment)
        return self

    def setButtonText(self, text: str):
        self.button.setText(text)
        return self

    def setButtonIcon(self, icon: Union[QIcon, str, FluentIconBase]):
        self.button.setIcon(icon)
        return self

    def setButtonIconSize(self, width: int, height: int):
        self.button.setIconSize(QSize(width, height))
        return self

    def setButtonFixedWidth(self, width: int):
        self.button.setFixedWidth(width)
        return self

    def setButtonFixedHeight(self, height: int):
        self.button.setFixedHeight(height)
        return self

    def setButtonMinWidth(self, width: int):
        self.button.setMinimumWidth(width)
        return self

    def setButtonFixedSize(self, width: int, height: int):
        self.button.setFixedSize(width, height)
        return self


class ButtonCard(ButtonCardBase):
    """ 标准按钮卡片 """
    def __init__(self, icon, title, content, btText=None, btIcon=None, parent=None):
        super().__init__(icon, title, content, parent)
        self.button = PushButton(self)
        self.setButtonText(btText).setButtonIcon(btIcon).initButton().setButtonMinWidth(120)


class PrimaryButtonCard(ButtonCardBase):
    """ 主题色按钮卡片 """
    def __init__(self, icon, title, content, btText=None, btIcon=None, parent=None):
        super().__init__(icon, title, content, parent)
        self.button = PrimaryPushButton(self)
        self.setButtonText(btText).setButtonIcon(btIcon).initButton().setButtonMinWidth(120)


class TransparentButtonCard(ButtonCardBase):
    """ 透明按钮卡片 """
    def __init__(self, icon, title, content, btText=None, btIcon=None, parent=None):
        super().__init__(icon, title, content, parent)
        self.button = TransparentPushButton(self)
        self.setButtonText(btText).setButtonIcon(btIcon).initButton().setButtonMinWidth(120)


class ToolButtonCard(ButtonCardBase):
    """ 工具按钮卡片 """
    def __init__(self, icon, title, content, btIcon=None, parent=None):
        super().__init__(icon, title, content, parent)
        self.button = ToolButton(self)
        self.setButtonIcon(btIcon).initButton()


class PrimaryToolButtonCard(ButtonCardBase):
    """ 主题色工具按钮卡片 """
    def __init__(self, icon, title, content, btIcon=None, parent=None):
        super().__init__(icon, title, content, parent)
        self.button = PrimaryToolButton(self)
        self.setButtonIcon(btIcon).initButton()


class TransparentToolButtonCard(ButtonCardBase):
    """ 透明工具按钮卡片 """
    def __init__(self, icon, title, content, btIcon=None, parent=None):
        super().__init__(icon, title, content, parent)
        self.button = TransparentToolButton(self)
        self.setButtonIcon(btIcon).initButton()


class SwitchButtonCard(ButtonCardBase):
    """ 状态卡关按钮 """
    def __init__(self, icon=None, title=None, content=None, isChecked: bool = False, parent=None):
        super().__init__(icon, title, content, parent)
        self.button = SwitchButton(self)
        self.initButton().setButtonChecked(isChecked)
        self.button._onText = "开"
        self.button._offText = "关"

    def setButtonChecked(self, isChecked=False):
        self.button.setChecked(isChecked)
        self.button.setText('开') if isChecked else self.button.setText('关')


class CheckBoxCard(ButtonCardBase):
    """ 复选框卡片 """
    def __init__(self, icon=None, title=None, content=None, isChecked: bool = False, boxText: str = None, parent=None):
        super().__init__(icon, title, content, parent)
        self.button = CheckBox(self)
        self.setButtonText(boxText).initButton().setButtonChecked(isChecked)
        self.hBoxLayout.setContentsMargins(20, 11, 20, 11)

    def setButtonChecked(self, isChecked=False):
        self.button.setChecked(isChecked)


class HyperLinkCard(ButtonCardBase):
    """链接按钮"""
    def __init__(self, url: str, icon, title, content, btText=None, btIcon=None, parent=None):
        super().__init__(icon, title, content, parent)
        self.button = HyperlinkButton(self)
        self.setButtonText(btText).setButtonIcon(btIcon).setUrl(url).initButton()

    def setUrl(self, url: str | QUrl):
        self.button.setUrl(url)
        return self


class DropDownCardBase(ButtonCardBase):
    # noinspection PyUnusedLocal
    def __init__(
            self, icon=None, title=None, content=None, btText=None,
            btIcon=None, parent=None, menuTexts: list[str] = None,
            menuIcons: list[Union[QIcon, str, FluentIconBase]] = None, triggered: list = None
    ):
        super().__init__(icon, title, content, parent)
        self.menu = AcrylicMenu('', self)

    def addMenu(self, texts, icons, triggered):
        if texts:
            if icons:
                for icon, text, in zip(icons, texts):
                    self.menu.addAction(Action(icon, text, triggered=triggered[texts.index(text)] if triggered else None))
            else:
                for text in texts:
                    self.menu.addAction(Action(text, triggered=triggered[text.index(text)] if triggered else None))

    def initButton(self, btText: str = None, btIcon: Union[QIcon, str, FluentIconBase] = None):
        super().initButton()
        self.setButtonIcon(btIcon).setButtonText(btText)
        return self


class DropDownCard(DropDownCardBase):
    """普通下拉按钮卡片"""
    def __init__(
            self, icon, title, content, btText=None, btIcon=None,
            menuTexts=None, menuIcons=None, triggered=None, parent=None
    ):
        super().__init__(icon, title, content, btText, btIcon, parent)
        self.button = DropDownPushButton(self)
        self.initButton(btText, btIcon).addMenu(menuTexts, menuIcons, triggered)
        self.button.setMenu(self.menu)


class PrimaryDropDownCard(DropDownCardBase):
    """主题色下拉按钮卡片"""
    def __init__(
            self, icon, title, content, btText=None, btIcon=None,
            menuTexts=None, menuIcons=None, triggered=None, parent=None
    ):
        super().__init__(icon, title, content, btText, btIcon, menuTexts, menuIcons, triggered, parent)
        self.button = PrimaryDropDownPushButton(self)
        self.initButton(btText, btIcon).addMenu(menuTexts, menuIcons, triggered)
        self.button.setMenu(self.menu)


class TransparentDropDownCard(DropDownCardBase):
    """透明下拉按钮卡片"""
    def __init__(
            self, icon, title, content, btText=None, btIcon=None,
            menuTexts=None, menuIcons=None, triggered=None, parent=None
    ):
        super().__init__(
            icon, title, content, btText, btIcon, parent
        )
        self.button = TransparentDropDownPushButton(self)
        self.initButton(btText, btIcon).addMenu(menuTexts, menuIcons, triggered)
        self.button.setMenu(self.menu)


class DropDownToolCard(DropDownCardBase):
    """下拉工具按钮卡片"""
    def __init__(
            self, icon, title, content, btIcon=None, menuTexts=None,
            menuIcons=None, triggered=None, parent=None
    ):
        super().__init__(icon, title, content, None, btIcon, parent)
        self.button = DropDownToolButton(self)
        self.initButton(btIcon=btIcon).addMenu(menuTexts, menuIcons, triggered)
        self.button.setMenu(self.menu)


class PrimaryDropDownToolCard(DropDownCardBase):
    """下拉工具主题色按钮卡片"""
    def __init__(
            self, icon, title, content, btIcon=None, menuTexts=None,
            menuIcons=None, triggered=None, parent=None
    ):
        super().__init__(icon, title, content, btIcon, parent)
        self.button = PrimaryDropDownToolButton(self)
        self.initButton(btIcon=btIcon).addMenu(menuTexts, menuIcons, triggered)
        self.button.setMenu(self.menu)


class TransparentDropDownToolCard(DropDownCardBase):
    """下拉工具透明按钮卡片"""
    def __init__(
            self, icon, title, content, btIcon=None, menuTexts=None,
            menuIcons=None, triggered=None, parent=None
    ):
        super().__init__(icon, title, content, btIcon, parent)
        self.button = TransparentDropDownToolButton(self)
        self.initButton(btIcon=btIcon).addMenu(menuTexts, menuIcons, triggered)
        self.button.setMenu(self.menu)


class SplitCard(DropDownCardBase):
    """拆分按钮"""
    def __init__(
            self, icon, title, content, btText=None, btIcon=None,
            menuTexts=None, menuIcons=None, triggered=None, parent=None
    ):
        super().__init__(icon, title, content, btText, btIcon, parent)
        self.button = SplitPushButton(self)
        self.initButton(btIcon=btIcon).addMenu(menuTexts, menuIcons, triggered)
        self.button.setFlyout(self.menu)


class PrimarySplitCard(DropDownCardBase):
    """主题色拆分按钮"""
    def __init__(
            self, icon, title, content, btText=None, btIcon=None,
            menuTexts=None, menuIcons=None, triggered=None, parent=None
    ):
        super().__init__(icon, title, content, btText, btIcon, parent)
        self.button = PrimarySplitPushButton(self)
        self.initButton(btIcon=btIcon).addMenu(menuTexts, menuIcons, triggered)
        self.button.setFlyout(self.menu)
