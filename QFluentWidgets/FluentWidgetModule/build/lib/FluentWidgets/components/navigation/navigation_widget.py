# coding:utf-8
from typing import Union

from PySide6.QtGui import Qt, QIcon
from PySide6.QtWidgets import QWidget
from qfluentwidgets import (
    Pivot, SegmentedWidget, SegmentedToolWidget, SegmentedToggleToolWidget, FluentIconBase, TabBar,
    TabCloseButtonDisplayMode, PopUpAniStackedWidget, setTheme, Theme, HorizontalSeparator
)
from ..layout import VBoxLayout, HBoxLayout


class NavigationBase(QWidget):
    """ 导航组件基类 """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        setTheme(Theme.AUTO)
        self.hBoxLayout = HBoxLayout(self)
        self.navigation = None
        self._key = '0'
        self.stackedWidget = PopUpAniStackedWidget(self)

    def _initLayout(self):
        self.vLayout = VBoxLayout(self)
        self.hLayout = HBoxLayout()
        self.hBoxLayout.addLayout(self.vLayout)
        self.vLayout.addWidgets([self.navigation, self.stackedWidget])
        self.vLayout.addLayout(self.hLayout)

    def addSeparator(self, index=1):
        separator = HorizontalSeparator(self)
        self.vLayout.insertWidget(index, separator)
        return self

    def addNavigationSeparator(self, index: int):
        self.navigation.insertItem(index, self._key, '|').setFixedWidth(1)
        self._key = str(int(self._key) + 1)
        return self

    def addSubInterface(self, routeKey: str, text: str, widget: QWidget, icon: Union[QIcon, str, FluentIconBase] = None):
        """ add sub interface, rotKey isUnique"""
        self.stackedWidget.addWidget(widget)
        self.navigation.addItem(routeKey, text, lambda: self.switchTo(widget), icon)
        return self

    def addSubInterfaces(
            self,
            routeKeys: list[str],
            texts: list[str],
            widgets: list[QWidget],
            icons: list[Union[QIcon, str, FluentIconBase]] = None
    ):
        icons = icons if icons is not None else [None for _ in range(len(routeKeys))]
        for key, text, widget, icon in zip(routeKeys, texts, widgets, icons):
            self.addSubInterface(key, text, widget, icon)
        return self

    def switchTo(self, widget: QWidget):
        self.stackedWidget.setCurrentWidget(widget)

    def setCurrentItem(self, routeKey: str):
        self.navigation.setCurrentItem(routeKey)
        return self

    def enableNavCenter(self):
        self.vLayout.removeWidget(self.navigation)
        self.vLayout.insertWidget(0, self.navigation, alignment=Qt.AlignmentFlag.AlignHCenter)
        return self


class PivotNav(NavigationBase):
    """ 导航栏 """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.navigation = Pivot(self)
        self._initLayout()


class SegmentedNav(PivotNav):
    """ 分段导航 """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.navigation = SegmentedWidget(self)
        self._initLayout()


class SegmentedToolNav(PivotNav):
    """ 工具导航 """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.navigation = SegmentedToolWidget(self)
        self._initLayout()
        self.enableNavCenter()

    def addSubInterface(self, routeKey: str, widget: QWidget, icon: Union[QIcon, str, FluentIconBase] = None, *args):
        self.stackedWidget.addWidget(widget)
        self.navigation.addItem(routeKey, icon, lambda: self.switchTo(widget))
        return self

    def addSubInterfaces(
            self,
            routeKeys: list[str],
            icons: list[Union[QIcon, str, FluentIconBase]],
            widgets: list[QWidget],
            *args
    ):
        for key, icon, widget in zip(routeKeys, icons, widgets):
            self.addSubInterface(key, widget, icon)
        return self


class SegmentedToggleToolNav(SegmentedToolNav):
    def __init__(self, parent=None):
        """ 主题色选中导航 """
        super().__init__(parent)
        self.navigation = SegmentedToggleToolWidget(self)
        self._initLayout()
        self.enableNavCenter()


class LabelBarWidget(QWidget):
    """ 标签页组件 """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.tabBar = TabBar(self)
        self.stackedWidget = PopUpAniStackedWidget(self)
        self.hLayout = HBoxLayout(self)
        self.vLayout = VBoxLayout()
        self.__initLayout()
        self.__initTitleBar()

    def __initLayout(self):
        self.hLayout.addLayout(self.vLayout)
        self.vLayout.addWidgets([self.tabBar, self.stackedWidget])

    def __initTitleBar(self):
        self.tabBar.setTabShadowEnabled(True)
        self.tabBar.setMovable(True)
        self.tabBar.setScrollable(True)
        self.tabBar.setCloseButtonDisplayMode(TabCloseButtonDisplayMode.ON_HOVER)

    def hideAddButton(self):
        self.tabBar.addButton.hide()
        return self

    def hideCloseButton(self):
        self.tabBar.setCloseButtonDisplayMode(TabCloseButtonDisplayMode.NEVER)
        return self

    def switchTo(self, widget: QWidget):
        self.stackedWidget.setCurrentWidget(widget)

    def addSubTab(self, routeKey, text, icon=None, widget: QWidget = None):
        """ add sub tab, roteKey isUnique """
        self.stackedWidget.addWidget(widget)
        self.tabBar.addTab(routeKey, text, icon, lambda: self.switchTo(widget))
        return self

    def addSubTabs(
            self, routeKeys: list[str],
            texts: list[str],
            widgets: list[QWidget] = None,
            icons: list[Union[QIcon, str, FluentIconBase]] = None
    ):
        icons = icons if icons is not None else [None for _ in range(len(routeKeys))]
        for key, text, icon, widget in zip(routeKeys, texts, icons, widgets):
            self.addSubTab(key, text, icon, widget)
        return self