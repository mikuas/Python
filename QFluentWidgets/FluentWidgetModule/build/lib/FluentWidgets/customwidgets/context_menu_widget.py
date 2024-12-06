from typing import Union

from PySide6.QtCore import QPoint
from PySide6.QtGui import QColor, QActionGroup, QIcon, QShortcut, QKeySequence
from PySide6.QtWidgets import QWidget
from qfluentwidgets import RoundMenu, Action, AvatarWidget, BodyLabel, CaptionLabel, setFont, HyperlinkButton, \
    CheckableMenu, MenuIndicatorType, FluentIconBase
from qfluentwidgets.components.material import AcrylicMenu as AM


class MenuBase(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.menu = None
        self.subMenu = None

    def addAction(self, action: Action) -> 'MenuBase':
        self.menu.addAction(action)
        return self

    def addActions(self, actions: list[Action]) -> 'MenuBase':
        for action in actions:
            self.addAction(action)
        return self

    def addItem(self, icon: Union[QIcon, str, FluentIconBase], text: str):
        action = Action(icon, text, self)
        self.menu.addAction(action)
        return action

    def addItems(self, icon: list[Union[QIcon, str, FluentIconBase]], text: list[str]):
        actions = []
        for icon, text in zip(icon, text):
            actions.append(self.addItem(icon, text))
        return actions

    def __createSubMenu(self, icon: Union[QIcon, str, FluentIconBase], title: str, parentMenu: RoundMenu):
        parentMenu = parentMenu or self.menu
        self.subMenu = RoundMenu(title, self)
        self.subMenu.setIcon(icon)
        self.setSubMenuMinWidth(160)
        return parentMenu

    def addSubAction(self, icon: Union[QIcon, str, FluentIconBase], title: str, action: Action, parentMenu: RoundMenu = None):
        """ parentMenu is None, default = self.menu """
        self.__createSubMenu(icon, title, parentMenu).addMenu(self.subMenu)
        self.subMenu.addAction(action)
        return self

    def addSubActions(self, icon: Union[QIcon, str, FluentIconBase], title: str, actions: list[Action], parentMenu: RoundMenu = None):
        """ parentMenu is None, default = self.menu """
        parentMenu = parentMenu or self.menu
        self.__createSubMenu(icon, title, parentMenu).addMenu(self.subMenu)
        self.subMenu.addActions(actions)
        return self

    def exec(self, position: QPoint):
        self.menu.exec(position)

    def execCenter(self, widget: QWidget):
        """ 在指定组件中心执行 """
        self.menu.exec(widget.mapToGlobal(widget.rect().center()))

    def addSeparator(self):
        self.menu.addSeparator()
        return self

    def addSubSeparator(self, subMenu: RoundMenu = None):
        """
        subMenu is None, default = self.subMenu
        """
        subMenu = subMenu or self.subMenu
        subMenu.addSeparator()
        return self

    def setMenuMinWidth(self, width: int):
        self.menu.setMinimumWidth(width)
        self.menu.view.setMinimumWidth(width - 20)
        return self

    def setSubMenuMinWidth(self, width: int, menu: RoundMenu = None):
        """
        menu is None, default = self.subMenu
        """
        menu = menu or self.subMenu
        menu.setMinimumWidth(width)
        menu.view.setMinimumWidth(width - 20)
        return self

    @staticmethod
    def setClicked(action: Action, func):
        action.triggered.connect(func)
        return action

    @staticmethod
    def setClickeds(actions: list[Action], function: list):
        for action, fc in zip(actions, function):
            action.triggered.connect(fc)
        return actions

    def setShortcut(self, action: Action, key: str):
        """ 设置快捷键 """
        action.setShortcut(QKeySequence(key))
        return self

    def setShortcuts(self, actions: list[Action], keys: list[str]):
        for action, key in zip(actions, keys):
            action.setShortcut(key)
        return self


class Menu(MenuBase):
    """ 菜单栏组件 """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.menu = RoundMenu(parent=self)
        self.setMenuMinWidth(160)


class AcrylicMenu(MenuBase):
    """ 亚力克菜单 """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.menu = AM(self)
        self.setMenuMinWidth(160)


class ProfileCardMenu(Menu):
    """ 个人信息卡片组件 """
    def __init__(self, avatarPath: str, name: str, email: str, parent=None, buttonText: str = '主页', url: str = ''):
        super().__init__(parent)
        self.__widget = QWidget(self)
        self.__widget.setFixedSize(307, 82),
        self.menu.addWidget(self.__widget)
        self.addSeparator().__initCard(avatarPath, name, email, buttonText, url)

    def __initCard(self, avatarPath: str, name: str, email: str, buttonText: str, url: str = ''):
        self.avatar = AvatarWidget(avatarPath, self.__widget)
        self.nameLabel = BodyLabel(name, self.__widget)
        self.emailLabel = CaptionLabel(email, self.__widget)
        self.button = HyperlinkButton(url, buttonText, self.__widget)

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
        self.menu = AcrylicMenu(self)


class CheckedMenu(MenuBase):
    """ 可选中菜单栏 """
    def __init__(self, parent=None, indicatorType: MenuIndicatorType = MenuIndicatorType.RADIO):
        super().__init__(parent)
        self.menu = CheckableMenu(parent=self, indicatorType=indicatorType)
        self.setMenuMinWidth(160)

    def createGroup(self):
        return QActionGroup(self)

    @staticmethod
    def getCheckedAction(actionGroup: QActionGroup):
        return actionGroup.checkedAction()

    def addCheckItem(self, icon: Union[QIcon, str, FluentIconBase], text: str):
        action = Action(icon, text, checkable=True)
        self.menu.addAction(action)
        return action

    def addCheckItems(self, icons: list[Union[QIcon, str, FluentIconBase]], texts: list[str]):
        actions = []
        for text, icon in zip(texts, icons):
            actions.append(self.addCheckItem(icon, text))
        return actions

    def addSubCheckItem(
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
        self.__createSubMenu(subIcon, text, parentMenu, indicatorType).addMenu(self.subMenu)
        self.subMenu.addAction(action)
        return action

    def addSubCheckItems(
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
        self.__createSubMenu(icon, title, parentMenu, indicatorType).addMenu(self.subMenu)
        for t, i in zip(text, subIcon):
            action = Action(i, t, checkable=True)
            self.subMenu.addAction(action)
            actions.append(action)
        return actions

    def __createSubMenu(
            self,
            icon: Union[QIcon, str, FluentIconBase],
            title: str,
            parentMenu: RoundMenu,
            indicatorType: MenuIndicatorType = MenuIndicatorType.RADIO
    ) -> RoundMenu:
        parentMenu = parentMenu or self.menu
        self.subMenu = CheckableMenu(title, self, indicatorType)
        self.setSubMenuMinWidth(160)
        self.subMenu.setIcon(icon)
        return parentMenu

    @staticmethod
    def addMenuToGroup(group: QActionGroup, action: Action) -> Action:
        group.addAction(action)
        return action

    @staticmethod
    def isChecked(action: Action) -> bool:
        return action.isChecked()

    @staticmethod
    def addMenuToGroups(group: QActionGroup, actions: list[Action]) -> list[Action]:
        for action in actions:
            group.addAction(action)
        return actions


class Shortcut:
    """ 设置快捷键 """
    def addShortcut(self, key: str, parent: QWidget, func):
        shortcut = QShortcut(QKeySequence(key), parent)
        shortcut.activated.connect(func)
        return self

    def addShortcuts(self, keys: list[str], parent: QWidget, funcs: list):
        for key, fc in zip(keys, funcs):
            self.addShortcut(key, parent, fc)
        return self

def setMenuWidget(widget: QWidget, parent: QWidget, pos: QPoint):
    # e.pos()
    # e.globalPos()
    return widget.rect().contains(widget.mapFromGlobal(parent.mapToGlobal(pos)))
