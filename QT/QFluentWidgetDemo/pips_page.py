import sys

from PySide6.QtCore import Qt, QEasingCurve
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QApplication
from qfluentwidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        '''分页器'''
        pager = PipsPager(Qt.Horizontal, self)
        # 设置页数
        pager.setPageNumber(20)

        # 设置圆点数量
        pager.setVisibleNumber(8)

        # 始终显示前进和后退
        pager.setNextButtonDisplayMode(PipsScrollButtonDisplayMode.ALWAYS)
        pager.setPreviousButtonDisplayMode(PipsScrollButtonDisplayMode.ALWAYS)
        # 设置当前页码
        pager.setCurrentIndex(3)
        # 当页码发生改变会发出信号
        pager.currentIndexChanged.connect(lambda index: print(index, pager.currentIndex()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
