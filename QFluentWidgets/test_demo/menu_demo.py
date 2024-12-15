import sys

from FluentWidgets import VBoxLayout, AcrylicProfileCardMenu
from PySide6.QtWidgets import QWidget, QApplication

from qfluentwidgets import Theme, setTheme, FluentIcon, PrimaryPushButton, Action, RoundMenu
from qfluentwidgets.components.material import AcrylicMenu

from QFluentWidgets.FluentWidgetModule.FluentWidgets import (
    Menu, AcrylicRoundMenu,
    ProfileCardMenu, AcrylicProfileCardMenu,
    CheckedMenu, AcrylicCheckedMenu, Shortcut
)


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 520)
        self.vBoxLayout = VBoxLayout(self)
        self.vBoxLayout.setContentsMargins(300, 0, 300, 0)

        self.menu = Menu(self)
        # add items
        self.menu.addItems(
            [FluentIcon.COPY, FluentIcon.CUT, FluentIcon.PASTE],
            ["复制", "剪切", "粘贴"]
        )
        # add action
        self.menu.addAction(
            Action(FluentIcon.MORE, "More", self)
        )
        # add subItems
        self.menu.addSubItems(
            '更多',
            FluentIcon.CARE_RIGHT_SOLID,
            ['升序', '降序'],
            [FluentIcon.UP, FluentIcon.DOWN]
        )

        self.menu.addSubItem(
            'Sub Sub Item',
            FluentIcon.WIFI,
            'Sub Item 1',
            FluentIcon.PAUSE,
            self.menu.getSubMenu()
        )

        self.acrylicMenu = AcrylicRoundMenu(self)
        self.acrylicMenu.addItems(
            [FluentIcon.COPY, FluentIcon.CUT, FluentIcon.PASTE],
            ["复制", "剪切", "粘贴"]
        )
        self.acrylicMenu.addSubItems(
            'Sub Item',
            FluentIcon.MORE,
            ['Item 1', 'Item 2'],
            [FluentIcon.UP, FluentIcon.DOWN]
        )

        self.profileCardMenu = ProfileCardMenu(
            r"C:\Users\Administrator\OneDrive\Pictures\49.jpg", 'miku', '114514@gel.com',
            self, url='https://www.bilibili.com/'
        )
        self.profileCardMenu.addItems(
            [FluentIcon.COPY, FluentIcon.CUT, FluentIcon.PASTE],
            ["复制", "剪切", "粘贴"]
        )

        self.acrylicProfileCardMenu = AcrylicProfileCardMenu(
            r"C:\Users\Administrator\OneDrive\Pictures\49.jpg", 'miku', '114514@gel.com',
            self, url='https://www.bilibili.com/'
        )
        self.acrylicProfileCardMenu.setShortcuts(
            self.acrylicProfileCardMenu.addItems(
                [FluentIcon.COPY, FluentIcon.CUT, FluentIcon.PASTE],
                ["复制", "剪切", "粘贴"]
            ),
            ["Ctrl+C", "Ctrl+X", "Ctrl+V"]
        )

        self.checkedMenu = CheckedMenu(self)
        self.checkedMenu.addItems(
            [FluentIcon.COPY, FluentIcon.CUT, FluentIcon.PASTE],
            ["复制", "剪切", "粘贴"]
        )

        self.acrylicCheckedMenu = AcrylicCheckedMenu(self)
        self.acrylicCheckedMenu.addItems(
            [FluentIcon.COPY, FluentIcon.CUT, FluentIcon.PASTE],
            ["复制", "剪切", "粘贴"]
        )

        self.button1 = PrimaryPushButton("Click Me Show Menu", self)
        self.button1.clicked.connect(
            lambda: self.menu.execCenter(self.button1)
        )

        self.button2 = PrimaryPushButton("Click Me Show AcrylicRoundMenu", self)
        self.button2.clicked.connect(
            lambda: self.acrylicMenu.execCenter(self.button2)
        )

        self.button3 = PrimaryPushButton("Click Me Show ProfileCardMenu", self)
        self.button3.clicked.connect(
            lambda: self.profileCardMenu.execCenter(self.button3)
        )

        self.button4 = PrimaryPushButton("Click Me Show CheckedMenu", self)
        self.button4.clicked.connect(
            lambda: self.checkedMenu.execCenter(self.button4)
        )

        self.button5 = PrimaryPushButton("Click Me Show AcrylicCheckedMenu", self)
        self.button5.clicked.connect(
            lambda: self.acrylicCheckedMenu.execCenter(self.button5)
        )

        self.button6 = PrimaryPushButton("Ctrl+Q Exit App", self)
        self.shortcut = Shortcut()
        self.shortcut.addShortcut('Ctrl+Q', self.button6, QApplication.quit)

        self.vBoxLayout.addWidgets([
            self.button1, self.button2, self.button3, self.button4, self.button5, self.button6
        ])

    def contextMenuEvent(self, event):
        super().contextMenuEvent(event)
        self.acrylicProfileCardMenu.exec(event.globalPos())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    setTheme(Theme.AUTO)
    demo.show()
    sys.exit(app.exec())