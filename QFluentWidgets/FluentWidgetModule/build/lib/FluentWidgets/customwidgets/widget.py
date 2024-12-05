import PySide6
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget

# ################################### !!!!!!
class CBoxWidget(QWidget):
    """ 内容垂直居中小部件 """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.hLayout = QHBoxLayout(self)
        self.vLayout = QVBoxLayout()
        self.hLayout.addLayout(self.vLayout)

    def addWidget(self, widget: QWidget, alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter):
        self.vLayout.addWidget(widget, alignment=alignment)
        return self

    def addWidgets(self, widgets: list[QWidget]):
        for widget in widgets:
            self.addWidget(widget)
        return self

    def addLayout(self, layout: PySide6.QtWidgets.QBoxLayout):
        self.vLayout.addLayout(layout)
        return self

    def addItem(self, item: PySide6.QtWidgets.QLayoutItem):
        self.vLayout.addItem(item)
        return self

    def addChildLayout(self, l: PySide6.QtWidgets.QLayout):
        self.vLayout.addChildLayout(l)
        return self

    def addChildWidget(self, w: PySide6.QtWidgets.QWidget):
        self.hLayout.addChildWidget(w)
        return self

    def addStrut(self, strut: int):
        self.vLayout.addStrut(strut)
        return self

    def addSpacerItem(self, spacerItem: PySide6.QtWidgets.QSpacerItem):
        self.vLayout.addSpacerItem(spacerItem)
        return self

    def addSpacing(self, size: int):
        self.vLayout.addSpacing(size)
        return self

    def addStretch(self, stretch: int):
        self.hLayout.addStretch(stretch)
        return self




