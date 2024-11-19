from typing import Union

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget
from qfluentwidgets import CardWidget, FluentIconBase


class CustomCardParent(CardWidget):
    # noinspection PyUnusedLocal
    def __init__(
            self,
            icon: Union[QIcon, str, FluentIconBase, None] = None,
            title: str = None,
            content: str = None,
            parent: QWidget = None
    ):
        super().__init__(parent)
        self.hBoxLayout = None
        self.VBoxLayout = None
        self.iconWidget = None
        self.titleLabel = None
        self.contentLabel = None
        self.button = None
        self.comboBox = None
        self.comboBox = None
        self.noSelected = False
        self.slider = None
        self.sliderLabel = None

    def initLayout(self) -> 'CustomCardParent':
        pass

    def initIcon(self, icon: Union[QIcon, str, FluentIconBase, QWidget]) -> 'CustomCardParent':
        pass

    def initTitle(self, title: str) -> 'CustomCardParent':
        pass

    def initContent(self, content: str) -> 'CustomCardParent':
        pass