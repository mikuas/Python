from typing import Union

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget
from qfluentwidgets import ComboBox, EditableComboBox, FluentIconBase, OptionsConfigItem, ConfigItem


class CustomComboBoxCard:
    # noinspection PyUnusedLocal
    def __init__(
            self,
            icon: Union[QIcon, str, FluentIconBase] = None,
            title: str = None,
            content: str = None,
            items: list[str] = None,
            noSelected: bool = False,
            info: str = None,
            parent: QWidget = None,
            boxType: Union[type[ComboBox], type[EditableComboBox]] = None
    ):
        pass

    def initComboBox(self, boxType: Union[type[ComboBox], type[EditableComboBox]], items: list[str]) -> 'CustomComboBoxCard':
        pass

    def setPlaceholderText(self, text: str) -> 'CustomComboBoxCard':
        pass

    def isNoSelected(self) -> bool:
        pass


class CustomOptionsCard:
    # noinspection PyUnusedLocal
    def __init__(
            self,
            icon: Union[QIcon, str, FluentIconBase] = None,
            title: str = None,
            content: str = None,
            items: list[str] = None,
            defaultValue: str = None,
            parent: QWidget = None
    ):
        pass

    @staticmethod
    def __initOptItems(value: str, items: list) -> 'OptionsConfigItem':
        pass

    def __initConfItems(self, value: str) -> ConfigItem:
        pass

    def setOptionsFixedHeight(self, height: int, parent):
        pass