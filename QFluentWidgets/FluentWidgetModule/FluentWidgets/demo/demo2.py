import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import Qt, QShortcut, QKeySequence, QColor
from PySide6.QtWidgets import QApplication, QWidget
from qfluentwidgets import Theme, setTheme, FluentIcon, Action, qconfig, CommandBar, PrimaryPushButton

from QFluentWidgets.FluentWidgetModule.FluentWidgets import FlowLayoutWidget, Shortcut, FlipViewWidget
from QFluentWidgets.FluentWidgetModule.FluentWidgets.customwidgets import PivotNav, SegmentedNav, SegmentedToolNav, \
    SegmentedToggleToolNav, Menu, setMenuWidget, ProfileCardMenu, CheckedMenuWidget
from QFluentWidgets.FluentWidgetModule.FluentWidgets.demo.demo1 import Demo as d
from QT.QFluentWidget.Test.FlunetWindow import ImageWidget, SettingWidget, CardsWidget

from PyMyMethod.Method import FileControl


class Demo(SegmentedNav):
# class Demo(SegmentedToggleToolNav):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fc = FileControl()
        self.d1 = d()
        self.imgWidget = ImageWidget("IMAGE", self.fc.readJsonFiles('../../../data/json/data.json')['imgPath'], self)
        self.setWidget = SettingWidget("SETTING", qconfig.themeMode)
        self.cardWidget = CardsWidget("CARD", self)
        self.widget = Widget(self)
        self.d6 = d()
        self.initWindow()

        self.menu = ProfileCardMenu(r"C:\Users\Administrator\OneDrive\Pictures\ff.jpg", "miku", "None", self)
        self.menu.addSeparator().addMenus([
            Action(FluentIcon.COPY, "Copy", triggered=lambda: print("Copy")),
            Action(FluentIcon.PASTE, "Past", triggered=lambda: print("Past")),
            Action(FluentIcon.REMOVE, "Remove", triggered=lambda: print("Remove")),
        ]).addSeparator().addSubMenus(
            FluentIcon.MORE,
            "更多",
            [
                Action(FluentIcon.MUSIC, "Music", triggered=lambda: print("Music")),
                Action(FluentIcon.VIDEO, "Video", triggered=lambda: print("Video")),
                Action(FluentIcon.HOME, "Home", triggered=lambda: print("Home")),
            ]
        )

        self.checkMenu = CheckedMenuWidget(self)
        self.checkMenu.setTriggered(
            self.checkMenu.setShortcut(
                self.checkMenu.addMenuToGroup(self.checkMenu.createGroup(), self.checkMenu.addCheckedMenus(
                    ["Copy", "Past", "Home"],
                    [FluentIcon.COPY, FluentIcon.PASTE, FluentIcon.HOME]
                )[0]),
                ["Ctrl+C", "Ctrl+V", "Home"]
            ),
            [lambda b: print("Copy", b), lambda b: print("Past", b), lambda b: print("Home", b)],
        )
        self.checkMenu.setTriggered(
            self.checkMenu.setShortcut(
                self.checkMenu.addSubCheckedMenus(
                    "More",
                    FluentIcon.MORE,
                    ["Music", "Video", "Game"],
                    [FluentIcon.MUSIC, FluentIcon.VIDEO, FluentIcon.GAME]
                )[0],
                ["Music", "Video", "Game"]
            ),
            [lambda b: print("Music", b), lambda b: print("Video", b), lambda b: print("Game", b)],
        )

    def initWindow(self):

        self.addItems(
            ['HOME', 'MUSIC', 'VIDEO', 'GAME', "VIEW", "GITHUB"],
            ['HOME', 'MUSIC', 'VIDEO', 'GAME', "VIEW", "GITHUB"],
            [self.d1, self.imgWidget, self.setWidget, self.cardWidget, self.widget, self.d6],
            [FluentIcon.HOME, FluentIcon.MUSIC, FluentIcon.VIDEO, FluentIcon.GAME, FluentIcon.VIEW, FluentIcon.GITHUB]
        ).navigation.setCurrentItem("HOME")

    def contextMenuEvent(self, e):
        if setMenuWidget(self.imgWidget, self.imgWidget, e.pos()):
            self.menu.exec(e.globalPos())
        if setMenuWidget(self.setWidget.powerCard, self.setWidget, e.pos()):
            self.checkMenu.exec(e.globalPos())


class Widget(SegmentedToggleToolNav):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.widget = QWidget(self)
        cb = CommandBar(self.widget)
        cb.addActions([
            Action(FluentIcon.COPY, "Copy"),
            Action(FluentIcon.PASTE, "Past"),
            Action(FluentIcon.REMOVE, "Remove"),
        ])
        cb.addHiddenActions([
            Action(FluentIcon.MUSIC, "Music"),
            Action(FluentIcon.VIDEO, 'Video')
        ])
        cb.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        fw = FlowLayoutWidget(parent=self)
        for i in range(20):
            bt = PrimaryPushButton("Ciallo～(∠・ω< )⌒☆", self)
            bt.setMinimumSize(200, 120)
            fw.addWidget(bt)

        self.fly = FlipViewWidget(self)
        self.fly.setFixedSize(QSize(1200, 580))
        self.fly.setItemSize(QSize(1190, 580))
        self.fly.addImages([
            "C:\\Projects\\Items\\Python\\QFluentWidgets\\data\\images\\0.jpg",
            "C:\\Projects\\Items\\Python\\QFluentWidgets\\data\\images\\1.jpg",
            "C:\\Projects\\Items\\Python\\QFluentWidgets\\data\\images\\2.jpg",
            "C:\\Projects\\Items\\Python\\QFluentWidgets\\data\\images\\3.jpg",
            "C:\\Projects\\Items\\Python\\QFluentWidgets\\data\\images\\4.jpg",
            "C:\\Projects\\Items\\Python\\QFluentWidgets\\data\\images\\5.jpg"
        ]).setAutoPlay()
        # fly.setDelegate(QColor(255, 255, 255, 180), 24, QColor(11, 146, 234), "This is True Power \n This is True Image", 250)

        self.addToolItems(
            ["HOME", "MUSIC", "VIDEO", "GAME", "GITHUB"],
            [FluentIcon.HOME, FluentIcon.MUSIC, FluentIcon.VIDEO, FluentIcon.GAME, FluentIcon.GITHUB],
            [QWidget(), self.widget, fw, self.fly, QWidget()]
        )

        Shortcut().addShortcuts(
            ['Ctrl+A', "Ctrl+C", "Alt+C"],
            self,
            [lambda: print('Ctrl+A'), lambda: print('Ctrl+C'), lambda: print('Alt+C')],
        )

    def resizeEvent(self, e):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Demo()
    w.resize(1200, 700)
    setTheme(Theme.AUTO)
    w.show()
    sys.exit(app.exec())