from typing import Union

from PySide6.QtGui import Qt, QIcon
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QHBoxLayout, QWidget
from qfluentwidgets import PushButton, FluentIconBase, ToolButton, HyperlinkButton, \
     SplitWidgetBase


class CustomButtonCardParent:
    # noinspection PyUnusedLocal
    def __init__(
            self,
            icon: Union[QIcon, str, FluentIconBase] = None,
            title: str = None,
            content: str = None,
            btText: str = None,
            btIcon: Union[QIcon, str, FluentIconBase] = None,
            parent: QWidget = None,
            btType: Union[type[PushButton], type[ToolButton], type[HyperlinkButton], type[QWidget], type[SplitWidgetBase]] = None
    ):
        pass

    def initButton(
            self,
            btType: Union[
                type[PushButton],
                type[ToolButton],
                type[HyperlinkButton],
                type[QWidget],
                type[SplitWidgetBase]
            ]
    ) -> 'CustomButtonCardParent':
        pass

    def setButtonText(self, text: str) -> 'CustomButtonCardParent':
        pass

    def setButtonIcon(self, icon: Union[QIcon, str, FluentIconBase]) -> 'CustomButtonCardParent':
        pass

    def setButtonFW(self, width: int) -> 'CustomButtonCardParent':
        pass

    def setButtonChecked(self, isChecked: bool = False) -> 'CustomButtonCardParent':
        pass

    def setUrl(self, url: QUrl | str) -> 'CustomButtonCardParent':
        pass


class CustomSwitchButtonCard:
    # noinspection PyUnusedLocal
    def __init__(
            self,
            icon: Union[QIcon, str, FluentIconBase] = None,
            title: str = None,
            content: str = None,
            isChecked: bool = False,
            parent: QWidget = None
    ):
        self.switchButton = None


class CustomCheckBoxCard:
    # noinspection PyUnusedLocal
    def __init__(
            self,
            icon: Union[QIcon, str, FluentIconBase] = None,
            title: str = None,
            content: str = None,
            isChecked: bool = False,
            boxText: str = None,
            boxIcon: Union[QIcon, str, FluentIconBase] = None,
            parent: QWidget = None
    ):
        pass


class SliderCardParent:
    # noinspection PyUnusedLocal
    def __init__(
            self,
            icon: Union[QIcon, str, FluentIconBase] = None,
            title: str = None,
            content: str = None,
            ranges: tuple[int | float, int | float] = None,
            defaultValue: int | float = 0, orientation: Qt.Orientation = Qt.Orientation.Horizontal,
            parent: QWidget = None
    ):
        pass

    def initSlider(self, ranges: tuple[int, int], value: int | float, orientation: Qt.Orientation = Qt.Orientation.Horizontal):
        pass

    def initSliderLabel(self, value: str | int | float):
        pass


class CustomDropDownCard:
    # noinspection PyUnusedLocal
    def __init__(
            self,
            icon: Union[QIcon, str, FluentIconBase] = None,
            title: str = None,
            content: str = None,
            btText: str = None,
            btIcon: Union[QIcon, str, FluentIconBase] = None,
            menuTexts: list[str] = None,
            menuIcons: list[Union[QIcon, str, FluentIconBase]] = None,
            triggered: list = None,
            parent: QWidget = None,
            btType: Union[type[PushButton], type[ToolButton], type[SplitWidgetBase]] = None
    ):
        self.menu = None

    def addMenu(self, texts: list, icons: list[Union[QIcon, str, FluentIconBase]], triggered: list):
        pass