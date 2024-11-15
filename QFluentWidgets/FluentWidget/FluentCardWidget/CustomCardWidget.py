from PySide6.QtGui import Qt
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget
from qfluentwidgets import CardWidget, IconWidget, BodyLabel, CaptionLabel, PushButton, TransparentToolButton, \
    FluentIcon, PrimaryPushButton, SwitchButton, HyperlinkButton, ComboBox, EditableComboBox, ExpandGroupSettingCard, \
    Slider


class __ButtonCard(CardWidget):
    def __init__(self, icon, title, content, buttonText=None, parent=None, button=None):
        super().__init__(parent)
        self.iconWidget = IconWidget(icon)
        self.titleLabel = BodyLabel(title, self)
        self.contentLabel = CaptionLabel(content, self)
        if buttonText is not None:
            self.button = button(buttonText, self)
        else:
            self.button = button(self)
        self.hBoxLayout = QHBoxLayout(self)
        self.vBoxLayout = QVBoxLayout()

        self.setFixedHeight(80)
        self.iconWidget.setFixedSize(32, 32)
        self.contentLabel.setTextColor("#606060", "#d2d2d2")
        self.button.setFixedWidth(120)

        self.hBoxLayout.setContentsMargins(20, 11, 11, 11)
        self.hBoxLayout.setSpacing(15)
        self.hBoxLayout.addWidget(self.iconWidget)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.addWidget(self.titleLabel, 0, Qt.AlignmentFlag.AlignVCenter)
        self.vBoxLayout.addWidget(self.contentLabel, 0, Qt.AlignmentFlag.AlignVCenter)
        self.vBoxLayout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.hBoxLayout.addLayout(self.vBoxLayout)

        self.hBoxLayout.addStretch(1)
        self.hBoxLayout.addWidget(self.button, 0, Qt.AlignmentFlag.AlignRight)


# 标准按钮卡片
class PushButtonCard(__ButtonCard):
    def __init__(self,icon,title, content,buttonText,moreButtonIcon=FluentIcon.MORE,parent=None,):
        super().__init__(icon, title, content, buttonText, parent, PushButton)
        self.moreButton = TransparentToolButton(moreButtonIcon, self)
        self.hBoxLayout.addWidget(self.moreButton, 0, Qt.AlignmentFlag.AlignRight)
        self.moreButton.setFixedSize(32, 32)


# 主题色按钮卡片
class PrimaryPushButtonCard(__ButtonCard):
    def __init__(self, icon, title, content, buttonText, moreButtonIcon=FluentIcon.MORE, parent=None):
        super().__init__(icon, title, content, buttonText, parent, PrimaryPushButton)
        self.moreButton = TransparentToolButton(moreButtonIcon, self)
        self.hBoxLayout.addWidget(self.moreButton, 0, Qt.AlignmentFlag.AlignRight)
        self.moreButton.setFixedSize(32, 32)


# 状态开关按钮卡片
class SwitchButtonCard(__ButtonCard):
    def __init__(self, icon, title, content, default: bool = False, parent=None):
        super().__init__(icon, title, content, parent=parent, button=SwitchButton)
        self.button.setChecked(default)
        self.button._offText = '关'
        self.button.onText = '开'


# 超链接按钮卡片
class HyperLinkButtonCard(__ButtonCard):
    def __init__(self, url, icon, title, content, buttonText=None, buttonIcon=None, parent=None):
        super().__init__(icon, title, content, parent=parent, button=HyperlinkButton)
        self.button.setUrl(url)
        if buttonText is not None:
            self.button.setText(buttonText)
        if buttonIcon is not None:
            self.button.setIcon(buttonIcon)


# 下拉框
class ComboBoxCard(__ButtonCard):
    def __init__(self, icon, title, content, items, noSelected: bool = False, info=None, parent=None):
        super().__init__(icon, title, content, parent=parent, button=ComboBox)
        self.button.addItems(items)
        if noSelected:
            self.button.setCurrentIndex(-1)
            self.button.setPlaceholderText(info)


# 可编辑下拉框
class EditComboBoxCard(__ButtonCard):
    def __init__(self, icon, title, content, items, noSelected: bool = False, info=None, parent=None):
        super().__init__(icon, title, content, parent=parent, button=EditableComboBox)
        self.button.addItems(items)
        if noSelected:
            self.button.setCurrentIndex(-1)
            self.button.setPlaceholderText(info)


