from PySide6.QtGui import QFont, QColor
from PySide6.QtWidgets import QWidget
from qfluentwidgets import setFont


def setFonts(widgets: list[QWidget], fontSize: int, weight: QFont.Weight = QFont.Weight.Normal):
    """ set widget font size"""
    for widget in widgets:
        setFont(widget, fontSize, weight)

def setTextColors(widgets: list[QWidget], color: QColor | str):
    for widget in widgets:
        widget.setStyleSheet(f"color: {color}")