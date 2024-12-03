import sys

from PySide6.QtWidgets import QWidget, QApplication
from qfluentwidgets import NavigationBar, FluentIcon, setTheme, Theme, Action, TitleLabel, PrimaryPushButton
from QFluentWidgets.FluentWidgetModule.FluentWidgets import Menu, ProfileCardMenu, AcrylicMenu, VBoxLayout, HBoxLayout, \
    CheckedMenu, Shortcut, MenuIndicatorType, WinFluentIcon, CheckableMenu


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 500)
        self.vLayout = VBoxLayout(self)
        self.hLayout = HBoxLayout()
        self.vLayout.addLayout(self.vLayout)
        self.button = PrimaryPushButton("Profile Card", self)
        self.vLayout.addWidget(self.button)

        self.cm = CheckedMenu(self, MenuIndicatorType.CHECK)

        self.menu = AcrylicMenu(self)
        self.menu.addActions([
            Action(FluentIcon.GITHUB, "GITHUB", self, triggered=lambda: print("Github")),
            Action(FluentIcon.SETTING, "SETTING", self, triggered=lambda: print("Setting")),
            Action(FluentIcon.SEND, "SEND", self, triggered=lambda: print("Send")),
        ]).addSubActions(
            FluentIcon.MENU,
            'Sub',
            [Action(FluentIcon.HOME, "HOME", self, triggered=lambda: print("Home"))],
        )

        group = self.cm.createGroup()
        self.cm.setShortcuts(
            self.cm.addMenuToGroups(
                self.cm.createGroup(),
                self.cm.addCheckItems(
                    [FluentIcon.GITHUB, FluentIcon.SETTING, FluentIcon.SEND],
                    ["GITHUB", "SETTING", "SEND"]
                )
            ),
            ["Ctrl+U", "Ctrl+I", "Ctrl+T"]
        ).setShortcut(
            self.cm.setClicked(
                self.cm.addCheckItem(
                    FluentIcon.HOME,
                    "HOME",
                ),
                lambda: print('HOME')
            ),
            "Ctrl+P"
        ).setClickeds(
            self.cm.addMenuToGroups(
                group,
                self.cm.addSubCheckItems(
                    'Sub',
                    WinFluentIcon.WIN_11_LOG,
                    ["Item1", "Item2", "Item3"],
                    [WinFluentIcon.SEND, WinFluentIcon.FOLDER, WinFluentIcon.MORE],
                    indicatorType=MenuIndicatorType.CHECK
                )
            ),
            [
                lambda: print(self.cm.getCheckedAction(group)),
                lambda: print(self.cm.getCheckedAction(group)),
                lambda: print(self.cm.getCheckedAction(group))
            ]
        )

        self.button.clicked.connect(
            lambda: self.cm.execWidget(self.button)
        )

    def contextMenuEvent(self, event):
        super().contextMenuEvent(event)
        # self.menu.exec(event.globalPos())
        # self.pm.exec(event.globalPos())
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    setTheme(Theme.AUTO)
    window.show()
    sys.exit(app.exec())
