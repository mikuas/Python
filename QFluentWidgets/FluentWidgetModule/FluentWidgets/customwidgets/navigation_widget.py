import sys
import random
from typing import Union

from PySide6.QtGui import Qt, QIcon
from PySide6.QtWidgets import QWidget, QStackedWidget, QHBoxLayout, QVBoxLayout, QApplication
from qfluentwidgets import Pivot, SegmentedWidget, SegmentedToolWidget, SegmentedToggleToolWidget, FluentIconBase, \
    TabBar, FluentIcon, setTheme, Theme, TabCloseButtonDisplayMode, TitleLabel


class PivotNav(QWidget):
    """ 导航栏 """

    def __init__(self, parent: QWidget = None, nav: type[Pivot] = Pivot):
        super().__init__(parent)
        self.stackedWidget = QStackedWidget(self)
        self.__initNavigation(nav)

    def __initNavigation(self, nav: type[Pivot]):
        self.navigation = nav(self)
        mainLayout = QVBoxLayout(self)
        hLayout = QHBoxLayout()
        mainLayout.addLayout(hLayout)

        hLayout.addWidget(self.navigation, alignment=Qt.AlignmentFlag.AlignVCenter)
        mainLayout.addWidget(self.stackedWidget)

    def addItem(self, routeKey: str, text: str, widget: QWidget, icon: Union[QIcon, str, FluentIconBase] = None):
        self.stackedWidget.addWidget(widget)
        self.navigation.addItem(routeKey, text, lambda: self.stackedWidget.setCurrentWidget(widget), icon)
        return self

    def addItems(self, routeKeys: list[str], texts: list[str], widgets: list[QWidget],
                 icons: list[Union[QIcon, str, FluentIconBase]] = None):
        for key, text, widget in zip(routeKeys, texts, widgets):
            self.addItem(key, text, widget, icons[texts.index(text)] if icons else None)
        return self

    def setNavHeight(self, height: int):
        self.navigation.setFixedHeight(height)
        return self

    def setNavWidth(self, width: int):
        self.navigation.setFixedWidth(width)
        return self


class SegmentedNav(PivotNav):
    """ 分段导航 """

    def __init__(self, parent=None):
        super().__init__(parent, SegmentedWidget)


class SegmentedToolNav(PivotNav):
    """ 工具导航 """

    def __init__(self, parent=None, nav: type[Pivot] = SegmentedToolWidget):
        super().__init__(parent, nav)
        self.setNavWidth(0)

    def addToolItem(self, routeKey: str, icon: Union[QIcon, str, FluentIconBase], widget: QWidget):
        self.stackedWidget.addWidget(widget)
        self.navigation.addItem(routeKey, icon, lambda: self.stackedWidget.setCurrentWidget(widget))
        return self

    def addToolItems(self, routeKeys: list[str], icons: list[Union[QIcon, str, FluentIconBase]],
                     widgets: list[QWidget]):
        for key, icon, widget in zip(routeKeys, icons, widgets):
            self.addToolItem(key, icon, widget)
        return self


class SegmentedToggleToolNav(SegmentedToolNav):
    def __init__(self, parent=None):
        """ 主题色选中导航 """
        super().__init__(parent, SegmentedToggleToolWidget)


class LabelBarWidget(QWidget):
    """ 标签页组件 """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleBar = TabBar(self)
        self.stackedWidget = QStackedWidget(self)
        self.hLayout = QHBoxLayout(self)
        self.vLayout = QVBoxLayout()
        self.__initLayout_()
        self.__initTitleBar()

    def __initLayout_(self):
        self.hLayout.addLayout(self.vLayout)
        self.vLayout.addWidget(self.titleBar)
        self.vLayout.addWidget(self.stackedWidget)

    def __initTitleBar(self):
        self.titleBar.setTabShadowEnabled(True)
        self.titleBar.setMovable(True)
        self.titleBar.setScrollable(True)
        self.titleBar.setCloseButtonDisplayMode(TabCloseButtonDisplayMode.ON_HOVER)

        # self.tabCloseRequested.connect()

    def hideAddButton(self):
        self.titleBar.addButton.hide()
        return self

    def hideCloseButton(self):
        self.titleBar.setCloseButtonDisplayMode(TabCloseButtonDisplayMode.NEVER)
        return self

    def addTabWidget(self, routeKey, text, icon=None, widget: QWidget = None):
        self.__addWidget(widget)
        self.titleBar.addTab(routeKey, text, icon, lambda: self.stackedWidget.setCurrentWidget(widget))
        return self

    def __addWidget(self, widget: QWidget):
        self.stackedWidget.addWidget(widget)

    def addTabWidgets(self, routeKeys: list[str], texts: list[str], icons: list[Union[QIcon, str, FluentIconBase]] = None, widgets: list[QWidget] = None):
        if icons is None: icons = [None for _ in range(len(routeKeys))]
        for key, text, icon, widget in zip(routeKeys, texts, icons, widgets):
            self.addTabWidget(key, text, icon, widget)
        return self


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 380)
        self.tab = LabelBarWidget(self)
        self.tab.setFixedSize(self.width(), self.height())


        w1 = QWidget()
        t1 = TitleLabel("HOME", w1)
        l1 = QHBoxLayout(w1)
        l1.addWidget(t1)
        w1.setStyleSheet("background-color: red;")

        w2 = QWidget()
        t2 = TitleLabel("Music", w2)
        l2 = QHBoxLayout(w2)
        l2.addWidget(t2)
        w2.setStyleSheet("background-color: red;")

        self.tab.addTabWidget(
            'Home',
            "Home",
            FluentIcon.HOME,
            w1
        ).addTabWidget(
            "Music",
            "Music",
            FluentIcon.MUSIC,
            w2
        ).hideCloseButton().hideAddButton()

    def resizeEvent(self, event):
        self.tab.setFixedSize(self.width(), self.height())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Demo()
    setTheme(Theme.AUTO)
    w.show()
    sys.exit(app.exec())
