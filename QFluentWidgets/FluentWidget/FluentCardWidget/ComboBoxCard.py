from typing import Union

from PySide6.QtGui import Qt
from qfluentwidgets import ComboBox, EditableComboBox

from QFluentWidgets.FluentWidget.FluentCardWidget.CustomCard import CustomCard


class CustomComboBoxCard(CustomCard):
    def __init__(
            self,
            icon,
            title,
            content,
            items: list[str],
            noSelected: bool = False,
            info: str = None,
            parent=None,
            __type: Union[type[ComboBox], type[EditableComboBox]] = None
    ):
        super().__init__(icon, title, content, parent)
        self.comboBox = __type(self)
        self.initComboBox(items)
        self.setPlaceholderText(noSelected, info)
        self.hBoxLayout.addWidget(self.comboBox, 0, Qt.AlignmentFlag.AlignRight)

    def initComboBox(self, items: list[str]):
        self.comboBox.addItems(items)
        self.comboBox.setFixedWidth(150)

    def setPlaceholderText(self, b: bool, text: str):
        if b:
            self.comboBox.setPlaceholderText(text)
            self.comboBox.setCurrentIndex(-1)