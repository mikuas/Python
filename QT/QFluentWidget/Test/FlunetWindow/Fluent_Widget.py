import sys

from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QApplication, QVBoxLayout
from qfluentwidgets import *

from webView import WebView
from imageWidget import ImageWidget
from settingWidget import SettingWidget
from cardWidget import CardsWidget


class Window(FluentWindow):
    def __init__(self):
        super().__init__()
        self.move(300, 150)
        self.webView = WebView('Web', "https://yiyan.baidu.com/")
        # 设置主题色
        # setTheme(Theme.LIGHT)
        # 更改主题颜色
        # setThemeColor('#0078d4')

        with open('./data/json/filePath.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.resize(1200, 700)
        self.home = ImageWidget("HOME", data['path'])
        self.music = ImageWidget("MUSIC", [r"C:\Users\Administrat1or\OneDrive\Pictures\13.jpg"])
        self.github = ImageWidget("Interface 3", [r"C:\Users\Administrator\OneDrive\Pictures\14.jpg"])
        self.setting = SettingWidget("SETTINGS", qconfig.themeMode, self)
        self.tool = CardsWidget("CARDS")

        # 跟换主题信号插槽
        self.setting.getThemeCard().optionChanged.connect(
            lambda theme: setTheme(theme.value)
        )

        self.initWindow()
        #  初始化导航栏
        self.initNavigation()

        # 调整展开状态下侧边导航的宽度
        self.navigationInterface.setExpandWidth(150)
        # 展开导航栏
        # self.navigationInterface.expand(useAni=False)

    def initWindow(self):
        # 窗口图标
        self.setWindowIcon(Icon(FluentIcon.GITHUB))
        # 标题
        self.setWindowTitle("Window")

    def initNavigation(self):
        self.addSubInterface(self.home, FluentIcon.HOME, "主页")
        self.addSubInterface(self.music, FluentIcon.MUSIC, "音乐")
        self.addSubInterface(self.github, FluentIcon.GITHUB, "GitHub")
        self.addSubInterface(self.tool, FluentIcon.APPLICATION, "卡片")
        # 添加分隔符
        self.navigationInterface.addSeparator()
        self.navigationInterface.addItem(
            "Web",
            FluentIcon.SEND,
            "浏览器",
            onClick=self.webView.show
        )
        self.addSubInterface(self.setting, FluentIcon.SETTING, "设置", NavigationItemPosition.BOTTOM)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    #  启用云母特效
    window.setMicaEffectEnabled(True)
    window.show()
    sys.exit(app.exec())
