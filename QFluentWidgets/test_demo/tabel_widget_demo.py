import sys

from PySide6.QtWidgets import QApplication, QTableWidget
from qfluentwidgets import FluentIcon

from QtFluentWidgets.FluentWidgetModule.FluentWidgets import VerticalScrollWidget, TableWidget, ListWidget


class Demo(VerticalScrollWidget):
    def __init__(self):
        super().__init__()
        self.resize(950, 600)
        self.setMinimumWidth(950)
        self.setMinimumHeight(600)
        self.table = (
            TableWidget(self)
            .addTableData([[f"Item {i}" for i in range(36)][_:_ + 4] for _ in range(0, 36, 4)])
            .hideVerticalHeader()
            .setItemMinWidth(self.width() / 4.11)
            .setItemMinHeight(48)
            .setHorizontalTitle(['Title 1', 'Title 2', 'Title 3', 'Title 4'])
            .disableEdit()
        )
        self.table.setFixedWidth(self.width() - 20)

        self.list = ListWidget(self)
        self.list.addItems([f"Item {i}" for i in range(16)])
        self.list.addIconItems(
            [FluentIcon.HOME for _ in range(16)],
            [f"Item {i+16}" for i in range(16)]
        )

        self.list.setFixedWidth(self.width() - 20)
        self.vBoxLayout.addWidgets([self.table, self.list])

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.table.setFixedWidth(self.width() - 20)
        self.table.setItemMinWidth(self.width() / 4.11)
        self.list.setFixedWidth(self.width() - 20)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec())