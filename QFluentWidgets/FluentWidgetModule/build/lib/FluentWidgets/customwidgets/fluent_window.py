# coding:utf-8
from typing import Union
import sys

from .layout import HBoxLayout, VBoxLayout
from PySide6.QtCore import Qt, QSize, QRect
from PySide6.QtGui import QIcon, QPainter, QColor
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QApplication
from qfluentwidgets import FluentStyleSheet, qconfig, FluentIconBase, NavigationItemPosition, qrouter, isDarkTheme, \
    NavigationInterface, NavigationTreeWidget, SplitTitleBar
from qfluentwidgets.common.animation import BackgroundAnimationWidget
from qfluentwidgets.components.widgets.frameless_window import FramelessWindow
from qfluentwidgets.window.stacked_widget import StackedWidget

from qframelesswindow import TitleBar, TitleBarBase


class FluentWindowBase(BackgroundAnimationWidget, FramelessWindow):
    """ Fluent window base class """

    def __init__(self, parent=None):
        self._isMicaEnabled = False
        self._lightBackgroundColor = QColor(240, 244, 249)
        self._darkBackgroundColor = QColor(32, 32, 32)
        super().__init__(parent=parent)

        self.vBoxLayout = VBoxLayout(self)
        self.hBoxLayout = HBoxLayout()
        self.vBoxLayout.addLayout(self.hBoxLayout)
        self.stackedWidget = StackedWidget(self)
        self.navigationInterface = None

        # initialize layout
        self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)

        FluentStyleSheet.FLUENT_WINDOW.apply(self.stackedWidget)

        # enable mica effect on win11
        self.setMicaEffectEnabled(True)

        # show system title bar buttons on macOS
        if sys.platform == "darwin":
            self.setSystemTitleBarButtonVisible(True)

        qconfig.themeChangedFinished.connect(self._onThemeChangedFinished)

    def addSubInterface(
            self,
            interface: QWidget,
            icon: Union[FluentIconBase, QIcon, str],
            text: str,
            position=NavigationItemPosition.TOP
    ):
        """ add sub interface """
        raise NotImplementedError

    def switchTo(self, interface: QWidget):
        self.stackedWidget.setCurrentWidget(interface, popOut=False)

    def _onCurrentInterfaceChanged(self, index: int):
        widget = self.stackedWidget.widget(index)
        self.navigationInterface.setCurrentItem(widget.objectName())
        qrouter.push(self.stackedWidget, widget.objectName())

        self._updateStackedBackground()

    def _updateStackedBackground(self):
        isTransparent = self.stackedWidget.currentWidget().property("isStackedTransparent")
        if bool(self.stackedWidget.property("isTransparent")) == isTransparent:
            return

        self.stackedWidget.setProperty("isTransparent", isTransparent)
        self.stackedWidget.setStyle(QApplication.style())

    def setCustomBackgroundColor(self, light, dark):
        """ set custom background color """
        self._lightBackgroundColor = QColor(light)
        self._darkBackgroundColor = QColor(dark)
        self._updateBackgroundColor()

    def _normalBackgroundColor(self):
        if not self.isMicaEffectEnabled():
            return self._darkBackgroundColor if isDarkTheme() else self._lightBackgroundColor

        return QColor(0, 0, 0, 0)

    def _onThemeChangedFinished(self):
        if self.isMicaEffectEnabled():
            self.windowEffect.setMicaEffect(self.winId(), isDarkTheme())

    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QPainter(self)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(self.backgroundColor)
        painter.drawRect(self.rect())

    def setMicaEffectEnabled(self, isEnabled: bool):
        """ set whether the mica effect is enabled, only available on Win11 """
        if sys.platform != 'win32' or sys.getwindowsversion().build < 22000:
            return

        self._isMicaEnabled = isEnabled

        if isEnabled:
            self.windowEffect.setMicaEffect(self.winId(), isDarkTheme())
        else:
            self.windowEffect.removeBackgroundEffect(self.winId())

        self.setBackgroundColor(self._normalBackgroundColor())

    def isMicaEffectEnabled(self):
        return self._isMicaEnabled

    def systemTitleBarRect(self, size: QSize) -> QRect:
        """ Returns the system title bar rect, only works for macOS """
        return QRect(size.width() - 75, 0 if self.isFullScreen() else 9, 75, size.height())

    def setTitleBar(self, titleBar):
        super().setTitleBar(titleBar)

        # hide title bar buttons on macOS
        if sys.platform == "darwin" and self.isSystemButtonVisible() and isinstance(titleBar, TitleBarBase):
            titleBar.minBtn.hide()
            titleBar.maxBtn.hide()
            titleBar.closeBtn.hide()


