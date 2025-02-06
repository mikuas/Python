# encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QGraphicsOpacityEffect, QPushButton
from PySide6.QtGui import QColor, QPalette
from PySide6.QtCore import QPropertyAnimation, QPoint, Qt, QEasingCurve, QSize, QRect
from qfluentwidgets import PrimaryPushButton, LineEdit, PushButton, TitleLabel, TransparentToolButton, FluentIcon
from FluentWidgets import VerticalScrollWidget, Widget, HBoxLayout, NavigationBar, VBoxLayout


class Window(Widget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self._isExpand = False
        self._expandWidth = 256
        self._collapsedWidth = 65

        self.layout = HBoxLayout(self)
        self.w = Widget(self)
        self.w.setDarkBackgroundColor('deeppink')
        self.w.setRadius(8, 8)
        self.btn = PushButton('expand', self)
        self.layout.addWidget(self.w)
        self.btn.clicked.connect(self.expandNavigation)
        self.layout.addWidget(self.btn)

        self._navLayout = VBoxLayout(self.w)
        self._returnButton = TransparentToolButton(FluentIcon.RETURN, self.w)
        self._expandButton = TransparentToolButton(FluentIcon.MENU, self.w)
        self._returnButton.setFixedSize(45, 35)
        self._expandButton.setFixedSize(45, 35)
        self._scrollWidget = VerticalScrollWidget(self.w)
        self.__expandNavAni = QPropertyAnimation(self.w, b'maximumWidth')
        # self.__expandNavAni = QPropertyAnimation(self.w, b'minimumWidth')

        self.__initScrollWidget()
        self.__initLayout()
        self.w.setMaximumWidth(self._collapsedWidth)
        self.__connectSignalSlot()

    def __initLayout(self):
        self._navLayout.addWidgets([self._returnButton, self._expandButton])

        self._topLayout = VBoxLayout()
        self._topLayout.setSpacing(5)
        self._topLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self._bottomLayout = VBoxLayout()
        self._navLayout.addLayout(self._topLayout)
        self._navLayout.addWidget(self._scrollWidget)
        self._navLayout.addLayout(self._bottomLayout)

    def __initScrollWidget(self):
        self._scrollWidget.enableTransparentBackground()
        self._scrollWidget.vBoxLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self._scrollWidget.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self._scrollWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._scrollWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

    def __connectSignalSlot(self):
        self._expandButton.clicked.connect(self.expandNavigation)

    def expandNavigation(self):
        """ expand navigation bar """
        if self._isExpand:
            self._isExpand = False
            width = self._collapsedWidth
            text = 'expand'
        else:
            self._isExpand = True
            width = self._expandWidth
            text = 'collapsed'
        self.btn.setText(text)
        self.__createExpandNavAni(width)

    def __createExpandNavAni(self, endValue):
        self.__expandNavAni.setDuration(120)
        self.__expandNavAni.setStartValue(self.w.width())
        self.__expandNavAni.setEndValue(endValue)
        self.__expandNavAni.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.resize(800, 500)
    window.show()
    sys.exit(app.exec())