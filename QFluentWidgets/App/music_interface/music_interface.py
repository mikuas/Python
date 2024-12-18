import sys

from PySide6.QtWidgets import QApplication
from qfluentwidgets import FluentIcon, setTheme, Theme, NavigationItemPosition, Action

from FluentWidgets import SplitFluentWindow, SystemTrayIcon
from QtFluentWidgets.App.music_interface import MusicListInterface, SettingInterface, LyricsInterface, HomeInterface
from QtFluentWidgets.FluentWidgetModule.FluentWidgets import WinFluentIcon


class MusicInterface(SplitFluentWindow):
    def __init__(self):
        super().__init__()
        self.__initWindow()
        self.systemTrayIcon = SystemTrayIcon(self)
        self.systemTrayIcon.setIcon(WinFluentIcon.WIN_11_LOG)
        self.systemTrayIcon.show()
        self.homeInterface = HomeInterface("HOME_INTERFACE", self)
        self.musicListInterface = MusicListInterface("MUSIC_LIST_INTERFACE", self)
        self.settingInterface = SettingInterface("SETTINGS_INTERFACE", self)
        self.lyricsInterface = LyricsInterface("LYRICS_INTERFACE", self)

        self.stackedWidget.setMinimumSize(500, 420)
        self.hBoxLayout.setContentsMargins(0, 30, 0, 0)
        self.musicList = self.musicListInterface.table
        self.vBoxLayout.addWidget(self.musicListInterface.media)

        self.initNavigation()
        self.initTrayIcon()

        self.musicListInterface.table.currentItemChanged.connect(self.updateMusicPath)

    def initTrayIcon(self):
        self.systemTrayIcon.addMenus([
            Action(FluentIcon.HOME, "打开主界面", self, triggered=lambda: (
                self.raise_(), self.activateWindow(), self.show()
            )),
            Action(FluentIcon.EMBED, '退出', self, triggered=QApplication.quit)
        ])

    def updateMusicPath(self):
        file = self.musicList.currentItem().text()
        path = f"{self.musicListInterface.path}\\{file}\\{file}"
        self.lyricsInterface.setImageLabelPath(f"{path}.jpg")
        self.lyricsInterface.setLyrics(f"{path}.lrc")
        print(path)

    def initNavigation(self):
        self.navigationInterface.setExpandWidth(250)
        self.navigationInterface.setMinimumExpandWidth(1500)
        self.navigationInterface.setAcrylicEnabled(True)
        self.addSubInterface(
            self.homeInterface,
            FluentIcon.HOME,
            '主页'
        )
        self.addSubInterface(
            self.musicListInterface,
            FluentIcon.MUSIC,
            '音乐列表'
        )
        self.addSubInterface(
            self.settingInterface,
            FluentIcon.SETTING,
            "设置",
            NavigationItemPosition.BOTTOM
        )
        self.addSubInterface(
            self.lyricsInterface,
            FluentIcon.PLAY,
            "专辑"
        )

    def __initWindow(self):
        self.setMicaEffectEnabled(True)
        self.setMinimumSize(1150, 680)
        desktop = QApplication.primaryScreen().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

    def resizeEvent(self, event):
        super().resizeEvent(event)

    def closeEvent(self, event):
        super().closeEvent(event)
        event.ignore()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MusicInterface()
    window.setMicaEffectEnabled(True)
    setTheme(Theme.AUTO)
    window.show()
    sys.exit(app.exec())
