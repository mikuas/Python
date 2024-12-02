import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QLayout, QApplication
from qfluentwidgets import TitleLabel, setTheme, Theme


class HBoxLayout(QHBoxLayout):
    """ 水平布局控件 """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

    def addWidgets(self, widgets: list[QWidget], stretch=0, alignment=Qt.AlignmentFlag.AlignCenter):
        for widget in widgets:
            self.addWidget(widget, stretch=stretch, alignment=alignment)
        return self

    def addLayouts(self, layouts: list[QLayout], stretch=0):
        for layout in layouts:
            self.addLayout(layout, stretch)
        return self

    def addWidgets_(self, widgets: list[QWidget], stretch: list[int] | int = 1, alignment: list[Qt.AlignmentFlag] | Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter):
        stretch = [stretch for _ in range(len(widgets))] if type(stretch) is not list else stretch
        alignment = [alignment for _ in range(len(widgets))] if type(alignment) is not list else alignment
        for w, s, a in zip(widgets, stretch, alignment):
            self.addWidget(w, s, a)
        return self

    def addLayouts_(self, layouts: list[QLayout], stretches: list[int] | int = 1):
        stretches = [stretches for _ in range(len(layouts))] if type(stretches) is not list else stretches
        for l, s in zip(layouts, stretches):
            self.addLayout(l, s)
        return self


class VBoxLayout(QVBoxLayout, HBoxLayout):
    """ 垂直布局控件 """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)