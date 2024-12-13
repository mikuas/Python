from typing import Union

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QListWidgetItem
from qfluentwidgets import TableWidget as Table, ListWidget as List, FluentIcon, Icon, FluentIconBase


class TableWidget(Table):
    """ 表格组件 """

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.__initTable()
        self.setSelectRightClickedRow(True)
        # lambda value: print(self.model().data(value))

    def __initTable(self):
        self.setBorderVisible(True)
        self.setBorderRadius(8)
        self.setWordWrap(False)

    def setRowColumn(self, row: int, column: int):
        self.setRowCount(row)
        self.setColumnCount(column)
        return self

    def addTableData(self, table: list[list[str]]):
        self.setRowColumn(len(table), 1)
        for i, item in enumerate(table):
            for j in range(len(item)):
                self.setItem(i, j, QTableWidgetItem(item[j]))
        return self

    def addTabWidget(self, table: list[list[QWidget]]):
        self.setRowColumn(len(table), 1)
        for i, item in enumerate(table):
            for j in range(len(item)):
                self.setCellWidget(i, j, item[j])

    def setHorizontalTitle(self, title: list[str]):
        self.setHorizontalHeaderLabels(title)
        self.verticalHeader().hide()
        return self

    def setVerticalTitle(self, title: list[str]):
        self.setVerticalHeaderLabels(title)
        self.horizontalHeader().hide()
        return self

    def setAllTitle(self, horTitle: list[str], vertTitle: list[str]):
        self.setHorizontalHeaderLabels(horTitle)
        self.setVerticalHeaderLabels(vertTitle)
        return self

    def setItemMinWidth(self, width: int):
        self.horizontalHeader().setDefaultSectionSize(width)
        return self

    def setItemMinHeight(self, height: int):
        self.verticalHeader().setDefaultSectionSize(height)
        return self


class ListWidget(List):
    """ 列表组件 """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)

    def addIconItems(
            self,
            icons: list[Union[QIcon, str, FluentIconBase, FluentIcon]],
            items: list[str],
            itemHeight: int = 45,
            alignFlag: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignVertical_Mask
    ):
        listItem = []
        for icon, item in zip(icons, items):
            item = QListWidgetItem(item)
            # if isinstance(icon, FluentIcon) or isinstance(icon, FluentLabelBase):
            if type(icon) is not str:
                item.setIcon(Icon(icon))
            else:
                item.setIcon(QIcon(icon))
            item.setTextAlignment(alignFlag)
            item.setSizeHint(QSize(self.width(), itemHeight))
            self.addItem(item)
            listItem.append(item)
        return listItem

    def addItems(self, items: list[str], itemHeight: int = 45, alignFlag: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignVertical_Mask):
        listItem = []
        for item in items:
            item = QListWidgetItem(item)
            item.setTextAlignment(alignFlag)
            item.setSizeHint(QSize(self.width(), itemHeight))
            self.addItem(item)
            listItem.append(item)
        return listItem
