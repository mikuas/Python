from typing import Union

from PySide6.QtCore import QSize
from PySide6.QtGui import Qt, QIcon
from qfluentwidgets import (
    PushButton, PrimaryPushButton, TransparentPushButton, ToolButton, PrimaryToolButton, TransparentToolButton,
    DropDownPushButton, PrimaryDropDownPushButton, FluentIconBase, TransparentDropDownPushButton, DropDownToolButton,
    PrimaryDropDownToolButton, TransparentDropDownToolButton, SplitPushButton, PrimarySplitPushButton, HyperlinkButton,
    CheckBox, RoundMenu, Action, SwitchButton
)

from ...widgetdoc import CustomSwitchButtonCard, CustomDropDownCard, CustomButtonCardParent, CustomCheckBoxCard
from .custom_card import CustomCard


class CustomButtonCard(CustomButtonCardParent, CustomCard):
    # noinspection PyUnusedLocal
    def __init__(self, icon, title, content, parent=None, btType=None, btText=None, btIcon=None):
        CustomCard.__init__(self, parent)
        self.initIcon(icon).initTitle(title).initContent(content).initLayout()
        self.initButton(btType)

    def initButton(self, btType):
        self.button = btType(self)
        self.hBoxLayout.addWidget(self.button, 0, Qt.AlignmentFlag.AlignRight)
        return self

    def setButtonText(self, text: str):
        self.button.setText(text)
        return self

    def setButtonIcon(self, icon: Union[QIcon, str, FluentIconBase]):
        self.button.setIcon(icon)
        return self

    def setButtonIconSize(self, width, height):
        self.button.setIconSize(QSize(width, height))
        return self

    def setButtonFixedWidth(self, width):
        self.button.setFixedWidth(width)
        return self

    def setButtonFixedHeight(self, height):
        self.button.setFixedHeight(height)
        return self

    def setButtonFixedSize(self, width, height):
        self.button.setFixedSize(width, height)
        return self


# 标准按钮
class ButtonCard(CustomButtonCard):
    """ 标准按钮卡片 """
    def __init__(self, icon, title, content, btText=None, btIcon=None, parent=None):
        super().__init__(icon, title, content, parent, PushButton)
        self.setButtonText(btText).setButtonIcon(btIcon)


class PrimaryButtonCard(CustomButtonCard):
    """ 主题色按钮卡片 """
    def __init__(self, icon, title, content, btText=None, btIcon=None, parent=None):
        super().__init__(icon, title, content, parent, PrimaryPushButton)
        self.setButtonText(btText).setButtonIcon(btIcon)


class TransparentButtonCard(CustomButtonCard):
    """ 透明按钮卡片 """
    def __init__(self, icon, title, content, btText=None, btIcon=None, parent=None):
        super().__init__(icon, title, content, parent, TransparentPushButton)
        self.setButtonText(btText).setButtonIcon(btIcon)


# 工具按钮
class ToolButtonCard(CustomButtonCard):
    """ 工具按钮卡片 """
    def __init__(self, icon, title, content, btIcon=None, parent=None):
        super().__init__(icon, title, content, parent, ToolButton)
        self.setButtonIcon(btIcon)


class PrimaryToolButtonCard(CustomButtonCard):
    """ 主题色工具按钮卡片 """
    def __init__(self, icon, title, content, btIcon=None, parent=None):
        super().__init__(icon, title, content, parent, PrimaryToolButton)
        self.setButtonIcon(btIcon)


class TransparentToolButtonCard(CustomButtonCard):
    """ 透明工具按钮卡片 """
    def __init__(self, icon, title, content, btIcon=None, parent=None):
        super().__init__(icon, title, content, parent, TransparentToolButton)
        self.setButtonIcon(btIcon)


# 状态卡关按钮
class SwitchButtonCard(CustomSwitchButtonCard, CustomButtonCard):
    """ 状态卡关按钮 """
    def __init__(self, icon, title, content, isChecked=False, parent=None):
        CustomButtonCard.__init__(self, icon, title, content, parent, SwitchButton)
        self.setButtonChecked(isChecked)
        self.button._onText = "开"
        self.button._offText = "关"

    def setButtonChecked(self, isChecked=False):
        self.button.setChecked(isChecked)
        self.button.setText('开') if isChecked else self.button.setText('关')


