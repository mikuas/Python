import sys
from symtable import Function

from PySide6.QtCore import QSize, QUrl, QDate
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QMenu
from PySide6.QtGui import Qt, QAction
from pyautogui import shortcut
from qfluentwidgets import *
from qfluentwidgets.multimedia import SimpleMediaPlayBar, MediaPlayBarButton, StandardMediaPlayBar

from QT.button_event import MainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 450)
        centerWindget = QWidget(self)
        mainLayout = QVBoxLayout(centerWindget)

        '''菜单'''
        menu = RoundMenu()
        # 逐个添加动作，Action 继承自 QAction，接受 FluentIconBase 类型的图标
        menu.addAction(Action(FluentIcon.COPY, '复制', triggered=lambda: print("复制成功")))
        menu.addAction(Action(FluentIcon.CUT, '剪切', triggered=lambda: print("剪切成功")))

        # 添加动作
        menu.addActions([
            Action(FluentIcon.PASTE, '粘贴'),
            Action(FluentIcon.CANCEL, '撤销')
        ])
        # 分割线
        menu.addSeparator()
        menu.addAction(QAction('全选', shortcut="Ctrl+A"))

        # 添加子菜单
        submenu = RoundMenu("添加到", self)

        submenu.setIcon(FluentIcon.ADD)
        submenu.addActions([
            Action(FluentIcon.VIDEO, '视频'),
            Action(FluentIcon.MUSIC, '音乐'),
        ])

        menu.addMenu(submenu)

        mainLayout.addWidget(menu)
        self.setCentralWidget(centerWindget)


# 右键
class ProfileCard(QWidget):
    """ Profile card """

    def __init__(self, avatarPath: str, name: str, email: str, parent=None):
        super().__init__(parent=parent)
        self.avatar = AvatarWidget(avatarPath, self)
        self.nameLabel = BodyLabel(name, self)
        self.emailLabel = CaptionLabel(email, self)
        self.logoutButton = HyperlinkButton('https://qfluentwidgets.com/', '注销', self)

        self.emailLabel.setTextColor(QColor(96, 96, 96), QColor(206, 206, 206))
        setFont(self.logoutButton, 13)

        self.setFixedSize(307, 82)
        self.avatar.setRadius(24)
        self.avatar.move(2, 6)
        self.nameLabel.move(64, 13)
        self.emailLabel.move(64, 32)
        self.logoutButton.move(52, 48)


class Demo(QWidget):

    def __init__(self):
        super().__init__()

    # def contextMenuEvent(self, e):
    def mousePressEvent(self, e) -> None:
        menu = RoundMenu(parent=self)

        # add custom widget
        card = ProfileCard('resource/shoko.png', '硝子酱', 'shokokawaii@outlook.com', menu)
        menu.addWidget(card, selectable=True)
        menu.addSeparator()
        at = Action(FluentIcon.PEOPLE, '管理账户和设置')
        at.triggered.connect(lambda: print(True))
        menu.addActions([
            at,
            Action(FluentIcon.SHOPPING_CART, '支付方式'),
            Action(FluentIcon.CODE, '兑换代码和礼品卡'),
        ])
        menu.addSeparator()
        menu.addAction(Action(FluentIcon.SETTING, '设置'))
        if e.button() == Qt.LeftButton:
            menu.exec(e.globalPos())
        # menu.exec(e.globalPos())
        # print(e.globalPos())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Demo()
    # window = Window()
    window.show()
    sys.exit(app.exec())