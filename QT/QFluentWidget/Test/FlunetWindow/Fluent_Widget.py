import sys
import json

from PySide6.QtWidgets import QApplication
from qfluentwidgets import FluentWindow, RoundMenu, setTheme, qconfig, Icon, FluentIcon, NavigationItemPosition, \
    InfoBarPosition, InfoBar, Theme

from imageWidget import ImageWidget
from settingWidget import SettingWidget
from cardWidget import CardsWidget
from githubWidget import GitHubWidget
from profileCard import ProfileNavigationAvatarWidget
from musicWidget import MusicWidget
from trayIcon import SystemTrayIcon


class Window(FluentWindow):
    def __init__(self):
        super().__init__()
        self.resize(1200, 700)
        # 设置主题色
        # setTheme(Theme.LIGHT)
        # 更改主题颜色
        # setThemeColor('#0078d4')
        self.menu = RoundMenu(parent=self)

        with open('data/json/filePath.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.home = ImageWidget("HOME", data['path'])
        self.music = MusicWidget("MUSIC")
        self.github = GitHubWidget("GITHUB")
        self.tool = CardsWidget("CARDS")
        self.setting = SettingWidget("SETTINGS", qconfig.themeMode, self)

        self.initWindow()
        #  初始化导航栏
        self.initNavigation()

        # 调整展开状态下侧边导航的宽度
        # self.navigationInterface.setExpandWidth(150)
        # self.navigationInterface.setMinimumExpandWidth(300)
        # 展开导航栏
        # self.navigationInterface.expand(useAni=False)

    def initWindow(self):
        # 窗口图标
        self.setWindowIcon(Icon(FluentIcon.GITHUB))
        # 标题
        self.setWindowTitle("Window")
        # 显示位置
        desktop = QApplication.primaryScreen().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

        self.systemTray = SystemTrayIcon(self)
        self.systemTray.setToolTip('Ciallo～(∠・ω< )⌒☆')
        self.systemTray.show()

    def initNavigation(self):
        self.navigationInterface.setExpandWidth(250)
        self.navigationInterface.setMinimumExpandWidth(1500)
        self.addSubInterface(self.home, FluentIcon.HOME, "主页")
        self.addSubInterface(self.music, FluentIcon.MUSIC, "音乐")
        self.addSubInterface(self.github, FluentIcon.GITHUB, "GitHub")
        self.addSubInterface(self.tool, FluentIcon.DEVELOPER_TOOLS, "工具")
        # 添加分隔符
        self.navigationInterface.addSeparator()
        self.navigationInterface.addWidget(
            'author',
            ProfileNavigationAvatarWidget(self),
            onClick=lambda: self.menu,
            position=NavigationItemPosition.BOTTOM
        )
        self.addSubInterface(self.setting, FluentIcon.SETTING, "设置", NavigationItemPosition.BOTTOM)
        self.navigationInterface.setAcrylicEnabled(True)

    def input(self):
        if self.count < 50:
            self.count += 1
            for i in range(1):
                InfoBar.success(
                    "爸爸",
                    "LZG是我爸爸",
                    isClosable=False,
                    duration=2000,
                    position=InfoBarPosition.TOP,
                    parent=self
                )

    def closeEvent(self, event):
        event.ignore()
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    #  启用云母特效
    window.setMicaEffectEnabled(True)
    setTheme(Theme.AUTO)
    window.show()
    sys.exit(app.exec())
