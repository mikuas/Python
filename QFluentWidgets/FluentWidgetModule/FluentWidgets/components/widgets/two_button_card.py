# coding:utf-8
from PySide6.QtCore import Qt

from qfluentwidgets import TransparentToolButton, FluentIcon, PushButton, PrimaryPushButton, TransparentPushButton

from .button_card import ButtonCardBase


class MoreButtonCardBase(ButtonCardBase):
    def __init__(self, icon, title, content, btText=None, btIcon=None, parent=None):
        super().__init__(icon, title, content, parent, btText, btIcon)
        self.hBoxLayout.setContentsMargins(20, 11, 25, 11)

    def _initMoreButton(self):
        self.moreButton = TransparentToolButton(FluentIcon.MORE, self)
        self.hBoxLayout.addWidget(self.moreButton, 0, Qt.AlignmentFlag.AlignRight)


class MoreButtonCard(MoreButtonCardBase):
    """ 带更多按钮的普通按钮 """
    def __init__(self, icon, title, content, btText=None, btIcon=None, parent=None):
        super().__init__(icon, title, content, parent, btText, btIcon)
        self.button = PushButton(self)
        self.setButtonText(btText).setButtonIcon(btIcon).initButton().setButtonMinWidth(120)
        self._initMoreButton()


class MorePrimaryButtonCard(MoreButtonCardBase):
    """ 带更多按钮的主题色普通按钮 """
    def __init__(self, icon, title, content, btText=None, btIcon=None, parent=None):
        super().__init__(icon, title, content, btText, btIcon, parent)
        self.button = PrimaryPushButton(self)
        self.setButtonText(btText).setButtonIcon(btIcon).initButton().setButtonMinWidth(120)
        self._initMoreButton()


class MoreTransparentButtonCard(MoreButtonCardBase):
    """ 带更多按钮的透明普通按钮 """
    def __init__(self, icon, title, content, btText=None, btIcon=None, parent=None):
        super().__init__(icon, title, content, btText, btIcon, parent)
        self.button = TransparentPushButton(self)
        self.setButtonText(btText).setButtonIcon(btIcon).initButton().setButtonMinWidth(120)
        self._initMoreButton()
