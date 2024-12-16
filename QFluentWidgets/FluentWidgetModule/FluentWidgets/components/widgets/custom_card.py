# coding:utf-8
from typing import Union

from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QWidget
from qfluentwidgets import CardWidget, FluentIconBase, IconWidget, BodyLabel, CaptionLabel, CustomColorSettingCard, \
    FluentIcon, themeColor, ColorConfigItem, setThemeColor

from ..layout import HBoxLayout, VBoxLayout


class CardBase(CardWidget):
    """ 卡片基类 """
    # noinspection PyUnusedLocal
    def __init__(
            self,
            icon: Union[QIcon, str, FluentIconBase, None] = None,
            title: str = None,
            content: str = None,
            parent: QWidget = None
    ):
        super().__init__(parent)
        self.setFixedHeight(70)

    def initLayout(self):
        self.hBoxLayout = HBoxLayout(self)
        self.vBoxLayout = VBoxLayout()

        self.hBoxLayout.setContentsMargins(20, 11, 48, 11) # left top right bottom
        self.hBoxLayout.setSpacing(15)
        self.hBoxLayout.addWidget(self.iconWidget)
        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.addWidget(self.titleLabel, 0, Qt.AlignVCenter)
        self.vBoxLayout.addWidget(self.contentLabel, 0, Qt.AlignVCenter)
        self.vBoxLayout.setAlignment(Qt.AlignVCenter)
        self.hBoxLayout.addLayout(self.vBoxLayout)
        self.hBoxLayout.addStretch(1)
        return self

    def initIcon(self, icon):
        """ set card icon """
        self.iconWidget = IconWidget(icon)
        self.iconWidget.setFixedSize(24, 24)
        return self

    def initTitle(self, title):
        """ set card title """
        self.titleLabel = BodyLabel(title, self)
        return self

    def initContent(self, content):
        """ set card content """
        self.contentLabel = CaptionLabel(content, self)
        # self.contentLabel.setTextColor("#606060", "#d2d2d2")
        return self


class ColorSelectCard(CustomColorSettingCard):
    """ 主题颜色选择卡 """
    def __init__(self, title, content, parent=None, icon=FluentIcon.PALETTE, enableAlpha=False):
        super().__init__(
            ColorConfigItem("Color", "select", themeColor()),
            icon, title, content, parent, enableAlpha
        )
        self.__initCard()

    def __initCard(self):
        self.chooseColorButton.setText("选择")
        self.defaultRadioButton.setText("默认颜色")
        self.customRadioButton.setText("自定义颜色")
        self.choiceLabel.setText('默认颜色')
        self.customLabel.setText('选择颜色')
        self.colorChanged.connect(lambda color: setThemeColor(color))

    def setCardFixedHeight(self, height: int):
        self.card.setFixedHeight(height)
        self.setFixedHeight(self.card.height())
        self.setViewportMargins(0, self.card.height(), 0, 0)