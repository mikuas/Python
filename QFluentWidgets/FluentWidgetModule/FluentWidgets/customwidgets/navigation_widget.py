import sys
from typing import Union

from PySide6.QtGui import Qt, QIcon
from PySide6.QtWidgets import QWidget, QStackedWidget, QHBoxLayout, QVBoxLayout, QApplication
from qfluentwidgets import Pivot, SegmentedWidget, SegmentedToolWidget, SegmentedToggleToolWidget, FluentIconBase, \
    TabBar, FluentIcon, setTheme, Theme


class PivotNav(QWidget):
    """ 导航栏 """
    def __init__(self, parent: QWidget = None, nav: type[Pivot] = Pivot):
        super().__init__(parent)
        self.__initStackedWidget()
        self.__initNavigation(nav)

    def __initNavigation(self, nav: type[Pivot]):
        self.navigation = nav(self)
        mainLayout = QVBoxLayout(self)
        hLayout = QHBoxLayout()
        mainLayout.addLayout(hLayout)

        hLayout.addWidget(self.navigation, alignment=Qt.AlignmentFlag.AlignVCenter)
        mainLayout.addWidget(self.stackedWidget)

    def __initStackedWidget(self):
        self.stackedWidget = QStackedWidget(self)

    def addItem(self, routeKey: str, text: str, widget: QWidget, icon: Union[QIcon, str, FluentIconBase] = None):
        self.stackedWidget.addWidget(widget)
        self.navigation.addItem(routeKey, text, lambda: self.stackedWidget.setCurrentWidget(widget), icon)
        return self

    def addItems(self, routeKeys: list[str], texts: list[str], widgets: list[QWidget],  icons: list[Union[QIcon, str, FluentIconBase]] = None):
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

    def addToolItems(self, routeKeys: list[str], icons: list[Union[QIcon, str, FluentIconBase]], widgets: list[QWidget]):
        for key, icon, widget in zip(routeKeys, icons, widgets):
            self.addToolItem(key, icon, widget)
        return self


class SegmentedToggleToolNav(SegmentedToolNav):
    def __init__(self, parent=None):
        """ 主题色选中导航 """
        super().__init__(parent, SegmentedToggleToolWidget)


class LabelBarWidget(TabBar):
    """ 标签页组件 """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTabShadowEnabled(True)
        self.setMovable(True)
        self.setScrollable(True)

        self.addButton.clicked.connect(
            lambda: print(True)
        )

    def addTabs(self):
        pass

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 380)
        lb = LabelBarWidget(self)
        lb.addTab(
            "T1",
            "Hello",
            FluentIcon.GITHUB,
            lambda: print(True)
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Demo()
    setTheme(Theme.AUTO)
    w.show()
    sys.exit(app.exec())