class FluentTitleBar(TitleBar):
    """ Fluent title bar"""

    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedHeight(48)
        self.hBoxLayout.removeWidget(self.minBtn)
        self.hBoxLayout.removeWidget(self.maxBtn)
        self.hBoxLayout.removeWidget(self.closeBtn)

        # add window icon
        self.iconLabel = QLabel(self)
        self.iconLabel.setFixedSize(18, 18)
        self.hBoxLayout.insertWidget(0, self.iconLabel, 0, Qt.AlignLeft | Qt.AlignVCenter)
        self.window().windowIconChanged.connect(self.setIcon)

        # add title label
        self.titleLabel = QLabel(self)
        self.hBoxLayout.insertWidget(1, self.titleLabel, 0, Qt.AlignLeft | Qt.AlignVCenter)
        self.titleLabel.setObjectName('titleLabel')
        self.window().windowTitleChanged.connect(self.setTitle)

        self.vBoxLayout = QVBoxLayout()
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setSpacing(0)
        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonLayout.setAlignment(Qt.AlignTop)
        self.buttonLayout.addWidget(self.minBtn)
        self.buttonLayout.addWidget(self.maxBtn)
        self.buttonLayout.addWidget(self.closeBtn)
        self.vBoxLayout.addLayout(self.buttonLayout)
        self.vBoxLayout.addStretch(1)
        self.hBoxLayout.addLayout(self.vBoxLayout, 0)

        FluentStyleSheet.FLUENT_WINDOW.apply(self)

    def setTitle(self, title):
        self.titleLabel.setText(title)
        self.titleLabel.adjustSize()

    def setIcon(self, icon):
        self.iconLabel.setPixmap(QIcon(icon).pixmap(18, 18))


class FluentWindow(FluentWindowBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitleBar(FluentTitleBar(self))
        self.navigationInterface = NavigationInterface(self, showReturnButton=True)
        self.navigationInterface.setAcrylicEnabled(True)
        self.navigationInterface.setExpandWidth(250)
        self.navigationInterface.setMinimumExpandWidth(1500)
        self.widgetLayout = HBoxLayout()

        # initialize layout
        self.hBoxLayout.addWidget(self.navigationInterface)
        self.hBoxLayout.addLayout(self.widgetLayout)
        self.hBoxLayout.setStretchFactor(self.widgetLayout, 1)

        self.widgetLayout.addWidget(self.stackedWidget)
        self.widgetLayout.setContentsMargins(0, 48, 0, 0)

        self.navigationInterface.displayModeChanged.connect(self.titleBar.raise_)
        self.titleBar.raise_()

    def addSubInterface(
            self,
            interface: QWidget,
            icon: Union[FluentIconBase, QIcon, str],
            text: str,
            position=NavigationItemPosition.TOP,
            parent=None,
            isTransparent=False
    ) -> NavigationTreeWidget:
        """ add sub interface, the object name of `interface` should be set already """
        if not interface.objectName():
            raise ValueError("The object name of `interface` can't be empty string.")
        if parent and not parent.objectName():
            raise ValueError("The object name of `parent` can't be empty string.")

        interface.setProperty("isStackedTransparent", isTransparent)
        self.stackedWidget.addWidget(interface)

        # add navigation item
        routeKey = interface.objectName()
        item = self.navigationInterface.addItem(
            routeKey=routeKey,
            icon=icon,
            text=text,
            onClick=lambda: self.switchTo(interface),
            position=position,
            tooltip=text,
            parentRouteKey=parent.objectName() if parent else None
        )

        # initialize selected item
        if self.stackedWidget.count() == 1:
            self.stackedWidget.currentChanged.connect(self._onCurrentInterfaceChanged)
            self.navigationInterface.setCurrentItem(routeKey)
            qrouter.setDefaultRouteKey(self.stackedWidget, routeKey)

        self._updateStackedBackground()
        return item

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.titleBar.move(46, 0)
        self.titleBar.resize(self.width() - 46, self.titleBar.height())


class SplitFluentWindow(FluentWindow):
    """ 拆分流畅窗口 """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitleBar(SplitTitleBar(self))

        if sys.platform == "darwin":
            self.titleBar.setFixedHeight(48)

        self.widgetLayout.setContentsMargins(0, 0, 0, 0)

        self.titleBar.raise_()
        self.navigationInterface.displayModeChanged.connect(self.titleBar.raise_)