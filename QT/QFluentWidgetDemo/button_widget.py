import sys
from symtable import Function

from PySide6.QtCore import QSize, QUrl
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget
from PySide6.QtGui import Qt
from qfluentwidgets import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 450)
        centerWindget = QWidget(self)
        mainLayout = QVBoxLayout(centerWindget)

        '''不带图标的按钮'''
        # PrimaryPushButton()
        # PrimaryToolButton()
        # TransparentPushButton()
        # TransparentToolButton()
        self.button1 = PushButton(self)
        self.button1.setText("不带图标的按钮")
        # 带图标的按钮
        self.button2 = PushButton(self)
        self.button2.setIcon(FluentIcon.HOME)
        self.button2.setText("带图标的按钮")

        # 只显示图标
        self.button3 = ToolButton(self)
        self.button3.setIcon(FluentIcon.GITHUB)
        self.button3.setFixedSize(100, 100)
        self.button3.setIconSize(QSize(100, 100))

        '''实现链接跳转的按钮'''
        # 带图标
        self.button4 = HyperlinkButton(FluentIcon.LINK, "https://www.github.com/mikuas", "点击跳转", self)
        self.button4.setIcon(FluentIcon.LINK)
        # 不带图标
        self.button5 = HyperlinkButton(self)
        self.button5.setText("不带图标的链接")
        # 设置超链接
        self.button5.setUrl(QUrl('https://www.bilibili.com'))
        self.button5.setUrl(QUrl('https://www.bilibili.com'))

        '''状态开关按钮'''
        # ToggleToolButton()
        # TransparentToolButton()
        # TransparentPushButton()
        self.button6 = TogglePushButton(self)
        self.button6.setText("Statys Button")
        self.button6.setIcon(FluentIcon.SEND)
        # 状态改变信号插槽
        self.button6.toggled.connect(lambda: print("Click"))

        '''标签 过滤'''
        # PillToolButton()
        self.button7 = PillPushButton(self)
        self.button7.setIcon(FluentIcon.PLAY)
        self.button7.setText("Label")

        '''下拉菜单按钮'''
        # PrimaryDropDownButtonBase()
        # PrimaryDropDownPushButton()
        # TransparentDropDownPushButton()
        # TransparentDropDownToolButton()
        # DropDownToolButton()
        self.button8 = DropDownPushButton(FluentIcon.MAIL, "Email")
        # 子类必须是 RoundMenu 及其子类
        menu = RoundMenu(self.button8)
        menu.addAction(Action(FluentIcon.BASKETBALL, 'Basketball', triggered=lambda: print("你干嘛~")))
        menu.addAction(Action(FluentIcon.ALBUM, 'Sing', triggered=lambda: print("喜欢唱跳RAP")))
        menu.addAction(Action(FluentIcon.MUSIC, 'Music', triggered=lambda: print("只因你太美")))

        # 添加菜单
        self.button8.setMenu(menu)

        '''拆分按钮'''
        # SplitToolButton()
        # PrimarySplitPushButton()
        # PrimarySplitToolButton()
        # SplitPushButton 由两个按钮组成，点击左侧按钮会触发 clicked 信号
        # 点击右侧按钮可弹出下拉菜单，且下拉菜单必须是 RoundMenu 及其子类
        self.button9 = SplitPushButton(self)
        self.button9.setIcon(FluentIcon.HOME)
        self.button9.clicked.connect(lambda: print("Click"))
        self.button9.setText("HOME")
        # 子类必须是 RoundMenu 及其子类
        menu2 = RoundMenu(self.button9)
        menu2.addAction(Action(FluentIcon.BASKETBALL, 'Basketball', triggered=lambda: print("Home")))
        menu2.addAction(Action(FluentIcon.ALBUM, 'Sing', triggered=lambda: print("2")))
        menu2.addAction(Action(FluentIcon.MUSIC, 'Music', triggered=lambda: print("3")))

        self.button9.setFlyout(menu2)

        mainLayout.addWidget(self.button1)
        mainLayout.addWidget(self.button2)
        mainLayout.addWidget(self.button3)
        mainLayout.addWidget(self.button4)
        mainLayout.addWidget(self.button5)
        mainLayout.addWidget(self.button6)
        mainLayout.addWidget(self.button7)
        mainLayout.addWidget(self.button8)
        mainLayout.addWidget(self.button9)

        self.setCentralWidget(centerWindget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())