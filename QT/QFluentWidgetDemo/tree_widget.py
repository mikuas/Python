import sys

from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QWidget, QTreeWidgetItem, QVBoxLayout, QApplication, QPushButton
from qfluentwidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        '''树状控件'''
        layout = QVBoxLayout(self)
        tree = TreeWidget()

        # 添加子树
        item1 = QTreeWidgetItem(['JoJo 1 - Phantom Blood'])
        item1.addChildren([
            QTreeWidgetItem(['Jonathan Joestar']),
            QTreeWidgetItem(['Dio Brando']),
        ])
        tree.addTopLevelItem(item1)

        # 添加子树
        item2 = QTreeWidgetItem(['JoJo 3 - Stardust Crusaders'])
        item21 = QTreeWidgetItem(['Jotaro Kujo'])

        it = QTreeWidgetItem(['空条承太郎'])
        item21.addChildren([
            it,
            QTreeWidgetItem(['空条蕉太狼']),
        ])
        # 设置图标
        it.setIcon(0, Icon(FluentIcon.GITHUB))

        item2.addChild(item21)
        tree.addTopLevelItem(item2)

        # 隐藏表头
        tree.setHeaderHidden(True)
        tree.setFixedSize(300, 380)

        # 禁用平滑滚动
        tree.scrollDelagate.verticalSmoothScroll.setSmoothMode(SmoothMode.NO_SMOOTH)

        tv = TreeView()

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Item"])
        # 创建根项
        ri = QStandardItem("Root")
        self.model.appendRow(ri)

        # 创建子项
        c1 = QStandardItem("Child 1")
        c2 = QStandardItem("Child 2")

        ri.appendRow(c1)
        ri.appendRow(c2)

        # 添加孙子项
        g = QStandardItem("Grand")
        c1.appendRow(g)

        tv.setModel(self.model)

        tv.selectionModel().selectionChanged.connect(
            lambda selected, deselected: self.onItemSelected(selected)
        )

        layout.addWidget(tree)
        layout.addWidget(tv)

    def onItemSelected(self, selected):
        for index in selected.indexes():
            item = self.model.itemFromIndex(index)
            if item:
                print(item.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
