from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QLayout


class HBoxLayout(QHBoxLayout):
    """ horizontal layout """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

    def addWidgets(self, widgets: list[QWidget], stretch=0, alignment=Qt.AlignmentFlag(0)):
        """ add stretch default is 0, alignment default is None widgets"""
        for widget in widgets:
            self.addWidget(widget, stretch=stretch, alignment=alignment)
        return self

    def addLayouts(self, layouts: list[QLayout], stretch=0):
        """ add stretch default is 0 layouts"""
        for layout in layouts:
            self.addLayout(layout, stretch)
        return self

    def addWidgets_(self, widgets: list[QWidget], stretch: list[int] | int = 1, alignment: list[Qt.AlignmentFlag] | Qt.AlignmentFlag = Qt.AlignmentFlag(0)):
        """ add custom stretch alignment widgets"""
        stretch = [stretch for _ in range(len(widgets))] if type(stretch) is not list else stretch
        alignment = [alignment for _ in range(len(widgets))] if type(alignment) is not list else alignment
        for w, s, a in zip(widgets, stretch, alignment):
            self.addWidget(w, s, a)
        return self

    def addLayouts_(self, layouts: list[QLayout], stretches: list[int] | int = 1):
        """ add custom stretch alignment layouts"""
        stretches = [stretches for _ in range(len(layouts))] if type(stretches) is not list else stretches
        for l, s in zip(layouts, stretches):
            self.addLayout(l, s)
        return self


class VBoxLayout(QVBoxLayout, HBoxLayout):
    """ vertical layout """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)