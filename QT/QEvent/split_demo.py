from FluentWidgets import VBoxLayout
from PySide6.QtCore import QRect
from PySide6.QtGui import Qt, QPaintEvent, QPainter, QColor
from PySide6.QtWidgets import QApplication, QWidget, QSplitter, QSplitterHandle, QPushButton, QFrame, QStyleOption
from qfluentwidgets import LineEdit, PrimaryPushButton


class Splitter(QSplitter):
    def __init__(self, orientation=Qt.Orientation.Vertical, parent=None):
        super().__init__(orientation, parent)
        self.setHandleWidth(1)
        self.setSplitterColor('skyblue')

    def setSplitterColor(self, color: str):
        self.setStyleSheet("QSplitter::handle {" + f"background-color: {color};" + "}")

    def addWidgets(self, widgets: list[QWidget]):
        for widget in widgets:
            self.addWidget(widget)


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 500)
        self.vBoxLayout = VBoxLayout(self)
        self.splitter = Splitter(Qt.Orientation.Horizontal, self)

        self.frame1 = QFrame(self)
        self.frame2 = QFrame(self)
        self.frame3 = QFrame(self)

        # self.frame1.setStyleSheet('background-color:skyblue')
        # self.frame2.setStyleSheet('background-color:pink')

        self.splitter.addWidget(self.frame1)
        self.splitter.addWidget(self.frame2)
        self.splitter.addWidget(self.frame3)

        self.vBoxLayout.addWidget(self.splitter)

        self.fLayout1 = VBoxLayout(self.frame1)
        self.fLayout2 = VBoxLayout(self.frame2)
        self.fLayout3 = VBoxLayout(self.frame3)

        self.frame1.setMinimumHeight(50)
        self.frame2.setMinimumHeight(50)

        for _ in range(3):
            self.fLayout1.addWidget(PrimaryPushButton(f"Frame 1 Button {_}", self))
            self.fLayout2.addWidget(PrimaryPushButton(f"Frame 2 Button {_}", self))
            self.fLayout3.addWidget(PrimaryPushButton(f"Frame 3 Button {_}", self))


if __name__ == '__main__':
    app = QApplication([])
    window = Demo()
    window.show()
    app.exec()







