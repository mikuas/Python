from typing import Union

from PySide6.QtGui import Qt, QIcon
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QWidget
from qfluentwidgets import PushButton, FluentIconBase, ToolButton, HyperlinkButton, SplitWidgetBase, FolderListValidator


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
    ):
        pass

    def insertWidget(self, index: int, widget: QWidget, stretch: int, alignment: Qt.AlignmentFlag):
        pass

    def setButtonText(self, text: str):
        pass

    def setButtonIcon(self, icon: Union[QIcon, str, FluentIconBase]):
        pass

    def setButtonIconSize(self, width: int, height: int):
        pass

    def setButtonFixedWidth(self, width: int):
        pass

    def setButtonFixedHeight(self, height: int):
        pass

    def setButtonFixedSize(self, width: int, height: int):
        pass

    def setButtonChecked(self, isChecked: bool = False):
        pass

    def setUrl(self, url: QUrl | str):
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