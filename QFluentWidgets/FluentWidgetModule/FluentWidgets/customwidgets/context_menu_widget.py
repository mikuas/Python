import sys

from PySide6.QtCore import QPoint
from PySide6.QtGui import QColor, QActionGroup
from PySide6.QtWidgets import QWidget, QApplication
from qfluentwidgets import RoundMenu, Action, AvatarWidget, BodyLabel, CaptionLabel, setFont, HyperlinkButton, \
    FluentIcon, CheckableMenu, MenuIndicatorType, Theme, setTheme


class Menu(QWidget):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.__initMenu(parent)
        self.setMenuWidth(150)

    def __initMenu(self, parent: QWidget = None):
        self.menu = RoundMenu(parent=parent)

    def addMenu(self, action: Action):
        self.menu.addAction(action)
        return self

    def addMenus(self, actions: list[Action]):
        self.menu.addActions(actions)
        return self

    def addSubMenus(self, subTitle: str, actions: Action | list[Action]):
        self.subMenu = RoundMenu(subTitle, self)
        if type(actions) is list:
            self.subMenu.addActions(actions)
        else:
            self.subMenu.addAction(actions)
        self.menu.addMenu(self.subMenu)
        return self

    def exec(self, position: QPoint):
        self.menu.exec(position)

    def addMenuSeparator(self):
        self.menu.addSeparator()
        return self

    def addSubMenuSeparator(self):
        self.subMenu.addSeparator()
        return self

    def setMenuWidth(self, width: int):
        self.menu.view.setFixedWidth(width)
        return self


class ProfileCardMenu(Menu):
    def __init__(self, avatarPath: str, name: str, email: str, parent: QWidget = None):
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
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initCheckedMenu()

        self.addCheckedMenus(
            ['test1', 'test2', 'test3'],
            [FluentIcon.COPY, FluentIcon.PASTE, FluentIcon.MOVE]
        ).addSubCheckedMenus(
            "title",
            ['od1', 'od2', 'od3'],
            [FluentIcon.MUSIC, FluentIcon.GITHUB, FluentIcon.CHAT]
        ).setCheckedMenuWidth(200)

    def __initCheckedMenu(self):
        self.checkedMenu = CheckableMenu(parent=self, indicatorType=MenuIndicatorType.RADIO)

    def __initGroup(self):
        self.group = QActionGroup(self)

    def addCheckedMenu(self, text: str, icon):
        self.checkedMenu.addAction(Action(icon, text))
        return self

    def addCheckedMenus(self, texts, icons):
        for text, icon in zip(texts, icons):
            self.addCheckedMenu(text, icon)
        return self

    def addSubCheckedMenus(self, title: str, texts, icons, parent: QWidget = None, indicatorType=MenuIndicatorType.RADIO):
        self.subCheckedMeus = CheckableMenu(title, parent, indicatorType)
        for text, icon in zip(texts, icons):
            self.subCheckedMeus.addAction(Action(icon, text))
        self.checkedMenu.addMenu(self.subCheckedMeus)
        return self

    def addCheckedMenuGroup(self, action: Action):
        self.group.addAction(action)
        return self

    def contextMenuEvent(self, e):
        self.checkedMenu.exec(e.globalPos())

    def setCheckedMenuWidth(self, width: int):
        self.checkedMenu.setFixedWidth(width)
        self.checkedMenu.view.setFixedWidth(width - 20)
        return self

    def exec(self, position: QPoint):
        self.checkedMenu.exec(position)

def setMenuWidget(widget: QWidget, parent: QWidget, pos: QPoint):
    return widget.rect().contains(widget.mapFromGlobal(parent.mapToGlobal(pos)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CheckedMenuWidget()
    w.resize(1200, 700)
    setTheme(Theme.AUTO)
    w.show()
    sys.exit(app.exec())