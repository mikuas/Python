from typing import Union

from PySide6.QtGui import Qt, QIcon
from PySide6.QtWidgets import QWidget
from qfluentwidgets import ComboBox, EditableComboBox, FluentIconBase


class CustomComboBoxCard:
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
