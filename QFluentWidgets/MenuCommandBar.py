import sys

from PySide6.QtWidgets import QWidget, QApplication, QSystemTrayIcon
from PySide6.QtGui import Qt, QAction, QColor, QActionGroup, QIcon
from pyautogui import shortcut

from qfluentwidgets import SmoothScrollArea, VBoxLayout, RoundMenu, PrimaryPushButton, Action, FluentIcon, AvatarWidget, \
    BodyLabel, HyperlinkLabel, setFont, HyperlinkButton, CheckableMenu, SystemTrayMenu, LineEdit, LineEditMenu, \
    CommandButton, CommandBar, CommandBarView
from qfluentwidgets.components.widgets.combo_box import ComboBoxMenu
from qfluentwidgets.components.widgets.line_edit import CompleterMenu


class MenuCommandBar(SmoothScrollArea):
    def __init__(self, text, parent=None):
        super().__init__(parent)

        self.initWindow()
        self.initMenu()
        self.initLayout()

        self.setObjectName(text.replace(' ', '_'))

    def initWindow(self):
        self.scrollWidget = QWidget()
        self.vLayout = VBoxLayout(self.scrollWidget)
        self.vLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)
        # 系统托盘
        self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))
        SystemTrayIcon(self).show()

    def initMenu(self):
        '''圆角菜单'''
        self.roundMenu = RoundMenu("圆角菜单", self)
        # 添加动作
        self.roundMenu.addAction(
            Action(FluentIcon.COPY, '复制', shortcut="Ctrl+A", triggered=lambda: print("Copy Click")))
        self.roundMenu.addAction(Action(FluentIcon.PASTE, '粘贴', triggered=lambda: print("Paste Click")))
        # 批量添加
        # self.roundMenu.addActions()
        # 添加分割线
        self.roundMenu.addSeparator()
        self.roundMenu.hide()
        self.roundMenuButton = PrimaryPushButton("左键双击显示圆角菜单", self)

        # 添加子菜单
        self.subMenu = RoundMenu('添加到', self)
        self.subMenu.setIcon(FluentIcon.ADD)
        self.subMenu.addActions([
            Action(FluentIcon.VIDEO, "视频", triggered=lambda: print("Video Click")),
            Action(FluentIcon.MUSIC, '音乐', triggered=lambda: print("Music Click")),
        ]
        )
        self.roundMenu.addMenu(self.subMenu)

        '''添加自定义组件菜单'''
        self.customMenu = RoundMenu(self)
        self.customMenu.addWidget(CustomMenuWidget(
            r"C:\IDE\Projects\Python\QT\bitbug_favicon.ico",
            'GenShin',
            "email.com",
            self
        ))
        self.customMenu.addSeparator()  # 添加分隔线
        self.customMenu.addActions([
            Action(FluentIcon.DOWNLOAD, '下载', triggered=lambda: print("Download Click")),
            Action(FluentIcon.FOLDER, '目录', triggered=lambda: print("Folder Click")),
        ])
        self.customMenu.addSeparator()
        self.customMenu.addAction(Action(FluentIcon.SETTING, '设置', triggered=lambda: print("Settings Click")))
        self.customButton = PrimaryPushButton('右键双击显示自定义菜单', self)

        '''可选中菜单'''
        self.checkMenu = CheckableMenu(self)
        self.checkGroup = QActionGroup(self)  # 动作组
        self.checkGroup.addAction(
            Action(FluentIcon.CALENDAR, "创建日期", triggered=lambda b: print(b), checkable=True),
        )
        self.checkMenu.addActions([
            Action(FluentIcon.CAMERA, "拍摄日期", triggered=lambda b: print(b), checkable=True),
            Action(FluentIcon.EDIT, "修改日期", triggered=lambda b: print(b), checkable=True),
        ]
        )

        '''单行编辑框菜单'''
        # LineEditMenu()

        '''多行编辑框菜单'''
        # TextEditMenu()

        '''下拉框菜单'''
        self.cbm = ComboBoxMenu(self)
        self.cbm.addActions([
            Action("Copy", self),
            Action("Paste", self),
            Action("Setting", self)
        ])

        '''补全菜单'''
        self.lineEdit = LineEdit(self)
        self.completerMenu = CompleterMenu(self.lineEdit)
        self.completerMenu.addAction(
            Action(FluentIcon.COPY, 'Copy')
        )

        '''命令按钮'''
        self.commandButton = CommandButton(self)
        # self.commandButton.setIcon(FluentIcon.COMMAND_PROMPT)

        '''命令栏'''
        self.commandBar = CommandBar(self)
        ac = Action(FluentIcon.ADD, '')
        self.commandBar.addAction(ac)
        self.commandBar.addSeparator()
        self.commandBar.addActions([
            Action(FluentIcon.COPY, 'Copy', triggered=lambda: print("Copy Click")),
            Action(FluentIcon.PASTE, 'Past', triggered=lambda: print("Paste Click")),
            Action(FluentIcon.GAME, 'Game', triggered=lambda: print("Game Click")),
        ])
        self.commandBar.addSeparator()
        # 添加始终隐藏的动作
        self.commandBar.addHiddenAction(Action(FluentIcon.DOWNLOAD, '下载', triggered=lambda: print("Download Click")))
        # 默认情况下只显示动作的图标, 如需修改显示模式
        self.commandBar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)  # 图标右侧显示文本
        # self.commandBar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)  # 图标底部显示文本

        '''命令栏弹出视窗'''
        self.barViewButton = PrimaryPushButton('显示命令栏弹出视窗', self)
        self.commandBarView = CommandBarView(self.barViewButton)
        self.commandBarView.addActions([
            Action(FluentIcon.COPY, 'Copy', triggered=lambda: print("Copy Click")),
            Action(FluentIcon.PASTE, 'Past', triggered=lambda: print("Paste Click")),
            Action(FluentIcon.GAME, 'Game', triggered=lambda: print("Game Click")),
        ])
        self.commandBarView.hide()
        self.barViewButton.clicked.connect(self.commandBarView.show)

    def initLayout(self):
        self.vLayout.addWidget(self.roundMenuButton)
        self.vLayout.addWidget(self.customButton)
        self.vLayout.addWidget(self.lineEdit)
        self.vLayout.addWidget(self.commandButton)
        self.vLayout.addWidget(self.commandBar)
        self.vLayout.addWidget(self.barViewButton)
        self.vLayout.addWidget(self.cbm)

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.roundMenu.exec(event.globalPos())
        if event.button() == Qt.RightButton:
            self.customMenu.exec(event.globalPos())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.checkMenu.exec(event.globalPos())


