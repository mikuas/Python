# coding:utf-8
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from pyrect import TOPLEFT

from qfluentwidgets import *


class Demo(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # setTheme(Theme.DARK)
        hLayout = QHBoxLayout(self)
        layout = QVBoxLayout()
        hLayout.addLayout(layout)
        info = InfoBadge(level=InfoBadgePosition.LEFT)
        # 提示信息
        # info.info(1)
        # info.success(10)
        # info.attension(100)
        # info.warning(1000)
        # info.error(10000)
        # info.custom("1W+", '#005fb8', '#60cdff')


        # 附着在按钮上
        button = ToolButton(FluentIcon.GITHUB, self)
        button.setFixedSize(100, 60)
        # info.success(100, self, button)
        info.warning(100, self, button)
        button.clicked.connect(lambda : (print(True), info.error(-1, self, button)))

        layout.addWidget(button)
        self.resize(800, 300)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    sys.exit(app.exec())