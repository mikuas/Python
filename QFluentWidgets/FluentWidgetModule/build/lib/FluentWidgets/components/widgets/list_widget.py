# coding:utf-8
from typing import Union

from PySide6.QtCore import QSize
from PySide6.QtGui import Qt, QIcon
from PySide6.QtWidgets import QWidget, QListWidgetItem
from qfluentwidgets import ListWidget as List, FluentIcon, Icon, FluentIconBase


class ListWidget(List):
    """ 列表组件 """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)

    def addIconItems(
            self,
            icons: list[Union[QIcon, str, FluentIconBase, FluentIcon]],
            items: list[str],
            itemHeight=45,
            alignFlag=Qt.AlignmentFlag.AlignVertical_Mask
    ) -> list[QListWidgetItem]:
        listItem = []
        for icon, item in zip(icons, items):
            item = QListWidgetItem(item)
            if type(icon) is not str:
                item.setIcon(Icon(icon))
            else:
                item.setIcon(QIcon(icon))
            item.setTextAlignment(alignFlag)
            item.setSizeHint(QSize(self.width(), itemHeight))
            self.addItem(item)
            listItem.append(item)
        return listItem

    def addItems(self, items: list[str], itemHeight=45, alignFlag=Qt.AlignmentFlag.AlignVertical_Mask) -> list[QListWidgetItem]:
        listItem = []
        for item in items:
            item = QListWidgetItem(item)
            item.setTextAlignment(alignFlag)
            item.setSizeHint(QSize(self.width(), itemHeight))
            self.addItem(item)
            listItem.append(item)
        return listItem