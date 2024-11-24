from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout
from qfluentwidgets import VBoxLayout, SingleDirectionScrollArea, SmoothScrollArea


class VerticalScrollWidget(SingleDirectionScrollArea):
    """ 平滑垂直滚动小部件 """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.__initWidget()

    def __initWidget(self):
        self.__widget = QWidget()
        self.vLayout = VBoxLayout(self.__widget)
        self.setWidget(self.__widget)
        self.vLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setWidgetResizable(True)


class HorizontalScrollWidget(SingleDirectionScrollArea):
    """ 平滑水平滚动小部件 """
    def __int__(self, parent: QWidget = None):
        super().__init__(parent, Qt.Orientation.Horizontal)
        self.__initWidget()

    def __initWidget(self):
        self.__widget = QWidget()
        self.hLayout = VBoxLayout(self.__widget)
        self.setWidget(self.__widget)
        self.hLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setWidgetResizable(True)


class SmoothScrollWidget(SmoothScrollArea):
    """ 平滑双向滚动小部件 """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initWidget()

    def __initWidget(self):
        self.__widget = QWidget()
        self.setWidget(self.__widget)
        self.setWidgetResizable(True)

    def createVBoxLayout(self):
        return VBoxLayout(self.__widget)

    def createHBoxLayout(self):
        return QHBoxLayout(self.__widget)