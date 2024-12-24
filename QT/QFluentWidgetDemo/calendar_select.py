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

        '''日历选择器'''
        # calendar = CalendarPicker(self)
        calendar = FastCalendarPicker(self)
        # 设置当前日期
        calendar.setDate(QDate())
        calendar.dateChanged.connect(
            lambda: print(calendar.date)
        )

        # 设置日期格式
        calendar.setDateFormat(Qt.TextDate)
        calendar.setDateFormat('yyyy-M-d')

        mainLayout.addWidget(calendar)
        self.setCentralWidget(centerWindget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())