import sys

from PySide6.QtCore import QTime, QDate
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import Qt

from qfluentwidgets import SmoothScrollArea, VBoxLayout, TimePicker, AMTimePicker, DatePicker, ZhDatePicker, \
    CalendarPicker, FastCalendarPicker


class DateTimeWidget(SmoothScrollArea):
    def __init__(self, text, parent=None):
        super().__init__(parent)

        self.initWindow()
        self.initDT()
        self.initLayout()

        self.setObjectName(text.replace(' ', '_'))

    def initWindow(self):
        self.scrollWidget = QWidget()
        self.vLayout = VBoxLayout(self.scrollWidget)
        self.vLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)

    def initDT(self):
        '''
            TimePickerBase  时间选择器基类
            DatePickerBase  日期选择器基类
        '''

        '''24小时制时间选择器'''
        self.timePicker = TimePicker(self)
        self.timePicker.timeChanged.connect(lambda time: print(time.toString()))

        '''AM/PM 小时制时间选择器'''
        self.AMTimePicker = AMTimePicker(self)
        self.AMTimePicker.timeChanged.connect(lambda time: print(time.toString()))

        '''日期选择器'''
        # self.datePicker = DatePicker(self)
        # 中文
        self.datePicker = ZhDatePicker(self)
        self.datePicker.dateChanged.connect(lambda date: print(date.toString()))

        '''日历选择器'''
        self.calendarPicker = FastCalendarPicker(self)
        # set current date
        self.calendarPicker.setDate(QDate(2024, 11, 5))
        # set date formate
        self.calendarPicker.setDateFormat(Qt.TextDate)
        self.calendarPicker.setDateFormat('yyyy-M-d')
        self.calendarPicker.dateChanged.connect(lambda date: print(date.toString()))

    def initLayout(self):
        self.vLayout.addWidget(self.timePicker, 0, Qt.AlignmentFlag.AlignCenter)
        self.vLayout.addWidget(self.AMTimePicker, 0, Qt.AlignmentFlag.AlignCenter)
        self.vLayout.addWidget(self.datePicker, 0, Qt.AlignmentFlag.AlignCenter)
        self.vLayout.addWidget(self.calendarPicker, 0, Qt.AlignmentFlag.AlignCenter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = DateTimeWidget("DATATIME")
    w.resize(1000, 600)
    w.show()
    sys.exit(app.exec())