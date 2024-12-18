from PySide6.QtGui import QFont, QColor
from PySide6.QtWidgets import QWidget


def setFonts(widgets: list[QWidget], fontSize: int, weight: QFont.Weight = QFont.Weight.Normal):
    """ set widget font size"""
    for widget in widgets:
        widget.setFont(getFont(fontSize, weight))

def setFonts_(widgets: list[QWidget], fontSize: list[int], weight: QFont.Weight = QFont.Weight.Normal):
    for widget, size in zip(widgets, fontSize):
        widget.setFont(getFont(size, weight))

def getFont(fontSize: int, weight: QFont.Weight = QFont.Weight.Normal):
    """ get font size"""
    font = QFont()
    font.setFamilies(['Segoe UI', 'Microsoft YaHei', 'PingFang SC'])
    font.setPixelSize(fontSize)
    font.setWeight(weight)
    return font

def setTextColors(widgets: list[QWidget], color: QColor | str):
    """ set text color """
    for widget in widgets:
        widget.setStyleSheet(f"color: {color}")