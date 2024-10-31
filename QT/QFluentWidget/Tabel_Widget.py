import sys

from PySide6.QtCore import QUrl
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QApplication, QTableWidgetItem, QVBoxLayout
from qfluentwidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1000, 600)
        layout = QVBoxLayout(self)
        '''表格控件'''
        table = TableWidget()

        # 启动边框并设置圆角
        table.setBorderVisible(True)
        table.setBorderRadius(8)

        table.setWordWrap(False)
        # 行
        table.setRowCount(3)
        # 列
        table.setColumnCount(5)

        # 添加数据
        songInfos = [
            ['シアワセ', 'aiko', '秘密', '2008', '5:25'],
            ['なんでもないや', 'RADWIMPS', '君の名は。', '2016', '3:16'],
            ['恋をしたのは', 'aiko', '恋をしたのは', '2016', '6:02'],
        ]

        for i, songInfo in enumerate(songInfos):
            for j in range(5):
                table.setItem(i, j, QTableWidgetItem(songInfo[j]))

        # 设置水平表头并隐藏垂直表头
        table.setHorizontalHeaderLabels(['Title', 'Artist', 'Album', 'Year', 'Duration'])
        table.verticalHeader().hide()
        # 默认情况下，右键单击某个列表项时不会更新该列的选中状态，如需立即选中可调用下述方法
        table.setSelectRightClickedRow(True)

        # 禁用平滑滚动
        table.scrollDelagate.verticalSmoothScroll.setSmoothMode(SmoothMode.NO_SMOOTH)

        ''''''
        tv = TableView()
        model = QStandardItemModel()
        # 设置表头
        model.setHorizontalHeaderLabels(['Title', 'Artist', 'Album', 'Year', 'Duration'])

        # 添加数据
        for i, songInfo in enumerate(songInfos):
            for j in range(5):
                model.setItem(i, j, QStandardItem(songInfo[j]))

        tv.resize(400, 300)
        tv.setRowHeight(1, 500)

        tv.setModel(model)
        # layout.addWidget(table)
        layout.addWidget(tv)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
