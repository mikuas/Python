from qfluentwidgets import PushButton, PrimaryPushButton, TransparentPushButton, ToolButton, PrimaryToolButton, \
    TransparentToolButton, ComboBox, EditableComboBox, DropDownPushButton, PrimaryDropDownPushButton, \
    TransparentDropDownPushButton, DropDownToolButton, PrimaryDropDownToolButton, TransparentDropDownToolButton

from ...FluentCardWidget.CustomCard import CustomButtonCard, CustomSwitchButtonCard, CustomDropDownButtonCard
from ...FluentCardWidget.ComboBoxCard import CustomComboBoxCard


class PushButtonC(CustomButtonCard):
    """标准按钮卡片"""
    def __init__(self, icon, title, content, buttonText=None, buttonIcon=None, parent=None):
        super().__init__(icon, title, content, buttonText, buttonIcon, parent, PushButton)


class PrimaryButtonC(CustomButtonCard):
    """主题色按钮卡片"""
    def __init__(self, icon, title, content, buttonText=None, buttonIcon=None, parent=None):
        super().__init__(icon, title, content, buttonText, buttonIcon, parent, PrimaryPushButton)


class TransparentButtonC(CustomButtonCard):
    """透明按钮卡片"""
    def __init__(self, icon, title, content, buttonText=None, buttonIcon=None, parent=None):
        super().__init__(icon, title, content, buttonText, buttonIcon, parent, TransparentPushButton)


class ToolButtonC(CustomButtonCard):
    """工具按钮卡片"""
    def __init__(self, icon, title, content, buttonText=None, buttonIcon=None, parent=None):
        super().__init__(icon, title, content, buttonText, buttonIcon, parent, ToolButton)


class PrimaryToolButtonC(CustomButtonCard):
    """主题色工具按钮卡片"""
    def __init__(self, icon, title, content, buttonText=None, buttonIcon=None, parent=None):
        super().__init__(icon, title, content, buttonText, buttonIcon, parent, PrimaryToolButton)


class TransparentToolButtonC(CustomButtonCard):
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


class DropDownButtonCard(CustomDropDownButtonCard):
    """普通下拉按钮卡片"""
    def __init__(self, icon, title, content, menuIcon, menuText, triggered, parent=None):
        super().__init__(icon, title, content, menuIcon, menuText, triggered, parent, DropDownPushButton)

class PrimaryDropDownButtonCard(CustomDropDownButtonCard):
    """主题色下拉按钮卡片"""
    def __init__(self, icon, title, content, menuIcon, menuText, triggered, parent=None):
        super().__init__(icon, title, content, menuIcon, menuText, triggered, parent, PrimaryDropDownPushButton)


class TransparentDropDownButtonCard(CustomDropDownButtonCard):
    """透明下拉按钮卡片"""
    def __init__(self, icon, title, content, menuIcon, menuText, triggered, parent=None):
        super().__init__(icon, title, content, menuIcon, menuText, triggered, parent, PrimaryDropDownPushButton)


class DropDownToolButtonCard(CustomDropDownButtonCard):
    """下拉工具按钮卡片"""
    def __init__(self, icon, title, content, menuIcon, menuText, triggered, parent=None):
        super().__init__(icon, title, content, menuIcon, menuText, triggered, parent, PrimaryDropDownPushButton)