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

        button = TransparentDropDownPushButton("文件")
        button2 = TransparentDropDownPushButton("工具")
        button3 = TransparentDropDownPushButton("更多")
        button.setFixedHeight(34)
        menu = RoundMenu(parent=self)
        menu.addActions([
            Action(FluentIcon.COPY, '文件', self),
            Action(FluentIcon.SAVE, '设置', self),
            Action(FluentIcon.SAVE, '工具', self),
        ])
        button.setMenu(menu)
        button2.setMenu(menu)
        button3.setMenu(menu)

        commandBar.addWidget(button)
        commandBar.addSeparator()
        commandBar.addWidget(button2)
        commandBar.addWidget(button3)

    def contextMenuEvent(self, event):
        super().contextMenuEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    setTheme(Theme.AUTO)
    window.show()
    sys.exit(app.exec())
