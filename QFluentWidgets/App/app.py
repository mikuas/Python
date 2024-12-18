# from FluentWidgets import SystemTrayIcon
from QtFluentWidgets.FluentWidgetModule.FluentWidgets import SystemTrayIcon
from PySide6.QtWidgets import QApplication
from qfluentwidgets import FluentWindow, FluentIcon, Action, NavigationItemPosition

from . import MorseWidget, HomeWidget, SettingWidget


class Window(FluentWindow):
    def __init__(self, parent: str = None):
        super().__init__(parent)
        self.homeWidget = HomeWidget("HOME", self)
        self.moresWidget = MorseWidget("MORSE", self)
        self.settingWidget = SettingWidget("SETTING", self)

        self.__initWindow()
        self.__initNavigationInterface()
        self.__initTrayIcon()

    def __initWindow(self):
        self.setMicaEffectEnabled(True)
        self.resize(1200, 700)
        desktop = QApplication.primaryScreen().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

    def __initNavigationInterface(self):
        self.navigationInterface.setExpandWidth(250)
        self.navigationInterface.setMinimumExpandWidth(1500)
        self.navigationInterface.setAcrylicEnabled(True)
        self.addSubInterface(
            self.homeWidget,
            FluentIcon.HOME,
            "主页"
        )
        self.addSubInterface(
            self.moresWidget,
            FluentIcon.CODE,
            '文本加密',
        )
        self.addSubInterface(
            self.settingWidget,
            FluentIcon.SETTING,
            "设置",
            NavigationItemPosition.BOTTOM
        )

    def __initTrayIcon(self):
        self.systemTrayIcon = SystemTrayIcon(self)
        self.systemTrayIcon.setIcon(FluentIcon.APPLICATION)
        self.systemTrayIcon.addMenus([
            Action(FluentIcon.HOME, "显示应用界面", self, triggered=lambda: (self.raise_(), self.show(), self.activateWindow())),
            Action(FluentIcon.EMBED, "退出", self, triggered=QApplication.quit)
        ])
        self.systemTrayIcon.show()