from PySide6.QtGui import Qt
from qfluentwidgets import PushButton, PrimaryPushButton, TransparentPushButton, ToolButton, PrimaryToolButton, \
    TransparentToolButton, ComboBox, EditableComboBox, DropDownPushButton, PrimaryDropDownPushButton, \
    TransparentDropDownPushButton, DropDownToolButton, PrimaryDropDownToolButton, TransparentDropDownToolButton, \
    SplitPushButton, PrimarySplitPushButton, SplitToolButton, PrimarySplitToolButton, HyperlinkButton, TitleLabel, \
    Slider, CaptionLabel, ExpandGroupSettingCard
from qfluentwidgets.components.material import AcrylicComboBox, AcrylicEditableComboBox

from ...FluentCardWidget.CustomCard import CustomButtonCard, CustomToolCard, CustomSwitchButtonCard, CustomDropDownCard, \
    ExpandGroupCard
from ...FluentCardWidget.ComboBoxCard import CustomComboBoxCard


class ButtonCard(CustomButtonCard):
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


class ToolButtonCard(CustomToolCard):
    """工具按钮卡片"""
    def __init__(self, icon, title, content, buttonIcon=None, parent=None):
        super().__init__(icon, title, content, buttonIcon, parent, ToolButton)

class PrimaryToolButtonCard(CustomToolCard):
    """主题色工具按钮卡片"""
    def __init__(self, icon, title, content, buttonIcon=None, parent=None):
        super().__init__(icon, title, content, buttonIcon, parent, PrimaryToolButton)

class TransparentToolButtonCard(CustomToolCard):
    """透明工具按钮卡片"""
    def __init__(self, icon, title, content, buttonIcon=None, parent=None):
        super().__init__(icon, title, content, buttonIcon, parent, TransparentToolButton)

class SwitchButtonCard(CustomSwitchButtonCard):
    """状态卡关按钮"""
    def __init__(self, icon, title, content, status, parent=None):
        super().__init__(icon, title, content, status, parent)


class HyperLinkCard(CustomButtonCard):
    """链接按钮"""
    def __init__(self, url: str, icon, title, content, buttonText=None, buttonIcon=None, parent=None):
        super().__init__(icon, title, content, buttonText, buttonIcon, parent, HyperlinkButton)
        self.button.setUrl(url)


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
        self.setButtonText(buttonText)
        self.button.setMenu(self.menu)


class PrimaryDropDownCard(CustomDropDownCard):
    """主题色下拉按钮卡片"""
    def __init__(
            self, icon, title, content, buttonText=None, buttonIcon=None,
            menuText=None, menuIcon=None, triggered=None, parent=None
    ):
        super().__init__(icon, title, content, buttonText, buttonIcon, menuText, menuIcon, triggered, parent, PrimaryDropDownPushButton)
        self.setButtonText(buttonText)
        self.button.setMenu(self.menu)

class TransparentDropDownCard(CustomDropDownCard):
    """透明下拉按钮卡片"""
    def __init__(
            self, icon, title, content, buttonText=None, buttonIcon=None,
            menuText=None, menuIcon=None, triggered=None, parent=None
    ):
        super().__init__(icon, title, content, buttonText, buttonIcon, menuText, menuIcon, triggered, parent, TransparentDropDownPushButton)
        self.setButtonText(buttonText)
        self.button.setMenu(self.menu)


class DropDownToolCard(CustomDropDownCard):
    """下拉工具按钮卡片"""
    def __init__(
            self, icon, title, content, buttonIcon=None,
            menuText=None, menuIcon=None, triggered=None, parent=None
    ):
        super().__init__(icon, title, content, None, buttonIcon, menuText, menuIcon, triggered, parent, DropDownToolButton)
        self.button.setMenu(self.menu)

