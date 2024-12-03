import sys

from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QApplication, QStackedWidget
from qfluentwidgets import PipsPager, setTheme, Theme, PipsScrollButtonDisplayMode, TitleLabel, PrimaryPushButton, \
    LineEdit, Slider, NavigationPanel, FluentIcon, NavigationWidget, Action, NavigationInterface, NavigationBar, \
    NavigationItemPosition, NavigationTreeWidgetBase
from qfluentwidgets.components.navigation.navigation_widget import NavigationFlyoutMenu, NavigationTreeWidget

from QFluentWidgets.FluentWidgetModule.FluentWidgets import VBoxLayout, HBoxLayout, SmoothScrollWidget, \
    NavigationWidget, WinFluentIcon, NavigationBarWidget
from QFluentWidgets.FluentWidgetModule.App import SettingWidget


class HorizontalPager(PipsPager):
    """ 水平分页器 """
    def __init__(self, parent=None, orientation=Qt.Orientation.Horizontal):
        super().__init__(orientation, parent)
        self.__initStaticWidget()
        self.currentIndexChanged.connect(lambda index: self.stackedWidget.setCurrentIndex(index))
        self.__widgets = [] # type: [QWidget]

    def __initStaticWidget(self):
        self.stackedWidget = QStackedWidget(self)

    def addWidget(self, widget: QWidget):
        self.stackedWidget.addWidget(widget)
        self.addToWidgets(widget)
        self.setPageNumber(len(self.__widgets))
        return self

    def addWidgets(self, widgets: list[QWidget]):
        for widget in widgets:
            self.addWidget(widget)
        return self

    def setCurrentIndex(self, index: int):
        super().setCurrentIndex(index)
        self.stackedWidget.setCurrentIndex(index)
        return self

    def removeWidget(self, index: int):
        if index < len(self.__widgets):
            self.stackedWidget.removeWidget(self.__widgets.pop(index))
            self.setPageNumber(len(self.__widgets))
        return self

    def addToWidgets(self, widget: QWidget):
        self.__widgets.append(widget)
        return self

    def displayNextButton(self):
        self.setNextButtonDisplayMode(PipsScrollButtonDisplayMode.ALWAYS)
        return self

    def displayPrevButton(self):
        self.setPreviousButtonDisplayMode(PipsScrollButtonDisplayMode.ALWAYS)
        return self

    def hoverDisplayPrevButton(self):
        self.setPreviousButtonDisplayMode(PipsScrollButtonDisplayMode.ON_HOVER)
        return self

    def hoverDisplayNextButton(self):
        self.setNextButtonDisplayMode(PipsScrollButtonDisplayMode.ON_HOVER)
        return self

    def setStackedFixedWidth(self, width: int):
        self.stackedWidget.setFixedWidth(width)
        return self

    def setStackedFixedHeight(self, height: int):
        self.stackedWidget.setFixedHeight(height)
        return self

    def setStackedFixedSize(self, width: int, height: int):
        self.stackedWidget.setFixedSize(width, height)
        return self

    def setStackedMinWidth(self, width: int):
        self.stackedWidget.setMinimumWidth(width)
        return self

    def setStackedMinHeight(self, height: int):
        self.stackedWidget.setMinimumHeight(height)
        return self

    def setStackedMinSize(self, width: int, height: int):
        self.stackedWidget.setMinimumSize(width, height)
        return self


class VerticalPager(HorizontalPager):
    """ 垂直分页器 """
    def __init__(self, parent=None):
        super().__init__(parent, Qt.Orientation.Vertical)


class HorizontalPagerWidget(QWidget):
    """ 水平分页器组件 """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pager = HorizontalPager(self)
        self.__initLayout()

    def __initLayout(self):
        self.__vLayout = VBoxLayout(self)
        self.__vLayout.addWidgets_(
            [self.pager.stackedWidget, self.pager],
            [1, 0],
            [Qt.AlignmentFlag.AlignTop, Qt.AlignmentFlag.AlignCenter]
        )


class VerticalPagerWidget(QWidget):
    """ 垂直分页器组件 """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pager = VerticalPager(self)
        self.__initLayout()

    def __initLayout(self):
        self.__hLayout = HBoxLayout(self)
        self.__hLayout.addWidgets_(
            [self.pager.stackedWidget, self.pager],
            [1, 0],
            [Qt.AlignmentFlag.AlignTop, Qt.AlignmentFlag.AlignHCenter]
        )


class Demo(NavigationWidget):
# class Demo(NavigationBarWidget):
    def __init__(self):
        super().__init__()
        tree = NavigationTreeWidget(FluentIcon.GITHUB, 'Tree', True, self)
        tree.addChild()
        self.navigation.addWidget(
            'rot',
            tree,
            lambda: print("Tree"),
        )
        # self.resize(800, 600)
        self.addSubInterface(
            's1',
            FluentIcon.HOME,
            'Home',
            TitleLabel("HomeInterface", self),
            # FluentIcon.HOME_FILL
        ).addSubInterface(
            's2',
            WinFluentIcon.SETTING,
            "Setting",
            TitleLabel("SettingInterface", self),
        ).addSubInterface(
            's3',
            WinFluentIcon.MENU,
            "Menu",
            SettingWidget("SETTING", self)
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    setTheme(Theme.AUTO)
    demo.show()
    sys.exit(app.exec())