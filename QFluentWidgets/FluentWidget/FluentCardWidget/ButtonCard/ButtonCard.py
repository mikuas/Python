from qfluentwidgets import PushButton, PrimaryPushButton, TransparentPushButton, ToolButton, PrimaryToolButton, \
    TransparentToolButton, ComboBox, EditableComboBox, DropDownPushButton, PrimaryDropDownPushButton, \
    TransparentDropDownPushButton, DropDownToolButton, PrimaryDropDownToolButton, TransparentDropDownToolButton, \
    SplitPushButton

from ...FluentCardWidget.CustomCard import CustomButtonCard, CustomSwitchButtonCard, CustomDropDownCard
from ...FluentCardWidget.ComboBoxCard import CustomComboBoxCard


class PushButtonCard(CustomButtonCard):
    """标准按钮卡片"""
    def __init__(self, icon, title, content, buttonText=None, buttonIcon=None, parent=None):
        super().__init__(icon, title, content, buttonText, buttonIcon, parent, PushButton)


class PrimaryButtonCard(CustomButtonCard):
    """主题色按钮卡片"""
    def __init__(self, icon, title, content, buttonText=None, buttonIcon=None, parent=None):
        super().__init__(icon, title, content, buttonText, buttonIcon, parent, PrimaryPushButton)


class TransparentButtonCard(CustomButtonCard):
    """透明按钮卡片"""
    def __init__(self, icon, title, content, buttonText=None, buttonIcon=None, parent=None):
        super().__init__(icon, title, content, buttonText, buttonIcon, parent, TransparentPushButton)


class ToolButtonCard(CustomButtonCard):
    """工具按钮卡片"""
    def __init__(self, icon, title, content, buttonText=None, buttonIcon=None, parent=None):
        super().__init__(icon, title, content, buttonText, buttonIcon, parent, ToolButton)


class PrimaryToolButtonCard(CustomButtonCard):
    """主题色工具按钮卡片"""
    def __init__(self, icon, title, content, buttonText=None, buttonIcon=None, parent=None):
        super().__init__(icon, title, content, buttonText, buttonIcon, parent, PrimaryToolButton)


class TransparentToolButtonCard(CustomButtonCard):
    """透明工具按钮卡片"""
    def __init__(self, icon, title, content, buttonText=None, buttonIcon=None, parent=None):
        super().__init__(icon, title, content, buttonText, buttonIcon, parent, TransparentToolButton)


class SwitchButtonCard(CustomSwitchButtonCard):
    """状态卡关按钮"""
    def __init__(self, icon, title, content, status, parent=None):
        super().__init__(icon, title, content, status, parent)


class ComboBoxCard(CustomComboBoxCard):
    """下拉框卡片"""
    def __init__(self, icon, title, content, items, noSelected, info, parent=None):
        super().__init__(icon, title, content, items, noSelected, info, parent, ComboBox)


class EditComboBoxCard(CustomComboBoxCard):
    """可编辑下拉框卡片"""
    def __init__(self, icon, title, content, items, noSelected, info, parent=None):
        super().__init__(icon, title, content, items, noSelected, info, parent, EditableComboBox)


class DropDownCard(CustomDropDownCard):
    """普通下拉按钮卡片"""
    def __init__(
            self, icon, title, content, buttonText=None, buttonIcon=None,
            menuText=None, menuIcon=None, triggered=None, parent=None
    ):
        super().__init__(icon, title, content, buttonText, buttonIcon, menuText, menuIcon, triggered, parent, DropDownPushButton)
        self.button.setMenu(self.menu)


class PrimaryDropDownCard(CustomDropDownCard):
    """主题色下拉按钮卡片"""
    def __init__(
            self, icon, title, content, buttonText=None, buttonIcon=None,
            menuText=None, menuIcon=None, triggered=None, parent=None
    ):
        super().__init__(icon, title, content, buttonText, buttonIcon, menuText, menuIcon, triggered, parent, PrimaryDropDownPushButton)
        self.button.setMenu(self.menu)

class TransparentDropDownCard(CustomDropDownCard):
    """透明下拉按钮卡片"""
    def __init__(
            self, icon, title, content, buttonText=None, buttonIcon=None,
            menuText=None, menuIcon=None, triggered=None, parent=None
    ):
        super().__init__(icon, title, content, buttonText, buttonIcon, menuText, menuIcon, triggered, parent, TransparentDropDownPushButton)
        self.button.setMenu(self.menu)

class DropDownToolCard(CustomDropDownCard):
    """下拉工具按钮卡片"""
    def __init__(
            self, icon, title, content, buttonText=None, buttonIcon=None,
            menuText=None, menuIcon=None, triggered=None, parent=None
    ):
        super().__init__(icon, title, content, buttonText, buttonIcon, menuText, menuIcon, triggered, parent, DropDownToolButton)
        self.button.setMenu(self.menu)


class PrimaryDropDownToolCard(CustomDropDownCard):
    """下拉工具主题色按钮卡片"""
    def __init__(
            self, icon, title, content, buttonText=None, buttonIcon=None,
            menuText=None, menuIcon=None, triggered=None, parent=None
    ):
        super().__init__(icon, title, content, buttonText, buttonIcon, menuText, menuIcon, triggered, parent, PrimaryDropDownToolButton)
        self.button.setMenu(self.menu)

class TransparentDropDownToolCard(CustomDropDownCard):
    """下拉工具透明按钮卡片"""
    def __init__(
            self, icon, title, content, buttonText=None, buttonIcon=None,
            menuText=None, menuIcon=None, triggered=None, parent=None
    ):
        super().__init__(icon, title, content, buttonText, buttonIcon, menuText, menuIcon, triggered, parent, TransparentDropDownToolButton)
        self.button.setMenu(self.menu)

class SplitButtonCard(CustomDropDownCard):
    """拆分按钮"""
    def __init__(
            self, icon, title, content, buttonText=None, buttonIcon=None,
            menuText=None, menuIcon=None, triggered=None, parent=None
    ):
        super().__init__(icon, title, content, buttonText, buttonIcon, menuText, menuIcon, triggered, parent, SplitPushButton)
        self.button.setFixedWidth()
        self.button.setFlyout(self.menu)