class PrimaryDropDownToolCard(CustomDropDownCard):
    """下拉工具主题色按钮卡片"""
    def __init__(
            self, icon, title, content, buttonIcon=None,
            menuText=None, menuIcon=None, triggered=None, parent=None
    ):
        super().__init__(icon, title, content, None, buttonIcon, menuText, menuIcon, triggered, parent, PrimaryDropDownToolButton)

        self.button.setMenu(self.menu)


class TransparentDropDownToolCard(CustomDropDownCard):
    """下拉工具透明按钮卡片"""
    def __init__(
            self, icon, title, content, buttonIcon=None,
            menuText=None, menuIcon=None, triggered=None, parent=None
    ):
        super().__init__(icon, title, content, None, buttonIcon, menuText, menuIcon, triggered, parent, TransparentDropDownToolButton)
        self.button.setMenu(self.menu)


class SplitCard(CustomDropDownCard):
    """拆分按钮"""
    def __init__(
            self, icon, title, content, buttonText=None, buttonIcon=None,
            menuText=None, menuIcon=None, triggered=None, parent=None
    ):
        super().__init__(icon, title, content, buttonText, buttonIcon, menuText, menuIcon, triggered, parent, SplitPushButton)
        self.button.setText(buttonText)
        self.button.setFlyout(self.menu)


class PrimarySplitCard(CustomDropDownCard):
    """主题色拆分按钮"""
    def __init__(
            self, icon, title, content, buttonText=None, buttonIcon=None,
            menuText=None, menuIcon=None, triggered=None, parent=None
    ):
        super().__init__(icon, title, content, buttonText, buttonIcon, menuText, menuIcon, triggered, parent, PrimarySplitPushButton)
        self.button.setText(buttonText)
        self.button.setFlyout(self.menu)


class SplitToolCard(CustomDropDownCard):
    """拆分工具按钮"""
    def __init__(
            self, icon, title, content, buttonIcon=None,
            menuTexts=None, menuIcons=None, triggered=None, parent=None
    ):
        super().__init__(icon, title, content, None, buttonIcon, menuTexts, menuIcons, triggered, parent, SplitToolButton)
        self.button.setFlyout(self.menu)

class PrimarySplitToolCard(CustomDropDownCard):
    """主题色拆分工具按钮"""
    def __init__(
            self, icon, title, content, buttonIcon=None,
            menuTexts=None, menuIcons=None, triggered=None, parent=None
    ):
        super().__init__(icon, title, content, None, buttonIcon, menuTexts, menuIcons, triggered, parent, PrimarySplitToolButton)
        self.button.setFlyout(self.menu)


class ExpandGroupCard(ExpandGroupCard):
    """展开按钮卡片"""
    def __init__(self, icon, title, content, parent=None):
        super().__init__(icon, title, content, parent)

    def addButtonCard(self, title, icon, text, __type=None):
        hLayout = self._initWidget()
        hLayout.addWidget(TitleLabel(title, self))
        button = PushButton(icon, text, self)
        button.setFixedWidth(120)
        hLayout.addStretch(1)
        hLayout.addWidget(button, 0, Qt.AlignmentFlag.AlignRight)

        return button

    def addPrimaryButtonCard(self, title, icon, text):
        return self.addButtonCard(title, icon, text, PrimaryPushButton)

    def addTransparentButtonCard(self, title, icon, text):
        return self.addButtonCard(title, icon, text, TransparentPushButton)

    def addSliderCard(self, title, ranges, defaultValue, orientation=Qt.Orientation.Horizontal):
        slider = Slider(orientation, self)
        slider.setRange(ranges[0], ranges[1])
        slider.setValue(defaultValue)
        slider.setFixedWidth(250)
        label = CaptionLabel(str(slider.value()), self)

        hLayout = self._initWidget()
        hLayout.addWidget(label)
        hLayout.addStretch(1)
        hLayout.addWidget(label, 0, Qt.AlignmentFlag.AlignRight)
        hLayout.addWidget(slider, 0, Qt.AlignmentFlag.AlignRight)

        slider.valueChanged.connect(
            lambda: label.setText(str(slider.value()))
        )

        return slider