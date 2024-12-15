# coding:utf-8
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QTableWidget
from qfluentwidgets import TableWidget as Table


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

    def disableEdit(self):
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        return self

    def addTableData(self, table: list[list[str]]):
        self.setRowColumn(len(table), len(table[0]))
        for i, item in enumerate(table):
            for j in range(len(item)):
                self.setItem(i, j, QTableWidgetItem(item[j]))
        return self

    def addTabWidget(self, table: list[list[QWidget]]):
        self.setRowColumn(len(table), len(table[0]))
        for i, item in enumerate(table):
            for j in range(len(item)):
                self.setCellWidget(i, j, item[j])

    def setHorizontalTitle(self, title: list[str]):
        self.setHorizontalHeaderLabels(title)
        return self

    def setVerticalTitle(self, title: list[str]):
        self.setVerticalHeaderLabels(title)
        return self

    def hideHorizontalHeader(self):
        self.horizontalHeader().hide()
        return self

    def hideVerticalHeader(self):
        self.verticalHeader().hide()
        return self

    def hideAllHeader(self):
        self.hideVerticalHeader().hideHorizontalHeader()
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