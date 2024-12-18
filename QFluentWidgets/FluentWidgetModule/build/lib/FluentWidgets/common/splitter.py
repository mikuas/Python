from PySide6.QtGui import Qt
from PySide6.QtWidgets import QSplitter, QWidget


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