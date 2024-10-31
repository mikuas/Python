import sys
from symtable import Function

from PySide6.QtCore import QSize, QUrl
from PySide6.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QVBoxLayout, QWidget
from PySide6.QtGui import Qt
from qfluentwidgets import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 450)
        centerWindget = QWidget(self)
        mainLayout = QVBoxLayout(centerWindget)

        '''弹出组件'''
        self.button = PushButton("OUT", self)
        # self.button.clicked.connect(self.showFlyout)

        mainLayout.addWidget(self.button)
        self.setCentralWidget(centerWindget)
        # FlyoutViewBase

    def showFlyout(self):
        # InfoBarIcon
        Flyout.create(
            "Title",
            'Hello😊',
            FluentIcon.HOME,
            #显示图片
            image=r"C:\Users\Administrator\OneDrive\Pictures\27.jpg",
            target=self.button,
            parent=self,
            isClosable=True,
            aniType=FlyoutAnimationType.PULL_UP

        )

class CustomFlyoutView(FlyoutViewBase):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.vBoxLayout = QVBoxLayout(self)
        self.label = BodyLabel('这是一场「试炼」，我认为这就是一场为了战胜过去的「试炼」，\n只有战胜了那些幼稚的过去，人才能有所成长。')
        self.button = PrimaryPushButton('Action')

        self.button.setFixedWidth(140)

        self.vBoxLayout.setSpacing(12)
        self.vBoxLayout.setContentsMargins(20, 16, 20, 16)
        self.vBoxLayout.addWidget(self.label)
        self.vBoxLayout.addWidget(self.button)


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.button = PushButton("Click Me", self)
        self.button.clicked.connect(self.showFlyout)

        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.addWidget(self.button, 0, Qt.AlignCenter)
        self.resize(600, 500)

    def showFlyout(self):
        Flyout.make(CustomFlyoutView(), self.button, self, aniType=FlyoutAnimationType.PULL_UP)



class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 450)
        centerWindget = QWidget(self)
        mainLayout = QVBoxLayout(centerWindget)

        '''弹出组件'''
        self.button = PushButton("OUT", self)
        self.button.clicked.connect(self.showTeachingTip)

        mainLayout.addWidget(self.button)
        self.setCentralWidget(centerWindget)
        # PopupTeachingTip()

    def showTeachingTip(self):
        TeachingTip.create(
            # image='' 显示图片
            target=self.button,
            icon=InfoBarIcon.SUCCESS,
            title='Lesson 4',
            content="表达敬意吧，表达出敬意，然后迈向回旋的另一个全新阶段！",
            isClosable=True,
            tailPosition=TeachingTipTailPosition.BOTTOM,
            duration=2000, # 消失时间
            parent=self
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())