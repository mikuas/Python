from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QSystemTrayIcon
from qfluentwidgets import SystemTrayMenu, Action, FluentIcon


class SystemTrayIcon(QSystemTrayIcon):

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setIcon(parent.windowIcon())

        self.menu = SystemTrayMenu(parent=parent)

    def setIcon(self, icon: QIcon | FluentIcon | str):
        self.setIcon(QIcon(icon))

    def addMenu(self, action: QAction | Action):
        self.menu.addAction(action)

    def addMenus(self, actions: list[QAction] | list[QAction]):
        self.menu.addActions(actions)
        self.setContextMenu(self.menu)
