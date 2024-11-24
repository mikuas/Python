from typing import Union

from PySide6.QtCore import QPoint
from PySide6.QtGui import QColor, QActionGroup, QIcon, QShortcut, QKeySequence
from PySide6.QtWidgets import QWidget
from qfluentwidgets import RoundMenu, Action, AvatarWidget, BodyLabel, CaptionLabel, setFont, HyperlinkButton, \
    CheckableMenu, MenuIndicatorType, FluentIconBase


class Menu(QWidget):
    """ 菜单栏组件 """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.menu = None
        self.subMenu = None
        self.__initMenu(parent)
        self.setMenuWidth(160)

    def __initMenu(self, parent: QWidget = None):
        self.menu = RoundMenu(parent=parent)

    def addMenu(self, action: Action):
        self.menu.addAction(action)
        return self

    def addMenus(self, actions: list[Action]):
        self.menu.addActions(actions)
        return self

    def addSubMenus(self, icon: Union[QIcon, str, FluentIconBase], title: str, actions: Action | list[Action], menu: RoundMenu = None):
        """
        menu is None, default = self.checkedMenu
        """
        menu = menu or self.menu
        self.subMenu = RoundMenu(title, self)
        self.subMenu.setIcon(icon)
        self.setSubMenuWidth(140)
        if type(actions) is list:
            self.subMenu.addActions(actions)
        else:
            self.subMenu.addAction(actions)
        menu.addMenu(self.subMenu)
        return self

    def exec(self, position: QPoint):
        self.menu.exec(position)

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

    def setMenuWidth(self, width: int):
        self.menu.setFixedWidth(width)
        self.menu.view.setFixedWidth(width - 20)
        return self

    def setSubMenuWidth(self, width: int, menu: RoundMenu = None):
        """
        menu is None, default = self.subMenu
        """
        menu = menu or self.subMenu
        menu.setFixedWidth(width)
        menu.view.setFixedWidth(width - 20)
        return self


class ProfileCardMenu(Menu):
    """ 个人信息卡片组件 """
    def __init__(self, avatarPath: str, name: str, email: str, parent=None):
        super().__init__(parent)
        self.__initCard(avatarPath, name, email)
        self.menu.addWidget(self)

    def __initCard(self, avatarPath: str, name: str, email: str):
        self.avatar = AvatarWidget(avatarPath, self)
        self.nameLabel = BodyLabel(name, self)
        self.emailLabel = CaptionLabel(email, self)
        self.button = HyperlinkButton('', "Button", self)

        self.emailLabel.setTextColor(QColor(96, 96, 96), QColor(206, 206, 206))
        setFont(self.button, 13)

        self.setFixedSize(307, 82),
        self.setAvatarRadius(24)
        self.avatar.move(2, 6)
        self.nameLabel.move(64, 13)
        self.emailLabel.move(64, 32)
        self.button.move(52, 48)

    def setAvatarRadius(self, radius: int):
        self.avatar.setRadius(radius)


class CheckedMenuWidget(QWidget):
    """ 可选中菜单栏 """
    def __init__(self, parent=None, indicatorType: MenuIndicatorType = MenuIndicatorType.CHECK):
        super().__init__(parent)
        self.checkedMenu = None
        self.subCheckedMeu = None
        self.__initCheckedMenu(indicatorType)
        self.setCheckedMenuWidth(160)

    def __initCheckedMenu(self, indicatorType: MenuIndicatorType = MenuIndicatorType.CHECK):
        self.checkedMenu = CheckableMenu(parent=self, indicatorType=indicatorType)

    def createGroup(self):
        return QActionGroup(self)

    def addCheckedMenu(self, text: str, icon: Union[QIcon, str, FluentIconBase]) -> tuple[Action, 'CheckedMenuWidget']:
        action = Action(icon, text, checkable=True)
        # action.triggered.connect(lambda a: print("HELLO", a))
        self.checkedMenu.addAction(action)
        return action, self

    def addCheckedMenus(self, texts: list[str], icons: list[Union[QIcon, str, FluentIconBase]]) -> tuple:
        """
        return actions[Action], self
        """
        actions = []
        for text, icon in zip(texts, icons):
            actions.append(self.addCheckedMenu(text, icon)[0])
        return actions, self

    def addSubCheckedMenus(
            self,
            title: str,
            icon: Union[QIcon, str, FluentIconBase],
            texts: list[str],
            icons: list[Union[QIcon, str, FluentIconBase]],
            menu: CheckableMenu = None,
            parent: QWidget = None,
            indicatorType=MenuIndicatorType.RADIO
    ) -> tuple:
        """
        menu is None, default = self.checkedMenu
        return actions[Action], self
        """
        menu = menu or self.checkedMenu
        self.subCheckedMeu = CheckableMenu(title, parent, indicatorType)
        self.setSubCheckedMenuWidth(140)
        self.subCheckedMeu.setIcon(icon)
        actions = []
        for text, icon in zip(texts, icons):
            action = Action(icon, text,  checkable=True)
            self.subCheckedMeu.addAction(action)
            actions.append(action)
        menu.addMenu(self.subCheckedMeu)
        return actions, self

    @staticmethod
    def addMenuToGroup(group: QActionGroup, actions: Action | list[Action]) -> list[Action] | Action:
        if type(actions) is list:
            for action in actions:
                group.addAction(action)
        else:
            group.addAction(actions)
        return actions

    def setCheckedMenuWidth(self, width: int):
        self.checkedMenu.setFixedWidth(width)
        self.checkedMenu.view.setFixedWidth(width - 20)
        return self

    def setSubCheckedMenuWidth(self, width: int, subMenu: CheckableMenu = None):
        """
        subMenu is None, default = self.subCheckedMenu
        """
        subMenu = subMenu or self.subCheckedMeu
        subMenu.setFixedWidth(width)
        subMenu.view.setFixedWidth(width - 20)
        return self

    def addSeparator(self):
        """ 添加分隔符 """
        self.checkedMenu.addSeparator()
        return self

    def addSubSeparator(self, subCheckedMenu: CheckableMenu = None):
        """
        添加子项分隔符
        `subCheckedMenu` is None, default is `self.subCheckedMenu`
        """
        subCheckedMenu = subCheckedMenu or self.subCheckedMeu
        subCheckedMenu.addSeparator()
        return self

    @staticmethod
    def setTriggered(actions: Action | list[Action], func: callable):
        if type(actions) is list:
            for action, fc in zip(actions, func):
                action.triggered.connect(fc)
        else:
            actions.triggered.connect(func)
        return actions

    @staticmethod
    def setShortcut(actions: Action | list[Action], shortcuts: callable):
        """ 设置快捷方式 """
        if type(actions) is list:
            for action, info in zip(actions, shortcuts):
                action.setShortcut(info)
        else:
            actions.setShortcut(shortcuts)
        return actions

    def exec(self, position: QPoint):
        """ run """
        self.checkedMenu.exec(position)


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