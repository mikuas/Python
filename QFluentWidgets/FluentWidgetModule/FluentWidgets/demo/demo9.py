# coding:utf-8
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QPainterPath, QPixmap, QColor, QPainter
from PySide6.QtWidgets import QApplication, QWidget
from qfluentwidgets.components.material import AcrylicWidget

from qfluentwidgets.components.widgets.acrylic_label import AcrylicBrush


class Demo(QWidget, AcrylicWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 400)
        # self.acrylic = AcrylicWidget()
        painter = QPainter()
        painter.setRenderHints(QPainter.RenderHint.Antialiasing)

        self._drawAcrylic(painter)
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.setPen(QColor(100, 120, 98, 32))
        rect = self.rect().adjusted(1, 1, -1, -1)
        painter.drawRoundedRect(rect, 8, 8)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec()