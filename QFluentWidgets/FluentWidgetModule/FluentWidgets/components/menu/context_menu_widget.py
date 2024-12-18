# coding:utf-8
from typing import Union

from PySide6.QtCore import QPoint
from PySide6.QtGui import QColor, QActionGroup, QIcon, QShortcut, QKeySequence
from PySide6.QtWidgets import QWidget
from qfluentwidgets import (
    RoundMenu, Action, AvatarWidget, BodyLabel, CaptionLabel, setFont, HyperlinkButton, CheckableMenu,
    MenuIndicatorType, FluentIconBase
)
from qfluentwidgets.components.material import AcrylicMenu, AcrylicCheckableMenu


class MenuBase:
    # noinspection PyUnusedLocal
    def __init__(self, parent: QWidget = None):
        self._menu = None
        self._subMenu = None


    def addAction(self, action: Action):
        self._menu.addAction(action)
        return self

    def addActions(self, actions: list[Action]):
        for action in actions:
            self.addAction(action)
        return self

    def addItem(self, icon: Union[QIcon, str, FluentIconBase], text: str):
        """ add item to _menu"""
        action = Action(icon, text)
        self._menu.addAction(action)
        return action

    def addItems(self, icon: list[Union[QIcon, str, FluentIconBase]], text: list[str]):
        """ add items to _menu"""
        actions = []
        for icon, text in zip(icon, text):
            actions.append(self.addItem(icon, text))
        return actions

    def addSubItem(
            self,
            title: str,
            icon: Union[QIcon, str, FluentIconBase],
            text: str,
            subIcon: Union[QIcon, str, FluentIconBase],
            parentMenu: RoundMenu = None
    ) -> Action:
        """ parentMenu is None, default = self._menu """
        action = Action(icon, text)
        self._createSubMenu(subIcon, text, parentMenu).addMenu(self._subMenu)
        self._subMenu.addAction(action)
        return action

    def addSubItems(
            self,
            title: str,
            icon: Union[QIcon, str, FluentIconBase],
            text: list[str],
            subIcon: list[Union[QIcon, str, FluentIconBase]],
            parentMenu: RoundMenu = None,
    ) -> list[Action]:
        """ parentMenu is None, default = self._menu """
        actions = []
        self._createSubMenu(icon, title, parentMenu).addMenu(self._subMenu)
        for t, i in zip(text, subIcon):
            action = Action(i, t, checkable=True)
            self._subMenu.addAction(action)
            actions.append(action)
        return actions

    def _createSubMenu(self, icon: Union[QIcon, str, FluentIconBase], title: str, parentMenu: RoundMenu = None):
        parentMenu = parentMenu or self._menu
        self._subMenu = RoundMenu(title, parentMenu)
        self._subMenu.setIcon(icon)
        self.setSubMenuMinWidth(160)
        return parentMenu

    def addSubAction(self, icon: Union[QIcon, str, FluentIconBase], title: str, action: Action, parentMenu: RoundMenu = None):
        """ parentMenu is None, default = self._menu """
        self._createSubMenu(icon, title, parentMenu).addMenu(self._subMenu)
        self._subMenu.addAction(action)
        return self

    def addSubActions(self, icon: Union[QIcon, str, FluentIconBase], title: str, actions: list[Action], parentMenu: RoundMenu = None):
        """ parentMenu is None, default = self._menu """
        self._createSubMenu(icon, title, parentMenu).addMenu(self._subMenu)
        self._subMenu.addActions(actions)
        return self

    def exec(self, position: QPoint):
        self._menu.exec(position)

    def execWidgetCenter(self, widget: QWidget):
        """ 在指定组件中心执行 """
        self._menu.exec(widget.mapToGlobal(widget.rect().center()))

    def getSubMenu(self):
        return self._subMenu

    def addSeparator(self):
        self._menu.addSeparator()
        return self

    def addSubSeparator(self, subMenu: RoundMenu = None):
        """ subMenu is None, default = self._subMenu """
        subMenu = subMenu or self._subMenu
        subMenu.addSeparator()
        return self

    def setMenuMinWidth(self, width: int):
        self._menu.setMinimumWidth(width)
        self._menu.view.setMinimumWidth(width - 20)
        return self

    def setSubMenuMinWidth(self, width: int, menu: RoundMenu = None):
        """ menu is None, default = self._subMenu """
        menu = menu or self._subMenu
        menu.setMinimumWidth(width)
        menu.view.setMinimumWidth(width - 20)
        return self

    @staticmethod
    def setClickedSlot(action: Action, func):
        """ set click method """
        action.triggered.connect(func)
        return action

    @staticmethod
    def setClickedSlots(actions: list[Action], function: list):
        for action, fc in zip(actions, function):
            action.triggered.connect(fc)
        return actions

    def setShortcut(self, action: Action, key: str):
        """ set shortcut """
        action.setShortcut(QKeySequence(key))
        return self

    def setShortcuts(self, actions: list[Action], keys: list[str]):
        for action, key in zip(actions, keys):
            action.setShortcut(key)
        return self

    def removeMenu(self):
        self._menu.removeMenu()
        return self

    def removeAction(self):
        self._menu.removeAction()
        return self


class Menu(MenuBase):
    """ 菜单栏组件 """
    def __init__(self, parent=None):
        super().__init__()
        self.menu = RoundMenu(parent=parent)
        self.setMenuMinWidth(160)


class AcrylicRoundMenu(Menu):
    """ 亚力克菜单 """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.menu = AcrylicMenu('', parent)
        self.setMenuMinWidth(160)

    def _createSubMenu(self, icon: Union[QIcon, str, FluentIconBase], title: str, parentMenu: RoundMenu = None):
        parentMenu = parentMenu or self.menu
        self.subMenu = AcrylicMenu(title, parentMenu)
        self.subMenu.setIcon(icon)
        self.setSubMenuMinWidth(160)
        return parentMenu


