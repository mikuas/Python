import sys

from PySide6.QtCore import Qt, QEasingCurve
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QApplication, QVBoxLayout
from qfluentwidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 垂直Qt.Vertical
        # 水平
        setTheme(Theme.DARK)
        self.resize(1000, 600)
        self.h = QHBoxLayout(self)
        self.qw = QWidget(self)
        self.h.addWidget(self.qw)
        self.qw.setFixedWidth(self.width())

        self.hLayout = QHBoxLayout(self.qw)
        self.vLayout = QVBoxLayout()
        self.hLayout.addLayout(self.vLayout)
        for i in range(15):
            cw = AppCard(
                FluentIcon.GITHUB,
                "Title",
                "Content",
                self
            )
            self.vLayout.addWidget(cw)
        self.sc = SingleDirectionScrollArea(
            self
        )
        self.sc.setWidget(self.qw)
        self.sc.setFixedSize(self.width(), self.height())
        # 水平方向有很多组件
        # self.view.setFixedSize(self.width(), self.height())
        # for i in range(20):
        #     layout.addWidget(QPushButton(f'按钮 {i}'))

        # sc.setWidget(self.view)

        # 默认情况下滚动区域的背景和边框不透明，如需改为透明背景并移除边框

        self.sc.setStyleSheet("QScrollArea{background: transparent; border: none}")
        self.sc.enableTransparentBackground()
        # 必须给内部的视图也加上透明背景样式
        self.qw.setStyleSheet("QWidget{background: transparent}")

        #  实现了水平和竖直方向的平滑滚动
        ScrollArea()
        # 取消平滑滚动的方法
        # self.sc.setSmoothMode(SmoothMode.NO_SMOOTH)

    def resizeEvent(self, event):
        self.sc.setFixedSize(self.width(), self.height())
        self.qw.setFixedWidth(self.width())
        pass

class AppCard(CardWidget):

    def __init__(self, icon, title, content, parent=None):
        super().__init__(parent)
        self.iconWidget = IconWidget(icon)
        self.titleLabel = BodyLabel(title, self)
        self.contentLabel = CaptionLabel(content, self)
        self.openButton = PushButton('Open', self)
        self.openButton.clicked.connect(
            lambda : print("Click")
        )
        self.moreButton = TransparentToolButton(FluentIcon.MORE, self)
        self.moreButton.clicked.connect(self.showFlyout)

        self.hBoxLayout = QHBoxLayout(self)
        self.vBoxLayout = QVBoxLayout()

        self.setFixedHeight(73)
        self.iconWidget.setFixedSize(48, 48)
        self.contentLabel.setTextColor("#606060", "#d2d2d2")
        self.openButton.setFixedWidth(120)

        self.hBoxLayout.setContentsMargins(20, 11, 11, 11)
        self.hBoxLayout.setSpacing(15)
        self.hBoxLayout.addWidget(self.iconWidget)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.addWidget(self.titleLabel, 0, Qt.AlignVCenter)
        self.vBoxLayout.addWidget(self.contentLabel, 0, Qt.AlignVCenter)
        self.vBoxLayout.setAlignment(Qt.AlignVCenter)
        self.hBoxLayout.addLayout(self.vBoxLayout)

        self.hBoxLayout.addStretch(1)
        self.hBoxLayout.addWidget(self.openButton, 0, Qt.AlignRight)
        self.hBoxLayout.addWidget(self.moreButton, 0, Qt.AlignRight)

        self.moreButton.setFixedSize(32, 32)

    def showFlyout(self):
        Flyout.create(
            "Title",
            '暂未编写该功能😓',
            InfoBarIcon.WARNING,
            target=self.moreButton,
            parent=self
        )


# 水平和竖直方向的平滑滚动
class Demo(SmoothScrollArea):

    def __init__(self):
        super().__init__()
        # 加载一张分辨率很高的图片
        self.label = ImageLabel(r"C:\Users\Administrator\OneDrive\Pictures\12.jpg")

        # 自定义平滑滚动动画
        self.setScrollAnimation(Qt.Vertical, 400, QEasingCurve.OutQuint)
        self.setScrollAnimation(Qt.Horizontal, 400, QEasingCurve.OutQuint)

        # 滚动到指定区域
        self.horizontalScrollBar().setValue(1900)

        self.setWidget(self.label)
        self.resize(1200, 800)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    setTheme(Theme.DARK)
    window.show()
    sys.exit(app.exec())
