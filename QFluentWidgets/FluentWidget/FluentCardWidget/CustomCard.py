from typing import Union

from PySide6.QtGui import Qt, QIcon
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget
from qfluentwidgets import CardWidget, IconWidget, BodyLabel, CaptionLabel, PushButton, \
    FluentIconBase, ToolButton, SwitchButton, HyperlinkButton, Action, ExpandGroupSettingCard
from qfluentwidgets.components.material import AcrylicMenu


class CustomCard(CardWidget):
    def __init__(self, icon: Union[QIcon, str, FluentIconBase, None], title: str, content: str, parent: QWidget = None):
        super().__init__(parent)
        self.iconWidget = IconWidget(icon)
        self.titleLabel = BodyLabel(title, self)
        self.contentLabel = CaptionLabel(content, self)
        self.hBoxLayout = QHBoxLayout(self)
        self.vBoxLayout = QVBoxLayout()

        self.setFixedHeight(80)
        self.iconWidget.setFixedSize(24, 24)
        self.contentLabel.setTextColor("#606060", "#d2d2d2")

        self.hBoxLayout.setContentsMargins(20, 11, 48, 11) # left top right bottom
        self.hBoxLayout.setSpacing(15)
        self.hBoxLayout.addWidget(self.iconWidget)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.addWidget(self.titleLabel, 0, Qt.AlignmentFlag.AlignVCenter)
        self.vBoxLayout.addWidget(self.contentLabel, 0, Qt.AlignmentFlag.AlignVCenter)
        self.vBoxLayout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.hBoxLayout.addLayout(self.vBoxLayout)

        self.hBoxLayout.addStretch(1)


class CustomButtonCard(CustomCard):
    def __init__(
            self, icon, title, content, buttonText: str = None, buttonIcon: Union[QIcon, str, FluentIconBase] = None,
            parent=None, __type: Union[type[PushButton], type[ToolButton], type[HyperlinkButton], type[QWidget]] = None
    ):
        super().__init__(icon, title, content, parent)
        self.button = __type(self)
        self.button.setFixedWidth(120)
        self.setButtonText(buttonText)
        self.setButtonIcon(buttonIcon)
        self.hBoxLayout.addWidget(self.button, 0, Qt.AlignmentFlag.AlignRight)

    def setButtonText(self, text: str):
        self.button.setText(text)

    def setButtonIcon(self, icon: Union[QIcon, str, FluentIconBase]):
        self.button.setIcon(icon)


class CustomToolCard(CustomCard):
    def __init__(
            self, icon, title, content, buttonIcon: Union[QIcon, str, FluentIconBase] = None,
            parent=None, __type: Union[type[PushButton], type[ToolButton], type[QWidget]] = None
    ):
        super().__init__(icon, title, content, parent)
        self.button = __type(self)
        self.setButtonIcon(buttonIcon)
        self.hBoxLayout.addWidget(self.button, 0, Qt.AlignmentFlag.AlignRight)

    def setButtonText(self, text: str):
        self.button.setText(text)

    def setButtonIcon(self, icon: Union[QIcon, str, FluentIconBase]):
        self.button.setIcon(icon)


class CustomSwitchButtonCard(CustomCard):
    def __init__(self, icon, title, content, status: bool = False, parent=None):
        super().__init__(icon, title, content, parent)
        self.switchButton = SwitchButton(self)
        self.initSwitchButton(status)
        self.hBoxLayout.addWidget(self.switchButton, 0, Qt.AlignmentFlag.AlignRight)

    def initSwitchButton(self, status: bool):
        self.switchButton._onText = '开'
        self.switchButton._offText = '关'
        self.switchButton.setChecked(status)
        self.switchButton.setFixedWidth(120)
        self.hBoxLayout.setContentsMargins(20, 11, 0, 11)


class CustomDropDownCard(CustomToolCard):

    def __init__(
            self, icon, title, content, buttonText: str = None, buttonIcon=None, menuTexts: list[str] = None,
            menuIcons: list[Union[QIcon, str, FluentIconBase]] = None, triggered: list = None, parent=None, __type=None
    ):
        super().__init__(icon, title, content, buttonIcon, parent, __type)
        self.addMenu(menuIcons, menuTexts, triggered)

    def addMenu(self, icons: list[Union[QIcon, str, FluentIconBase]], texts: list, triggered: list):
        self.menu = AcrylicMenu(self.button)
        if texts:
            if icons:
                for icon, text in zip(icons, texts):
                    self.menu.addAction(Action(icon, text, triggered=triggered[texts.index(text)] if triggered else None))
            else:
                for text in texts:
                    self.menu.addAction(Action(text, triggered=triggered[texts.index(text)] if triggered else None))


