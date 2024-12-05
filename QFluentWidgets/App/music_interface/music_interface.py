import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from qfluentwidgets import SplitFluentWindow, FluentIcon, setTheme, Theme, NavigationItemPosition

from QFluentWidgets.App.music_interface import MusicListWidget, SettingInterface, PlayWidget


class MusicWidget(SplitFluentWindow):
    def __init__(self):
        super().__init__()
        self.__initWindow()
        self.musicList = QWidget(self)
        self.musicList = MusicListWidget("Music_List")
        self.settingWidget = SettingInterface("SETTINGS")
        self.playWidget = PlayWidget("Play")
        self.stackedWidget.setMinimumSize(500, 420)
        self.initNavigation()
        self.widgetLayout.widget()

    def initNavigation(self):
        self.navigationInterface.setExpandWidth(250)
        self.navigationInterface.setMinimumExpandWidth(1500)
        self.navigationInterface.setAcrylicEnabled(True)
        self.addSubInterface(
            self.musicList,
            FluentIcon.MUSIC,
            '音乐列表'
        )
        self.addSubInterface(
            self.settingWidget,
            FluentIcon.SETTING,
            "设置",
            NavigationItemPosition.BOTTOM
        )
        self.addSubInterface(
            self.playWidget,
            FluentIcon.PLAY,
            "播放界面"
        )

    def __initWindow(self):
        self.setMicaEffectEnabled(True)
        self.resize(1200, 800)
        desktop = QApplication.primaryScreen().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.musicList.list.setFixedHeight(self.height() - 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MusicWidget()
    setTheme(Theme.AUTO)
    window.show()
    sys.exit(app.exec())
