from PySide6.QtGui import Qt
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout
from qfluentwidgets import IconWidget, BodyLabel, CaptionLabel, CustomColorSettingCard, ColorConfigItem, themeColor, \
    FluentIcon, setThemeColor

from ...widgetdoc import CustomCardParent


class CustomCard(CustomCardParent):
    # noinspection PyUnusedLocal
    def __init__(self, icon=None, title=None, content=None, parent=None):
        super().__init__(parent=parent)
        self.setFixedHeight(70)

    def initLayout(self):
        self.hBoxLayout = QHBoxLayout(self)
        self.vBoxLayout = QVBoxLayout()

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
        return self

    def initIcon(self, icon):
        # set card icon
        self.iconWidget = IconWidget(icon)
        self.iconWidget.setFixedSize(32, 32)
        return self

    def initTitle(self, title):
        # set card title
        self.titleLabel = BodyLabel(title, self)
        return self

    def initContent(self, content):
        # set card content
        self.contentLabel = CaptionLabel(content, self)
        # self.contentLabel.setTextColor("#606060", "#d2d2d2")
        return self
    

class CustomColorCard(CustomColorSettingCard):
    """ 自定义颜色选择卡 """
    def __init__(self, title, content, parent=None, icon=FluentIcon.PALETTE, enableAlpha=False):
        super().__init__(ColorConfigItem("Color", "select", themeColor()), icon, title, content, parent, enableAlpha)
        self.__initCard()

    def __initCard(self):
        self.chooseColorButton.setText("选择")
        self.defaultRadioButton.setText("默认颜色")
        self.customRadioButton.setText("自定义颜色")
        self.choiceLabel.setText('默认颜色')
        self.customLabel.setText('选择颜色')
        self.colorChanged.connect(lambda color: setThemeColor(color))