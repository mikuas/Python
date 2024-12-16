# coding:utf-8
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget
from qfluentwidgets import SingleDirectionScrollArea, SmoothScrollArea, ScrollArea, setTheme, Theme

from ..layout import VBoxLayout, HBoxLayout


class SingleScrollWidgetBase(SingleDirectionScrollArea):
    """ 滚动组件基类 """
    def __init__(self, parent=None, orient: Qt.Orientation = None):
        super().__init__(parent, orient)
        self._widget = QWidget()
        self.setWidget(self._widget)
        self.setWidgetResizable(True)
        setTheme(Theme.AUTO)
        # self.enableTransparentBackground()


class VerticalScrollWidget(SingleScrollWidgetBase):
    """ 平滑垂直滚动小部件 """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent, Qt.Orientation.Vertical)
        self.vBoxLayout = VBoxLayout(self._widget)


class HorizontalScrollWidget(SingleScrollWidgetBase):
    """ 平滑水平滚动小部件 """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent, Qt.Orientation.Horizontal)
        self.hBoxLayout = HBoxLayout(self._widget)


class ScrollWidget(ScrollArea):
    """ 平滑双向滚动小部件 """
    def __init__(self, parent=None):
        super().__init__(parent)
        setTheme(Theme.AUTO)
        # self.enableTransparentBackground()
        self.__widget = QWidget()
        self.setWidget(self.__widget)
        self.setWidgetResizable(True)

    def createVBoxLayout(self):
        """ create vertical layout """
        return VBoxLayout(self.__widget)

    def createHBoxLayout(self):
        """ create horizontal layout """
        return HBoxLayout(self.__widget)


class SmoothScrollWidget(SmoothScrollArea, ScrollWidget):
    """ 靠动画实现的平滑双向滚动小部件 """
    def __init__(self, parent=None):
        super().__init__(parent)