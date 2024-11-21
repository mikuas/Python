from typing import Union

from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout
from qfluentwidgets import ExpandGroupSettingCard, FluentIconBase, PushButton, ToolButton


class CustomExpandGroupCard(ExpandGroupSettingCard):
    def __init__(self, icon: Union[QIcon, str, FluentIconBase], title, content, parent=None):
        super().__init__(icon, title, content, parent)

    def __initButton(
            self,
            title: str,
            icon: Union[QIcon, str, FluentIconBase],
            text: str,
            parent: QWidget = None,
            btType: Union[type[PushButton], type[ToolButton]] = None
    ):
        pass

    def setExpandFixedHeight(self, height: int) -> 'CustomExpandGroupCard':
        pass

    def addGroupWidgets(self, widgets: list[QWidget]) -> 'CustomExpandGroupCard':
        pass

    def setIconSize(self, width: int, height: int) -> 'CustomExpandGroupCard':
        pass

    def addButtonCard(self, title: str, icon: Union[QIcon, str, FluentIconBase], text: str, parent: QWidget = None):
        pass

    def addPrimaryButtonCard(self, title: str, icon: Union[QIcon, str, FluentIconBase], text: str, parent: QWidget = None):
        pass

    def addTransparentButtonCard(self,  title: str, icon: Union[QIcon, str, FluentIconBase], text: str, parent: QWidget = None):
        pass

    def addSliderCard(
            self,
            title: str,
            ranges: tuple[int, int],
            defaultValue: int,
            orientation: Qt.Orientation = Qt.Orientation.Horizontal,
            parent: QWidget = None
    ):
        pass

    def _initWidget(self) -> QHBoxLayout:
        pass