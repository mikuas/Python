import sys

from PySide6.QtWidgets import QApplication, QMenu
from qfluentwidgets import Theme, setTheme, TitleLabel, FluentIcon, Action

from QFluentWidgets.FluentWidgetModule.FluentWidgets.customwidgets import PivotNav, SegmentedNav, SegmentedToolNav, \
    SegmentedToggleToolNav, Menu, setMenuWidget, ProfileCardMenu, CheckedMenuWidget
from QFluentWidgets.FluentWidgetModule.FluentWidgets.demo.demo1 import Demo as d

class Demo(SegmentedNav):
# class Demo(SegmentedToggleToolNav):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.d1 = d()
        self.d2 = d()
        self.d3 = d()
        self.d4 = d()
        self.d5 = d()
        self.d6 = d()
        self.initWindow()

        self.menu = ProfileCardMenu(r"C:\Users\Administrator\OneDrive\Pictures\ff.jpg", "miku", "None", self)
        self.menu.addMenuSeparator().addMenus([
            Action(FluentIcon.COPY, "Copy", triggered=lambda: print("Copy")),
            Action(FluentIcon.PASTE, "Past"),
            Action(FluentIcon.REMOVE, "Remove"),
        ]).addMenuSeparator().addSubMenus(
            "更多",
            [
                Action(FluentIcon.MUSIC, "Music"),
                Action(FluentIcon.VIDEO, "Video"),
                Action(FluentIcon.HOME, "Home")
            ]
        )

        self.ck = CheckedMenuWidget(self)
        self.ck.addCheckedMenu(
            "创建日期",
            FluentIcon.GITHUB
        )

    def initWindow(self):

        self.addItems(
            ['HOME', 'MUSIC', 'VIDEO', 'GAME', "VIEW", "GITHUB"],
            ['HOME', 'MUSIC', 'VIDEO', 'GAME', "VIEW", "GITHUB"],
            [self.d1, self.d2, self.d3, self.d4, self.d5, self.d6],
            [FluentIcon.HOME, FluentIcon.MUSIC, FluentIcon.VIDEO, FluentIcon.GAME, FluentIcon.VIEW, FluentIcon.GITHUB]
        ).navigation.setCurrentItem("HOME")

        # self.addToolItems(
        #     ['HOME', 'MUSIC', 'VIDEO', 'GAME', "VIEW", "GITHUB"],
        #     [FluentIcon.HOME, FluentIcon.MUSIC, FluentIcon.VIDEO, FluentIcon.GAME, FluentIcon.VIEW, FluentIcon.GITHUB],
        #     [self.d1, self.d2, self.d3, self.d4, self.d5, self.d6]
        # ).navigation.setCurrentItem("HOME")

    def contextMenuEvent(self, e):
        if setMenuWidget(self.d1.expandCard, self, e.pos()):
            self.ck.exec(e.globalPos())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Demo()
    w.resize(1200, 700)
    setTheme(Theme.AUTO)
    w.show()
    sys.exit(app.exec())