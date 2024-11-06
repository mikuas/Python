import sys

from PySide6.QtGui import Qt
from PySide6.QtNetwork import QAbstractSocket
from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout, QAbstractScrollArea
from qfluentwidgets import PipsPager, VBoxLayout, HorizontalPipsPager, SmoothScrollArea, VerticalPipsPager, \
    PipsScrollButtonDisplayMode


class ScrollWidget(QWidget):
    def __init__(self, text, parent=None):
        super().__init__(parent)

        self.initWindow()
        self.initWidget()

        self.setObjectName(text.replace(' ', '_'))

    def initWindow(self):
        self.vLayout = QVBoxLayout(self)
        self.vLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

    def initWidget(self):
        '''圆点分页组件'''
        self.pipsWidget = PipsPager(self)
        # 设置页数
        self.pipsWidget.setPageNumber(20)
        # 设置当前页码
        self.pipsWidget.setCurrentIndex(5)
        # 始终显示前进后退按钮
        self.pipsWidget.setNextButtonDisplayMode(PipsScrollButtonDisplayMode.ALWAYS)
        self.pipsWidget.setPreviousButtonDisplayMode(PipsScrollButtonDisplayMode.ALWAYS)

        '''水平圆点分页组件'''
        self.horizontalWidget = HorizontalPipsPager(self)
        self.horizontalWidget.setPageNumber(20)

        '''垂直圆点分页组件'''
        self.verticalWidget = VerticalPipsPager(self)
        self.verticalWidget.setPageNumber(20)

        '''滚动条'''
        # ScrollBar()

        '''平滑滚动条'''
        # SmoothScrollBar()

        '''平滑滚动条代理'''
        # SmoothScrollDelegate()

        '''平滑滚动区域'''
        # ScrollArea()

        '''单方向平滑滚动区域'''
        # SingleDirectionScrollArea()

        '''使用动画实现的平湖滚动区域'''
        # SmoothScrollArea()


    def initLayout(self):
        self.vLayout.addWidget(self.pipsWidget)
        self.vLayout.addWidget(self.horizontalWidget)
        self.vLayout.addWidget(self.verticalWidget)


class CustomSmoothScrollArea(SmoothScrollArea):
    def __init__(self, text, parent=None):
        super().__init__(parent)

        self.initWindow()

        self.setObjectName(text.replace(' ', '_'))

    def initWindow(self):
        self.scrollWidget = QWidget()
        self.vLayout = VBoxLayout(self.scrollWidget)
        self.vLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ScrollWidget('')
    w.resize(1000, 600)
    w.show()
    sys.exit(app.exec())