'''系统托盘'''


class SystemTrayIcon(QSystemTrayIcon):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setIcon(parent.windowIcon())
        self.menu = SystemTrayMenu(parent)
        # CheckableSystemTrayMenu() 可选中系统托盘菜单
        self.menu.addActions([
            Action("✈️ 打飞机", triggered=lambda: print("正在打飞机")),
            Action("退出程序", triggered=QApplication.exit),
            Action('🏀打篮球', triggered=lambda: print("""巅峰产生虚伪的拥护，黄昏见证真正的使徒 🏀

                       ⠰⢷⢿⠄
                   ⠀⠀⠀⠀⠀⣼⣷⣄
                   ⠀⠀⣤⣿⣇⣿⣿⣧⣿⡄
                   ⢴⠾⠋⠀⠀⠻⣿⣷⣿⣿⡀
                   ⠀⢀⣿⣿⡿⢿⠈⣿
                   ⠀⠀⠀⢠⣿⡿⠁⠀⡊⠀⠙
                   ⠀⠀⠀⢿⣿⠀⠀⠹⣿
                   ⠀⠀⠀⠀⠹⣷⡀⠀⣿⡄
                   ⠀⠀⠀⠀⣀⣼⣿⠀⢈⣧
        """))
        ])
        self.setToolTip('Ciallo～(∠・ω< )⌒☆')
        self.setContextMenu(self.menu)


class CustomMenuWidget(QWidget):
    def __init__(self, avatarPath: str, name: str, email: str, parent=None):
        super().__init__(parent)
        self.avatar = AvatarWidget(avatarPath, self)
        self.nameLabel = BodyLabel(name, self)
        self.emailLabel = BodyLabel(email, self)
        self.logoutButton = HyperlinkButton('https://www.github.com/mikuas', '注销', self)

        self.emailLabel.setTextColor(QColor(96, 96, 96), QColor(206, 206, 206))
        setFont(self.logoutButton, 13)

        self.setFixedSize(307, 82)
        self.avatar.setRadius(24)  # 设置半径
        self.avatar.move(2, 6)
        self.nameLabel.move(64, 13)
        self.emailLabel.move(64, 32)
        self.logoutButton.move(52, 48)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MenuCommandBar("MENUCOMMAND")
    w.resize(1000, 600)
    w.show()
    sys.exit(app.exec())
