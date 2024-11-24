from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenuBar, QMenu
from qfluentwidgets import Action


class MenuBar(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)

    def addItem(self, title, icon=None, parent=None):
        # action = Action(icon, title, parent)
        action = Action(title, parent)
        # if icon:
        #     action.setIcon(icon)
        self.addAction(action)
        return action

    def addItems(self, titles, icons=None, parent=None):
        actions = []
        for title, icon in zip(titles, icons):
            actions.append(self.addItem(title, icon, parent))
        return actions

    def setTriggered(self, action: QAction | Action, fc):
        action.triggered.connect(fc)
        return self

    def setShortcut(self, action: QAction | Action, shortcut):
        action.setShortcut(shortcut)
        return self


class Menu(QMenu):
    def __init__(self, parent=None):
        super().__init__(parent)

    def addItem(self, title, icon=None, parent=None):
        action = Action(title, parent)
        if icon:
            action.setIcon(icon)
        self.addAction(action)
        return action

    def addItems(self, titles, icons=None, parent=None):
        actions = []
        for title, icon in zip(titles, icons):
            actions.append(self.addItem(title, icon, parent))
        return actions