from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QSystemTrayIcon
from qfluentwidgets import SystemTrayMenu, Action, FluentIconBase
from .fluent_icon import Icon


class SystemTrayIcon(QSystemTrayIcon):
    """ 系统托盘图标 """

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.menu = SystemTrayMenu(parent=parent)
        self.setContextMenu(self.menu)

    def setIcon(self, icon: str | QIcon | FluentIconBase):
        super().setIcon(Icon(icon))
        return self

    def addAction(self, action: QAction | Action):
        self.menu.addAction(action)
        return self

    def addActions(self, actions: list[QAction] | list[QAction]):
        self.menu.addActions(actions)
        self.setContextMenu(self.menu)