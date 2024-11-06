import sys
from symtable import Function

from PySide6.QtCore import QSize, QUrl
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget
from PySide6.QtGui import Qt
from qfluentwidgets import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 450)
        centerWindget = QWidget(self)
        mainLayout = QVBoxLayout(centerWindget)

        '''下拉框'''
        # 允许用户编辑
        # EditableComboBox()
        items = [
            '0d00',
            '美咕噜',
            '朝武芳乃',
            '常磐华乃'
        ]
        self.comBox = ComboBox(self)
        self.comBox.setPlaceholderText("请选择一个脑婆")
        self.comBox.addItems(items)
        # 默认选中第一个, 取消选中
        self.comBox.setCurrentIndex(-1)


        self.comEditBox = EditableComboBox(self)
        self.comEditBox.setPlaceholderText("请选择一个脑婆")
        self.comEditBox.addItems(items)
        # 默认选中第一个, 取消选中
        self.comEditBox.setCurrentIndex(-1)

        # 当前选项的索引改变信号
        self.comEditBox.currentIndexChanged.connect(lambda index: print(self.comBox.currentText()))

        mainLayout.addWidget(self.comBox)
        mainLayout.addWidget(self.comEditBox)
        self.setCentralWidget(centerWindget)

        # setTheme(Theme.DARK)
        # setThemeColor(FluentThemeColor.DEFAULT_BLUE.color())
        setFont(self.comBox, 16)
        setFont(self.comEditBox, 16)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())