import sys

from PySide6.QtWidgets import QWidget, QApplication, QMenuBar
from qfluentwidgets import setTheme, Theme, CommandBar, Action, FluentIcon, PushButton, TransparentDropDownPushButton
from qfluentwidgets.components.widgets.command_bar import CommandMenu, RoundMenu


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 500)

        commandBar = CommandBar(self)
        commandBar.setMinimumWidth(500)
        commandBar.addActions([
            Action(FluentIcon.COPY, 'Copy', self),
            Action(FluentIcon.SAVE, 'Save', self),
            Action(FluentIcon.SAVE, 'Save', self),
            Action(FluentIcon.SAVE, 'Save', self),
        ]),
        commandBar.addSeparator()
        commandBar.addAction(
            Action(FluentIcon.PAUSE, 'Pause', self, checkable=True)
        )
        commandBar.addHiddenAction(
            Action(FluentIcon.SEND, 'Send', self)
        )

        button = TransparentDropDownPushButton(FluentIcon.MENU, "Menu")
        button.setFixedHeight(34)
        menu = RoundMenu(parent=self)
        menu.addActions([
            Action(FluentIcon.COPY, 'Copy', self),
            Action(FluentIcon.SAVE, 'Save', self),
            Action(FluentIcon.SAVE, 'Save', self),
        ])
        button.setMenu(menu)
        commandBar.addWidget(button)

    def contextMenuEvent(self, event):
        super().contextMenuEvent(event)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    setTheme(Theme.AUTO)
    window.show()
    sys.exit(app.exec())
