# coding:utf-8
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget
from qfluentwidgets import PipsScrollButtonDisplayMode, PopUpAniStackedWidget, Theme, setTheme

from ..layout import VBoxLayout
from .pips_pager import PipsPager


class PagerWidgetBase(QWidget):
    """ pager widget base class """
    def __init__(self, parent=None, orientation=Qt.Orientation.Horizontal):
        super().__init__(parent)
        self._pager = PipsPager(orientation, self)
        self._stackedWidget = PopUpAniStackedWidget(self)
        self._pager.currentIndexChanged.connect(lambda index: self._stackedWidget.setCurrentIndex(index))
        self.__widgets = [] # type: [QWidget]
        self.__initLayout()
        setTheme(Theme.AUTO)

    def addWidget(self, widget: QWidget):
        """ add widget to stacked widget"""
        self._stackedWidget.addWidget(widget)
        self.__addToWidgets(widget)
        self._pager.setPageNumber(len(self.__widgets))
        return self

    def addWidgets(self, widgets: list[QWidget]):
        """ add widgets to stacked widget"""
        for widget in widgets:
            self.addWidget(widget)
        return self

    def setCurrentIndex(self, index: int):
        """ set stacked widget current index"""
        self._stackedWidget.setCurrentIndex(index)
        return self

    def removeWidget(self, index: int):
        """ remove widget from stacked widget"""
        if index < len(self.__widgets):
            self._stackedWidget.removeWidget(self.__widgets.pop(index))
            self._pager.setPageNumber(len(self.__widgets))
        return self

    def __addToWidgets(self, widget: QWidget):
        self.__widgets.append(widget)

    def displayNextButton(self):
        """ set next page button display"""
        self._pager.setNextButtonDisplayMode(PipsScrollButtonDisplayMode.ALWAYS)
        return self

    def displayPrevButton(self):
        """ set previous page button display"""
        self._pager.setPreviousButtonDisplayMode(PipsScrollButtonDisplayMode.ALWAYS)
        return self

    def hoverDisplayPrevButton(self):
        """ set previous page button hover display"""
        self._pager.setPreviousButtonDisplayMode(PipsScrollButtonDisplayMode.ON_HOVER)
        return self

    def hoverDisplayNextButton(self):
        """ set next page button hover display"""
        self._pager.setNextButtonDisplayMode(PipsScrollButtonDisplayMode.ON_HOVER)
        return self

    def setPageVisible(self, visible: bool):
        """ set page visible flag"""
        self._pager.setVisible(visible)
        return self

    def setVisibleNumber(self, number: int):
        """ set page visible flag"""
        self._pager.setVisibleNumber(number)
        return self

    def setStackedFixedSize(self, width: int, height: int):
        self._stackedWidget.setFixedSize(width, height)
        return self

    def setStackedMinSize(self, width: int, height: int):
        self._stackedWidget.setMinimumSize(width, height)
        return self

    def getPageNumber(self):
        return self._pager.getPageNumber()

    def getAllWidget(self):
        """ get stacked all widget"""
        return self.__widgets

    def __initLayout(self):
        self.__vLayout = VBoxLayout(self)
        self.__vLayout.addWidget(self._stackedWidget)
        self.__vLayout.addWidget(self._pager, alignment=Qt.AlignmentFlag.AlignHCenter)


class HorizontalPagerWidget(PagerWidgetBase):
    """ 水平分页器 """
    def __init__(self, parent=None):
        super().__init__(parent)


class VerticalPagerWidget(PagerWidgetBase):
    """ 垂直分页器 """
    def __init__(self, parent=None):
        super().__init__(parent, Qt.Orientation.Vertical)