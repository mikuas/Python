from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QSystemTrayIcon
from qfluentwidgets import SystemTrayMenu, Action, FluentIconBase


class SystemTrayIcon(QSystemTrayIcon):

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.menu = SystemTrayMenu(parent=parent)
        self.setContextMenu(self.menu)

    def setIcon(self, icon: str | QIcon | FluentIconBase) -> "SystemTrayIcon":
        super().setIcon(icon)
        return self

    def addMenu(self, action: QAction | Action):
        self.menu.addAction(action)
        return self

    def addMenus(self, actions: list[QAction] | list[QAction]):
        self.menu.addActions(actions)
        self.setContextMenu(self.menu)
        return self
