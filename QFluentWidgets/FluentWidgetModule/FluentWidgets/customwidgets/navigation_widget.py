import sys
from typing import Union

from FluentWidgets import HBoxLayout, ButtonCard
from PySide6.QtCore import QSize, QRect
from PySide6.QtGui import Qt, QIcon
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QApplication
from qfluentwidgets import Pivot, SegmentedWidget, SegmentedToolWidget, SegmentedToggleToolWidget, FluentIconBase, \
    TabBar, TabCloseButtonDisplayMode, PopUpAniStackedWidget, TitleLabel, FluentIcon, Theme, setTheme, VBoxLayout, \
    FluentTitleBar, SwitchSettingCard, ScrollArea
from qfluentwidgets.components.widgets.frameless_window import FramelessWindow
from qfluentwidgets.window.fluent_window import FluentWindowBase
from qframelesswindow import AcrylicWindow


class NavigationBase(FluentWindowBase):
    """ 导航组件基类 """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setContentsMargins(0, 50, 0, 0)
        self.stackedWidget = PopUpAniStackedWidget(self)
        self.navigation = None

    def _initLayout(self):
        self.vLayout = VBoxLayout(self)
        self.hLayout = HBoxLayout()
        self.hBoxLayout.addLayout(self.vLayout)
        self.vLayout.addWidget(self.navigation, alignment=Qt.AlignmentFlag.AlignVCenter)
        self.vLayout.addLayout(self.hLayout)
        self.hLayout.addWidget(self.stackedWidget)

    def switchTo(self, widget: QWidget):
        self.stackedWidget.setCurrentWidget(widget)

    def addSubInterface(self, routeKey: str, text: str, widget: QWidget, icon: Union[QIcon, str, FluentIconBase] = None):
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
        for key, text, widget in zip(routeKeys, texts, widgets):
            self.addSubInterface(key, text, widget, icons[texts.index(text)] if icons else None)
        return self

    def setCurrentItem(self, routeKey: str):
        self.navigation.setCurrentItem(routeKey)
        return self

    def setNavHeight(self, height: int):
        self.navigation.setFixedHeight(height)
        return self

    def setNavWidth(self, width: int):
        self.navigation.setFixedWidth(width)
        return self


class PivotNav(NavigationBase):
    """ 导航栏 """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitleBar(FluentTitleBar(self))
        self.setWindowTitle("Navigation")
        self.navigation = Pivot(self)
        super()._initLayout()


class SegmentedNav(PivotNav):
    """ 分段导航 """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.navigation = SegmentedWidget(self)


class SegmentedToolNav(PivotNav):
    """ 工具导航 """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setNavWidth(0)
        self.navigation = SegmentedToolWidget(self)

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
    def __init__(self, text: str, parent=None):
        """ 主题色选中导航 """
        super().__init__(text, parent, SegmentedToggleToolWidget)


class LabelBarWidget(QWidget):
    """ 标签页组件 """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleBar = TabBar(self)
        self.stackedWidget = PopUpAniStackedWidget(self)
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

    def addTabWidgets(
            self, routeKeys: list[str],
            texts: list[str],
            icons: list[Union[QIcon, str, FluentIconBase]] = None,
            widgets: list[QWidget] = None
    ):
        if icons is None: icons = [None for _ in range(len(routeKeys))]
        for key, text, icon, widget in zip(routeKeys, texts, icons, widgets):
            self.addTabWidget(key, text, icon, widget)
        return self


class Widget(QWidget):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setObjectName(text)
        self.vLayout = QVBoxLayout(self)
        s = ScrollArea(self)
        for i in range(10):
            self.vLayout.addWidget(
                ButtonCard(
                    FluentIcon.HOME,
                    'home',
                    'content',
                    'OK'
                )
            )

class Demo(PivotNav):
    def __init__(self):
        super().__init__()
        self.resize(800, 520)
        from QFluentWidgets.StatusInfoWidget import StatusInfoWidget

        self.addSubInterfaces(
            ['r1', 'r2'],
            ['home', 'music'],
            [StatusInfoWidget("home", self), Widget('music', self)],
            # [FluentIcon.HOME, FluentIcon.MUSIC]
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Demo()
    setTheme(Theme.AUTO)
    window.show()
    sys.exit(app.exec())
