from PySide6.QtCore import Qt

from qfluentwidgets import TransparentToolButton, FluentIcon, PushButton, PrimaryPushButton, TransparentPushButton

from .button_card import CustomButtonCard


class MoreButtonCard(CustomButtonCard):
    """ 带更多按钮的普通按钮 """
    def __init__(self, icon, title, content, btText=None, btIcon=None, parent=None, btType=PushButton):
        super().__init__(icon, title, content, parent, btType, btText, btIcon)
        self.setButtonFixedWidth(120).setButtonText(btText).setButtonIcon(btIcon)
        self.__initMoreButton()

    def __initMoreButton(self):
        self.moreButton = TransparentToolButton(FluentIcon.MORE, self)
        self.hBoxLayout.addWidget(self.moreButton, 0, Qt.AlignmentFlag.AlignRight)


class MorePrimaryButtonCard(MoreButtonCard):
    """ 带更多按钮的主题色普通按钮 """
    def __init__(self, icon, title, content, btText=None, btIcon=None, parent=None):
        super().__init__(icon, title, content, btText, btIcon, parent, PrimaryPushButton)


class MoreTransparentButtonCard(MoreButtonCard):
    """ 带更多按钮的透明普通按钮 """
    def __init__(self, icon, title, content, btText=None, btIcon=None, parent=None):
        super().__init__(icon, title, content, btText, btIcon, parent, TransparentPushButton)

