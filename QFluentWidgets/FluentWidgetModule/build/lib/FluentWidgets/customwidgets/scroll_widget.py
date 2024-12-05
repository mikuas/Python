from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget
from qfluentwidgets import SingleDirectionScrollArea, SmoothScrollArea, ScrollArea

from .layout import VBoxLayout, HBoxLayout


class VerticalScrollWidget(SingleDirectionScrollArea):
    """ 平滑垂直滚动小部件 """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.__widget = QWidget()
        self.vLayout = VBoxLayout(self.__widget)
        self.setWidget(self.__widget)
        self.vLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setWidgetResizable(True)


class HorizontalScrollWidget(SingleDirectionScrollArea):
    """ 平滑水平滚动小部件 """
    def __int__(self, parent: QWidget = None):
        super().__init__(parent, Qt.Orientation.Horizontal)
        self.__widget = QWidget()
        self.hLayout = VBoxLayout(self.__widget)
        self.setWidget(self.__widget)
        self.hLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setWidgetResizable(True)


class ScrollWidget(ScrollArea):
    """ 平滑双向滚动小部件 """
    def __init__(self, parent=None):
        super().__init__(parent)
        self._initWidget()

    def _initWidget(self):
        self.__widget = QWidget()
        self.setWidget(self.__widget)
        self.setWidgetResizable(True)

    def createVBoxLayout(self):
        return VBoxLayout(self.__widget)

    def createHBoxLayout(self):
        return HBoxLayout(self.__widget)


class SmoothScrollWidget(SmoothScrollArea, ScrollWidget):
    """ 靠动画实现的平滑双向滚动小部件 """
    def __init__(self, parent=None):
        super().__init__(parent)
        self._initWidget()