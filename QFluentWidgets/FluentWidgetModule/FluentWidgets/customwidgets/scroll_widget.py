from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout
from qfluentwidgets import VBoxLayout, SingleDirectionScrollArea, SmoothScrollArea


class OneWayScrollWidget(SingleDirectionScrollArea):
    """ 单向滚动部件 """
    def __init__(self, parent=None, orient=Qt.Orientation.Horizontal):
        super().__init__(parent, orient)
        self.__initWidget(orient)

        # 取消平滑滚动
        # self.setSmoothMode(SmoothMode.NO_SMOOTH)

    def __initWidget(self, orient):
        self.widget = QWidget()
        if orient == Qt.Orientation.Horizontal:
            self.layout = QHBoxLayout(self.widget)
        elif orient == Qt.Orientation.Vertical:
            self.layout = VBoxLayout(self.widget)
        self.setWidget(self.widget)
        self.setWidgetResizable(True)


class SmoothScrollWidget(SmoothScrollArea):
    """ 平滑双向滚动小部件 """
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__initWidget()

    def __initWidget(self):
        self.widget = QWidget()
        self.vLayout = VBoxLayout(self.widget)
        self.hLayout = QHBoxLayout(self.widget)
        self.vLayout.addLayout(self.hLayout)
        self.setWidget(self.widget)
        self.vLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setWidgetResizable(True)