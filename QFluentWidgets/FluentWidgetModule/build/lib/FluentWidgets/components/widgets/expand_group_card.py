# coding:utf-8
from typing import Union

from PySide6.QtGui import Qt, QIcon
from PySide6.QtWidgets import QWidget, QHBoxLayout
from qfluentwidgets import TitleLabel, PushButton, PrimaryPushButton, TransparentPushButton, Slider, CaptionLabel, \
    FluentIconBase, ExpandGroupSettingCard, ToolButton


class ExpandGroupCard(ExpandGroupSettingCard):
    """ 展开按钮卡片 """
    def __init__(self, icon, title, content, parent=None):
        super().__init__(icon, title, content, parent)
        self.card.setContentsMargins(0, 0, 20, 0)
        self.viewLayout.setSpacing(0)
        self.setExpandFixedHeight(70).setIconSize(24, 24)

    def setExpandFixedHeight(self, height: int):
        """ set expandCard fixed height"""
        self.card.setFixedHeight(height)
        self.setFixedHeight(self.card.height())
        self.setViewportMargins(0, self.card.height(), 0, 0)
        return self

    def addGroupWidgets(self, widgets: list[QWidget]):
        for widget in widgets:
            self.addGroupWidget(widget)
        return self

    def setIconSize(self, width: int, height: int):
        self.card.setIconSize(width, height)
        return self

    def __initButton(
            self, title: str, icon: Union[QIcon, str, FluentIconBase], text: str,
            parent: QWidget = None, btType: Union[type[PushButton], type[ToolButton]] = None
    ):
        hLayout = self._initWidget()
        hLayout.addWidget(TitleLabel(title, parent))
        button = btType(icon, text, parent)
        button.setFixedWidth(120)
        hLayout.addStretch(1)
        hLayout.addWidget(button, 0, Qt.AlignmentFlag.AlignRight)
        return button

    def addButtonCard(self, title: str, icon: Union[QIcon, str, FluentIconBase], text: str, parent: QWidget= None):
        return self.__initButton(title, icon, text, parent, PushButton)

    def addPrimaryButtonCard(self, title: str, icon: Union[QIcon, str, FluentIconBase], text: str, parent: QWidget = None):
        return self.__initButton(title, icon, text, parent, PrimaryPushButton)

    def addTransparentButtonCard(self, title: str, icon: Union[QIcon, str, FluentIconBase], text: str, parent: QWidget = None):
        return self.__initButton(title, icon, text, parent, TransparentPushButton)

    def addSliderCard(self, title: str, minValue: int, maxValue: int, defaultValue: int, orientation=Qt.Orientation.Horizontal, parent: QWidget = None):
        slider = Slider(orientation, parent)
        slider.setRange(minValue, maxValue)
        slider.setValue(defaultValue)
        slider.setFixedWidth(250)
        label = CaptionLabel(str(slider.value()), parent)

        hLayout = self._initWidget()
        hLayout.addWidget(TitleLabel(title, parent))
        hLayout.addStretch(1)
        hLayout.addWidget(label, 0, Qt.AlignmentFlag.AlignRight)
        hLayout.addWidget(slider, 0, Qt.AlignmentFlag.AlignRight)
        slider.valueChanged.connect(lambda: label.setText(str(slider.value())))
        return slider

    def addCustomWidget(self, widget: QWidget, stretch: int = 0, alignment: Qt.AlignmentFlag = Qt.AlignmentFlag(0)):
        hLayout = self._initWidget()
        hLayout.addWidget(widget, stretch, alignment)
        return hLayout

    def _initWidget(self):
        window = QWidget()
        window.setFixedHeight(50)
        hLayout = QHBoxLayout(window)
        hLayout.setContentsMargins(48, 0, 48, 0)
        self.addGroupWidget(window)
        return hLayout