from typing import Union

from PySide6.QtGui import Qt, QIcon
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QHBoxLayout, QWidget
from qfluentwidgets import CardWidget, PushButton, FluentIconBase, ToolButton, HyperlinkButton, \
    ExpandGroupSettingCard, SplitWidgetBase


class CustomCardParent(CardWidget):
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


class CustomButtonCardParent:
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

    def initButton(self, btType: Union[type[PushButton], type[ToolButton], type[HyperlinkButton], type[QWidget], type[SplitWidgetBase]]) -> 'CustomButtonCardParent':
        pass

    def setButtonText(self, text: str) -> 'CustomButtonCardParent':
        pass

    def setButtonIcon(self, icon: Union[QIcon, str, FluentIconBase]) -> 'CustomButtonCardParent':
        pass

    def setButtonChecked(self, isChecked: bool = False) -> 'CustomButtonCardParent':
        pass

    def setUrl(self, url: QUrl | str) -> 'CustomButtonCardParent':
        pass


class CustomSwitchButtonCard:
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



class CustomDropDownCard:

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


class SliderCardParent:
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

    def initSlider(self, ranges: tuple[int, int], value: int | float,orientation: Qt.Orientation = Qt.Orientation.Horizontal):
        pass

    def initSliderLabel(self, value: str | int | float):
        pass


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