class ExpandGroupCard(ExpandGroupSettingCard):
    def __init__(self, icon, title, content, parent=None):
        super().__init__(icon, title, content, parent)
        self.card.setContentsMargins(0, 0, 20, 0)
        self.viewLayout.setSpacing(0)
        self.setCardMinHeight(80)

    def setCardMinHeight(self, height: int):
        self.card.setFixedHeight(height)

    def addGroupWidgets(self, widgets: list[QWidget]):
        for widget in widgets:
            self.addGroupWidget(widget)

    def addButtonCard(self, title: str, icon: Union[QIcon, str, FluentIconBase], text: str, __type: Union[type[PushButton], type[ToolButton]] = None):
        pass

    def addPrimaryButtonCard(self, title: str, icon: Union[QIcon, str, FluentIconBase], text: str):
        pass

    def addTransparentButtonCard(self, title: str, icon: Union[QIcon, str, FluentIconBase], text: str):
        pass

    def addSliderCard(self, title: str, ranges: tuple[int, int], defaultValue: int, orientation: Qt.Orientation = Qt.Orientation.Horizontal):
        pass

    def _initWidget(self):
        window = QWidget()
        window.setFixedHeight(65)
        hLayout = QHBoxLayout(window)
        hLayout.setContentsMargins(48, 12, 48, 12)
        self.addGroupWidget(window)

        return hLayout

#
#
# # 下拉框按钮
# class ComboxButtonCard(__ButtonCard):
#     def __init__(self, icon, title, content, items: list[str], buttonText, noSelected: bool = False, info=None, parent=None, comboBox=ComboBox):
#         super().__init__(icon, title, content, buttonText, parent, PrimaryPushButton)
#         self.combox = comboBox(self)
#         self.combox.setFixedWidth(120)
#         self.combox.addItems(items)
#         if noSelected:
#             self.combox.setCurrentIndex(-1)
#             self.combox.setPlaceholderText(info)
#
#         self.hBoxLayout.insertWidget(3, self.combox, 0, Qt.AlignmentFlag.AlignRight)
#
#
# # 可编辑下拉框按钮
# class EditComboBoxButtonCard(ComboxButtonCard):
#     def __init__(self, icon, title, content, items: list[str], buttonText, noSelected: bool = False, info=None, parent=None):
#         super().__init__(icon, title, content, items, buttonText, noSelected, info, parent, EditableComboBox)
#
#
# # 双按钮卡片
# class TwoButtonCard(__ButtonCard):
#     def __init__(self, icon, title, content, oneButtonText=None, oneButtonIcon=None, buttonText=None, parent=None, button=PushButton):
#         super().__init__(icon, title, content, buttonText, parent, PrimaryPushButton)
#         self.oneButton = button(self)
#         self.oneButton.setText(oneButtonText)
#         self.oneButton.setIcon(oneButtonIcon)
#         self.hBoxLayout.insertWidget(3, self.oneButton, 0, Qt.AlignmentFlag.AlignRight)
#
#
# # 展开卡片
# class ExpandButtonCard(ExpandGroupSettingCard):
#     def __init__(self, icon, title, content, parent=None):
#         super().__init__(icon, title, content, parent)
#         self.viewLayout.setContentsMargins(0, 0, 0, 0)
#         self.viewLayout.setSpacing(0)
#
#     def addButton(self, labelText, buttonText, label=CaptionLabel, button=PushButton):
#         window, layout = self.initLayout()
#
#         label = label(labelText, self)
#         button = button(self)
#         button.setText(buttonText)
#         button.setFixedWidth(120)
#
#         layout.addWidget(label)
#         layout.addStretch(1)
#         layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignRight)
#
#         return button
#
#     def addComboBox(self, labelText, items: list[str], label=CaptionLabel, comboBox=ComboBox):
#         window, layout = self.initLayout()
#
#         label = label(labelText, self)
#         combox = comboBox(self)
#         combox.addItems(items)
#         combox.setFixedWidth(120)
#
#         layout.addWidget(label)
#         layout.addStretch(1)
#         layout.addWidget(combox, alignment=Qt.AlignmentFlag.AlignRight)
#
#         return combox
#
#     def addSwitchButton(self, labelText, default: bool = False, label=CaptionLabel):
#         window, layout = self.initLayout()
#
#         label = label(labelText, self)
#         switchButton = SwitchButton(self)
#         switchButton.setChecked(default)
#         switchButton.setText('开') if default else switchButton.setText('关')
#         switchButton._offText = '关'
#         switchButton._onText = '开'
#
#         layout.addWidget(label)
#         layout.addStretch(1)
#         layout.addWidget(switchButton, alignment=Qt.AlignmentFlag.AlignRight)
#
#         return switchButton
#
#     def addRangeButton(self, labelText, range: tuple, defaultValue, label=CaptionLabel, position=Qt.Horizontal):
#         window, layout = self.initLayout()
#
#         label = label(labelText, self)
#         slider = Slider(position)
#         slider.setRange(range[0], range[1])
#         slider.setValue(defaultValue)
#         slider.setFixedWidth(250)
#         valueLabel = CaptionLabel(str(slider.value()), self)
#
#         layout.addWidget(label)
#         layout.addStretch(1)
#         layout.addWidget(valueLabel, alignment=Qt.AlignmentFlag.AlignRight)
#         layout.addWidget(slider, alignment=Qt.AlignmentFlag.AlignRight)
#
#         slider.valueChanged.connect(
#             lambda: valueLabel.setText(str(slider.value()))
#         )
#
#         return slider
#
#     def initLayout(self):
#         window = QWidget(self)
#         window.setFixedHeight(60)
#         layout = QHBoxLayout(window)
#         layout.setContentsMargins(48, 12, 48, 12)
#         self.addGroupWidget(window)
#
#         return window, layout