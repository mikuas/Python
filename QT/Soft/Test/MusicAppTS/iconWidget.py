from PySide6.QtWidgets import QSystemTrayIcon, QMenu
from PySide6.QtGui import QIcon, QAction

class TrayIconWidget:
    def __init__(self, parent, path):
        self.trayIcon = QSystemTrayIcon(parent)
        self.trayIcon.setIcon(QIcon(path))
        self.trayIcon.setToolTip('Ciallo～(∠・ω< )⌒☆')
        self.trayIcon.activated.connect(lambda reason: (parent.show(), parent.raise_(), parent.activateWindow()) if reason == QSystemTrayIcon.ActivationReason.Trigger else reason)
        # 托盘图标菜单
        trayMenu = QMenu()
        # 添加分隔符
        trayMenu.addSeparator()

        showActionTray = QAction('显示窗口', parent)
        showActionTray.triggered.connect(lambda: (parent.show(), parent.raise_(), parent.activateWindow()))
        quitAction = QAction('退出', parent)
        quitAction.triggered.connect(parent.quitApp)
        # 添加到托盘中
        trayMenu.addActions([showActionTray, quitAction])
        # 设置菜单
        self.trayIcon.setContextMenu(trayMenu)
        # 显示系统托盘图标
        self.trayIcon.show()
