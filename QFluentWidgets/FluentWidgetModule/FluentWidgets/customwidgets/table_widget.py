import sys
from typing import Union

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, Qt, QPainter, QColor, QFont
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QApplication, QListWidgetItem, QStyledItemDelegate, QMainWindow
from qfluentwidgets import TableWidget as Table, setTheme, Theme, ListWidget, FluentIcon, Icon


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
        for i, item in enumerate(table):
            for j in range(len(item)):
                self.setItem(i, j, QTableWidgetItem(item[j]))
        return self

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


# class ListWidgets(ListWidget):
#     def __init__(self, parent: QWidget = None):
#         super().__init__(parent)
#         self.setFocusPolicy(Qt.NoFocus)
#
#     def addIconItem(
#             self,
#             icons: list[Union[QIcon, str, FluentIcon]],
#             items: list[str],
#             itemHeight: int = 45,
#             alignFlag: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignVertical_Mask
#     ):
#         for icon, item in zip(icons, items):
#             item = QListWidgetItem(item)
#             if isinstance(icon, FluentIcon):
#                 item.setIcon(Icon(icon))
#             else:
#                 item.setIcon(QIcon(icon))
#             item.setTextAlignment(alignFlag)
#             item.setSizeHint(QSize(self.width(), itemHeight))
#             self.addItem(item)
#         return self


class Demo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1200, 700)
        self.listWidget = ListWidget(self)
        data = [
            '白金之星', '绿色法皇', "天堂制造", "绯红之王",
            '银色战车', '疯狂钻石', "壮烈成仁", "败者食尘",
            "隐者之紫", "黄金体验", "虚无之王", "纸月之王",
            "骇人恶兽", "男子领域", "华丽挚爱", "牙 Act 4",
            "铁球破坏者", "性感手枪", 'D4C • 爱之列车', "天生完美",
            "软又湿", "佩斯利公园", "奇迹于你", "行走的心",
            "护霜旅行者", "十一月雨", "调情圣手", "片刻静候"
        ]

        self.listWidget.addItems(data)
        self.listWidget.setFixedHeight(500)
        # 默认情况下，右键单击某个列表项时不会更新该列的选中状态，如需立即选中可调用下述方法
        self.listWidget.setSelectRightClickedRow(True)
        # 连接信号插槽
        self.listWidget.clicked.connect(
            lambda value: print(self.listWidget.model().data(value))
        )
        # 取消焦点
        self.listWidget.setFocusPolicy(Qt.NoFocus)
        self.listWidget.setStyleSheet("""
            ListWidget::item {
                font-size: 24px;
                background-color: red;
                height: 50px;
            }
            ListWidget::item:selected {
                border: none;
            }
        """)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Demo()
    setTheme(Theme.AUTO)
    w.show()
    sys.exit(app.exec())