# 下拉框按钮
class ComboxButtonCard(__ButtonCard):
    def __init__(self, icon, title, content, items: list[str], buttonText, noSelected: bool = False, info=None, parent=None, comboBox=ComboBox):
        super().__init__(icon, title, content, buttonText, parent, PrimaryPushButton)
        self.combox = comboBox(self)
        self.combox.setFixedWidth(120)
        self.combox.addItems(items)
        if noSelected:
            self.combox.setCurrentIndex(-1)
            self.combox.setPlaceholderText(info)

        self.hBoxLayout.insertWidget(3, self.combox, 0, Qt.AlignmentFlag.AlignRight)


# 可编辑下拉框按钮
class EditComboBoxButtonCard(ComboxButtonCard):
    def __init__(self, icon, title, content, items: list[str], buttonText, noSelected: bool = False, info=None, parent=None):
        super().__init__(icon, title, content, items, buttonText, noSelected, info, parent, EditableComboBox)


# 双按钮卡片
class TwoButtonCard(__ButtonCard):
    def __init__(self, icon, title, content, oneButtonText=None, oneButtonIcon=None, buttonText=None, parent=None, button=PushButton):
        super().__init__(icon, title, content, buttonText, parent, PrimaryPushButton)
        self.oneButton = button(self)
        self.oneButton.setText(oneButtonText)
        self.oneButton.setIcon(oneButtonIcon)
        self.hBoxLayout.insertWidget(3, self.oneButton, 0, Qt.AlignmentFlag.AlignRight)


# 展开卡片
class ExpandButtonCard(ExpandGroupSettingCard):
    def __init__(self, icon, title, content, parent=None):
        super().__init__(icon, title, content, parent)
        self.card.setFixedHeight(80)
        self.setFixedHeight(self.card.height())
        self.viewLayout.setContentsMargins(0, self.card.height(), 0, 0)
        self.viewLayout.setSpacing(0)

    def addButton(self, labelText, buttonText, label=CaptionLabel, button=PushButton):
        layout = self.initLayout()

        label = label(labelText, self)
        button = button(self)
        button.setText(buttonText)
        button.setFixedWidth(120)

        layout.addWidget(label)
        layout.addStretch(1)
        layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignRight)

        return button

    def addComboBox(self, labelText, items: list[str], label=CaptionLabel, comboBox=ComboBox):
        layout = self.initLayout()

        label = label(labelText, self)
        combox = comboBox(self)
        combox.addItems(items)
        combox.setFixedWidth(120)

        layout.addWidget(label)
        layout.addStretch(1)
        layout.addWidget(combox, alignment=Qt.AlignmentFlag.AlignRight)

        return combox

    def addSwitchButton(self, labelText, default: bool = False, label=CaptionLabel):
        layout = self.initLayout()

        label = label(labelText, self)
        switchButton = SwitchButton(self)
        switchButton.setChecked(default)
        switchButton.setText('开') if default else switchButton.setText('关')
        switchButton._offText = '关'
        switchButton._onText = '开'

        layout.addWidget(label)
        layout.addStretch(1)
        layout.addWidget(switchButton, alignment=Qt.AlignmentFlag.AlignRight)

        return switchButton

    def addRangeButton(self, labelText, range: tuple, defaultValue, label=CaptionLabel, position=Qt.Horizontal):
        layout = self.initLayout()

        label = label(labelText, self)
        slider = Slider(position)
        slider.setRange(range[0], range[1])
        slider.setValue(defaultValue)
        slider.setFixedWidth(250)
        valueLabel = CaptionLabel(str(slider.value()), self)

        layout.addWidget(label)
        layout.addStretch(1)
        layout.addWidget(valueLabel, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addWidget(slider, alignment=Qt.AlignmentFlag.AlignRight)

        slider.valueChanged.connect(
            lambda: valueLabel.setText(str(slider.value()))
        )

        return slider

    def initLayout(self):
        window = QWidget(self)
        window.setFixedHeight(60)
        layout = QHBoxLayout(window)
        layout.setContentsMargins(48, 12, 48, 12)
        self.addGroupWidget(window)

        return layout