# 复选框
class CheckBoxCard(CustomCheckBoxCard, CustomButtonCard):
    """ 复选框 """
    def __init__(self, icon, title, content, isChecked=False, boxText=None, boxIcon=None, parent=None):
        CustomButtonCard.__init__(self, icon, title, content, parent, CheckBox)
        self.setButtonText(boxText).setButtonIcon(QIcon(boxIcon))
        self.setButtonChecked(isChecked)

    def setButtonChecked(self, isChecked=False):
        self.button.setChecked(isChecked)


# 超链接
class HyperLinkCard(CustomButtonCard):
    """链接按钮"""
    def __init__(self, url: str, icon, title, content, btText=None, btIcon=None, parent=None):
        super().__init__(icon, title, content, parent, HyperlinkButton, btText, btIcon)
        self.setButtonText(btText).setButtonIcon(btIcon)
        self.setUrl(url)

    def setUrl(self, url):
        self.button.setUrl(url)


class DropDownCard(CustomDropDownCard, CustomButtonCard):
    """普通下拉按钮卡片"""
    def __init__(
            self, icon, title, content, btText=None, btIcon=None,
            menuTexts=None, menuIcons=None, triggered=None, parent=None, btType=DropDownPushButton
    ):
        CustomButtonCard.__init__(self, icon, title, content, parent, btType)
        self.setButtonIcon(btIcon).setButtonText(btText)
        self.addMenu(menuTexts, menuIcons, triggered)

    def addMenu(self, texts, icons, triggered):
        self.menu = RoundMenu(parent=self.button)
        if texts:
            if icons:
                for icon, text, in zip(icons, texts):
                    self.menu.addAction(Action(
                        icon, text, triggered=triggered[texts.index(text)] if triggered else None
                    ))
            else:
                for text in texts:
                    self.menu.addAction(Action(
                        text, triggered=triggered[text.index(text)] if triggered else None
                    ))


class PrimaryDropDownCard(DropDownCard):
    """主题色下拉按钮卡片"""
    def __init__(
            self, icon, title, content, btText=None, btIcon=None,
            menuTexts=None, menuIcons=None, triggered=None, parent=None
    ):
        super().__init__(icon, title, content, btText, btIcon, menuTexts, menuIcons, triggered, parent, PrimaryDropDownPushButton)
        self.button.setMenu(self.menu)


class TransparentDropDownCard(DropDownCard):
    """透明下拉按钮卡片"""
    def __init__(
            self, icon, title, content, btText=None, btIcon=None,
            menuTexts=None, menuIcons=None, triggered=None, parent=None
    ):
        super().__init__(icon, title, content, btText, btIcon, menuTexts, menuIcons, triggered, parent, TransparentDropDownPushButton)
        self.button.setMenu(self.menu)


class DropDownToolCard(DropDownCard):
    """下拉工具按钮卡片"""
    def __init__(
            self, icon, title, content, btIcon=None, menuTexts=None, menuIcons=None,
            triggered=None, parent=None, btType=DropDownToolButton
    ):
        super().__init__(icon, title, content, None, btIcon, menuTexts, menuIcons, triggered, parent, btType)
        self.button.setMenu(self.menu)


class PrimaryDropDownToolCard(DropDownToolCard):
    """下拉工具主题色按钮卡片"""
    def __init__(self, icon, title, content, btIcon=None, menuTexts=None, menuIcons=None, triggered=None, parent=None):
        super().__init__(icon, title, content, btIcon, menuTexts, menuIcons, triggered, parent, PrimaryDropDownToolButton)


class TransparentDropDownToolCard(DropDownToolCard):
    """下拉工具透明按钮卡片"""
    def __init__(self, icon, title, content, btIcon=None, menuTexts=None, menuIcons=None, triggered=None, parent=None):
        super().__init__(icon, title, content, btIcon, menuTexts, menuIcons, triggered, parent, TransparentDropDownToolButton)


class SplitCard(DropDownCard):
    """拆分按钮"""
    def __init__(
            self, icon, title, content, btText=None, btIcon=None, menuTexts=None, menuIcons=None,
            triggered=None, parent=None, btType=SplitPushButton
    ):
        super().__init__(icon, title, content, btText, btIcon, menuTexts, menuIcons, triggered, parent, btType)
        self.button.setFlyout(self.menu)


class PrimarySplitCard(SplitCard):
    """主题色拆分按钮"""
    def __init__(
            self, icon, title, content, btText=None, btIcon=None, menuTexts=None,
            menuIcons=None, triggered=None, parent=None
    ):
        super().__init__(icon, title, content, btText, btIcon, menuTexts, menuIcons, triggered, parent, PrimarySplitPushButton)
