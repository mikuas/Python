import sys
from symtable import Function

from PySide6.QtCore import QSize, QUrl, QDate
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget
from PySide6.QtGui import Qt
from qfluentwidgets import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 450)
        centerWindget = QWidget(self)
        mainLayout = QVBoxLayout(centerWindget)

        '''日期选着器'''
        self.datePicker = DatePicker()

        # 设置当前日期
        self.datePicker.setDate(QDate(2024, 2, 26))

        # Zh_CN
        self.datePicker = ZhDatePicker()
        self.datePicker.setDate(QDate(2024, 2, 26))
        # 获取当前日期
        print(self.datePicker.date)

        # 日期发生改变
        self.datePicker.dateChanged.connect(lambda date: print(date.toString()))

        mainLayout.addWidget(self.datePicker)
        self.setCentralWidget(centerWindget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())