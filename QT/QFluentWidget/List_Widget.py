import sys
from tkinter import Button

from PySide6.QtCore import QUrl, QStringListModel, QSize
from PySide6.QtGui import QIcon, QStandardItemModel, QStandardItem, Qt
from PySide6.QtWidgets import QStyledItemDelegate, QWidget, QApplication, QVBoxLayout, QListWidgetItem, QListView
from qfluentwidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.resize(1000, 600)
        '''列表控件'''
        lw = ListWidget()

        stands = [
            '白金之星', '绿色法皇', "天堂制造", "绯红之王",
            '银色战车', '疯狂钻石', "壮烈成仁", "败者食尘",
            "隐者之紫", "黄金体验", "虚无之王", "纸月之王",
            "骇人恶兽", "男子领域", "华丽挚爱", "牙 Act 4",
            "铁球破坏者", "性感手枪", 'D4C • 爱之列车', "天生完美",
            "软又湿", "佩斯利公园", "奇迹于你", "行走的心",
            "护霜旅行者", "十一月雨", "调情圣手", "片刻静候"
        ]

        # 添加列表项
        for stand in stands:
            item = QListWidgetItem(stand)
            item.setIcon(QIcon(':/qfluentwidget/images/logo.png'))
            lw.addItem(item)

        # 默认情况下，右键单击某个列表项时不会更新该列的选中状态，如需立即选中可调用下述方法
        lw.setSelectRightClickedRow(True)

        lw.itemClicked.connect(lambda element: print(element.text()))

        # model = QStringListModel()

        # 带图标
        lv = ListView()
        model = QStandardItemModel()
        items = [
            QStandardItem(Icon(FluentIcon.GITHUB), "GITHUB"),
            QStandardItem(Icon(FluentIcon.HOME), "HOME"),
            QStandardItem(Icon(FluentIcon.PASTE), "PASTE")
        ]
        # model.setStringList(items)
        # 将项添加到模型中
        for item in items:
            model.appendRow(item)
        # 将模型设置到ListView
        lv.setModel(model)
        # 取消焦点
        lv.setFocusPolicy(Qt.NoFocus)
        lv.setStyleSheet("""
            ListView::item {
                border-bottom: 1px solid black;
            }
            ListView::item:selected {
            }
        """)
        lv.setIconSize(QSize(24, 24))
        # 设置自定义代理
        # lv.setItemDelegate(CustomModel(lv))
        lv.setSelectRightClickedRow(True)
        # 获取文本
        lv.clicked.connect(lambda element: print(model.data(element)))
        # layout.addWidget(lw)
        layout.addWidget(lv)


# 重写高度 QStyledItemDelegate
# class CustomModel(ListItemDelegate):
#     def sizeHint(self, option, index):
#         return QSize(0, 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
