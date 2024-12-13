import sys

from PySide6.QtGui import Qt, QColor
from PySide6.QtWidgets import QWidget, QApplication, QListWidgetItem
from FluentWidgets import VerticalScrollWidget, HBoxLayout
from qfluentwidgets import TitleLabel, ListWidget, Icon, FluentIcon


class Demo(VerticalScrollWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.list = ListWidget(self)
        self.list.setFixedSize(self.size())
        for _ in range(100000):
            self.list.addItem(QListWidgetItem(Icon(FluentIcon.HOME), f"hello world {_}"))
            # self.vBoxLayout.addWidget(TitleLabel('hello world', self))
            # if _ % 2 == 0:
            #     self.vBoxLayout.addWidget(Widget(), alignment=Qt.AlignmentFlag.AlignHCenter)
            # else:
            #     w = Widget()
            #     w.title.setTextColor(QColor(111, 45, 200), QColor(114, 54, 4))
            #     self.vBoxLayout.addWidget(w, alignment=Qt.AlignmentFlag.AlignHCenter)


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.hBoxLayout = HBoxLayout(self)
        self.title = TitleLabel("hello world", self)
        self.hBoxLayout.addWidget(self.title)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec())