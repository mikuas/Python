from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QLayout


class HBoxLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()

    def addWidgets(self, widgets: list[QWidget], stretch: int = 1, alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter):
        for widget in widgets:
            self.addWidget(widget, stretch, alignment)
        return self

    def addWidgets(self, widgets: list[QWidget], stretch: list[int], alignment: list[Qt.AlignmentFlag] = Qt.AlignmentFlag.AlignCenter):
        for w, s, a in zip(widgets, stretch, alignment):
            self.addWidget(w, s, a)
        return self

    def addLayouts(self, layouts: list[QLayout], stretches: int = 1):
        for layout in layouts:
            self.addLayout(layout, stretches)
        return self

    def addLayouts(self, layouts: list[QLayout], stretches: list[int]):
        for l, s in zip(layouts, stretches):
            self.addLayout(l, s)
        return self


class VBoxLayout(QVBoxLayout, HBoxLayout):
    def __init__(self):
        super().__init__()


vb = VBoxLayout()
vb.addWidgets(
    [QWidget()],
    [1]
)