class ProfileCardMenu(Menu):
    """ 个人信息卡片组件 """
    def __init__(self, avatarPath: str, name: str, email: str, parent=None, buttonText: str = '主页', url: str = ''):
        super().__init__(parent)
        self._widget = QWidget()
        self._widget.setFixedSize(307, 82)
        self.menu.addWidget(self._widget)
        self.addSeparator()._initCard(avatarPath, name, email, buttonText, url)

    def _initCard(self, avatarPath: str, name: str, email: str, buttonText: str, url: str = ''):
        self.avatar = AvatarWidget(avatarPath, self._widget)
        self.nameLabel = BodyLabel(name, self._widget)
        self.emailLabel = CaptionLabel(email, self._widget)
        self.button = HyperlinkButton(url, buttonText, self._widget)

        self.emailLabel.setTextColor(QColor(96, 96, 96), QColor(206, 206, 206))
        setFont(self.button, 13)

        self.setAvatarRadius(24)
        self.avatar.move(2, 6)
        self.nameLabel.move(64, 13)
        self.emailLabel.move(64, 32)
        self.button.move(52, 48)

    def setAvatarRadius(self, radius: int):
        self.avatar.setRadius(radius)


class AcrylicProfileCardMenu(ProfileCardMenu):
    """ 亚力克个人信息卡片组件 """
    def __init__(self, avatarPath, name, email, parent=None, buttonText="主页", url=''):
        super().__init__(avatarPath, name, email, parent, buttonText, url)
        self.menu = AcrylicMenu(parent)
        self.menu.addWidget(self._widget)
        self.menu.addSeparator()


class CheckedMenu(MenuBase):
    """ 可选中菜单栏 """
    def __init__(self, parent=None, indicatorType: MenuIndicatorType = MenuIndicatorType.CHECK):
        super().__init__(parent)
        self.menu = CheckableMenu('', parent, indicatorType)
        self.setMenuMinWidth(160)

    def createGroup(self):
        return QActionGroup(self.menu)

    @staticmethod
    def getCheckedAction(actionGroup: QActionGroup):
        return actionGroup.checkedAction()

    def addItem(self, icon: Union[QIcon, str, FluentIconBase], text: str):
        action = Action(icon, text, checkable=True)
        self.menu.addAction(action)
        return action

    def addItems(self, icons: list[Union[QIcon, str, FluentIconBase]], texts: list[str]):
        actions = []
        for text, icon in zip(texts, icons):
            actions.append(self.addItem(icon, text))
        return actions

    def addSubItem(
            self,
            title: str,
            icon: Union[QIcon, str, FluentIconBase],
            text: str,
            subIcon: Union[QIcon, str, FluentIconBase],
            parentMenu: CheckableMenu = None,
            indicatorType: MenuIndicatorType = MenuIndicatorType.RADIO
    ) -> Action:
        """ parentMenu is None, default = self.menu """
        action = Action(icon, title, checkable=True)
        self._createSubMenu(subIcon, text, parentMenu, indicatorType).addMenu(self.subMenu)
        self.subMenu.addAction(action)
        return action

    def addSubItems(
            self,
            title: str,
            icon: Union[QIcon, str, FluentIconBase],
            text: list[str],
            subIcon: list[Union[QIcon, str, FluentIconBase]],
            parentMenu: CheckableMenu = None,
            indicatorType: MenuIndicatorType = MenuIndicatorType.RADIO
    ) -> list[Action]:
        """ parentMenu is None, default = self.menu """
        actions = []
        self._createSubMenu(icon, title, parentMenu, indicatorType).addMenu(self.subMenu)
        for t, i in zip(text, subIcon):
            action = Action(i, t, checkable=True)
            self.subMenu.addAction(action)
            actions.append(action)
        return actions

    def _createSubMenu(
            self,
            icon: Union[QIcon, str, FluentIconBase],
            title: str,
            parentMenu: RoundMenu = None,
            indicatorType: MenuIndicatorType = MenuIndicatorType.RADIO
    ) -> RoundMenu:
        parentMenu = parentMenu or self.menu
        self.subMenu = CheckableMenu(title, parentMenu, indicatorType)
        self.setSubMenuMinWidth(160)
        self.subMenu.setIcon(icon)
        return parentMenu

    @staticmethod
    def addMenuToGroup(group: QActionGroup, action: Action) -> Action:
        """ add menu to group, menu is radio"""
        group.addAction(action)
        return action

    @staticmethod
    def addMenuToGroups(group: QActionGroup, actions: list[Action]) -> list[Action]:
        for action in actions:
            group.addAction(action)
        return actions

    @staticmethod
    def isChecked(action: Action) -> bool:
        return action.isChecked()


class AcrylicCheckedMenu(CheckedMenu):
    def __init__(self, parent=None, indicatorType: MenuIndicatorType = MenuIndicatorType.CHECK):
        super().__init__(parent)
        self.menu = AcrylicCheckableMenu('', parent, indicatorType)


class Shortcut:
    """ 设置快捷键 """
    def addShortcut(self, key: str, parent: QWidget, function):
        """ set shortcut """
        shortcut = QShortcut(QKeySequence(key), parent)
        shortcut.activated.connect(function)
        return self

    def addShortcuts(self, keys: list[str], parent: QWidget, functions: list):
        for key, fc in zip(keys, functions):
            self.addShortcut(key, parent, fc)
        return self

def setMenuWidget(widget: QWidget, parent: QWidget, pos: QPoint):
    # e.pos()
    # e.globalPos()
    return widget.rect().contains(widget.mapFromGlobal(parent.mapToGlobal(pos)))
