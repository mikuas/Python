from PySide6.QtWidgets import QApplication, QTableWidget, QStyledItemDelegate, QMainWindow, QTableWidgetItem, \
    QAbstractItemView
from PySide6.QtGui import QPainter, QPixmap
from PySide6.QtCore import Qt, QRect, QModelIndex, QAbstractListModel
from qfluentwidgets import setTheme, Theme, TitleLabel, IconWidget, FluentIcon, TransparentToolButton

from FluentWidgets import TableWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.table = TableWidget(self)
        self.table.setFixedSize(self.size())

        self.table.setEditTriggers(
            QAbstractItemView.NoEditTriggers
        )

        self.table.setDragEnabled(False)

        # 启用边框并设置圆角
        self.table.setBorderVisible(True)
        self.table.setBorderRadius(8)

        self.table.setRowColumn(58, 2)

        self.table.addTabWidget([
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
            [TitleLabel('hello', self), TitleLabel('world', self)],
        ])
        # 设置水平表头并隐藏垂直表头
        # table.setHorizontalHeaderLabels(['Title', 'Artist', 'Album', 'Year', 'Duration'])
        self.table.verticalHeader().hide()

    def resizeEvent(self, event):
        self.table.setFixedSize(self.size())

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    setTheme(Theme.AUTO)
    window.resize(600, 400)
    window.show()
    sys.exit(app.exec())
