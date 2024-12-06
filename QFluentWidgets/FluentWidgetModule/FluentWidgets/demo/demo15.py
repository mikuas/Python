import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QAction
from PySide6.QtWidgets import QWidget, QApplication, QListWidget, QListView

from FluentWidgets import SplitFluentWindow, VBoxLayout, VerticalScrollWidget, HBoxLayout, ButtonCard
from qfluentwidgets import FluentIcon, ImageLabel, TitleLabel, BodyLabel, TransparentPushButton, \
    PushButton, setTheme, Theme, CardWidget, Icon


class CustomCardWidget(QWidget):
    def __init__(self):
        super().__init__()
        l = QListView(self)
        l.addAction(
            QAction(Icon(FluentIcon.PLAY), 'play', self)
        )
        # TitleLabel("hello world", self)


class MusicListWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName('MusicListWidget')

        self.vBoxLayout = VBoxLayout(self)
        self.musicListWidget = VerticalScrollWidget(self)

        self.infoWidget = QWidget(self)
        self.infoWidget.setFixedHeight(150)
        self.rightLayout = VBoxLayout(self.infoWidget)
        self.rightToolLayout = HBoxLayout()

        self.vBoxLayout.addWidget(self.infoWidget)

        self.title = TitleLabel("我的音乐", self)
        self.content = BodyLabel("精心完善歌单信息有机会获得推荐,让更多用户看到你的大作", self)

        self.editButton = TransparentPushButton(FluentIcon.LABEL, "Edit", self)

        self.imageLabel = ImageLabel(r"C:\Projects\Items\Python\QFluentWidgets\App\data\music\星座になれたら-結束バンド\星座になれたら-結束バンド.jpg", self.infoWidget)
        self.imageLabel.setFixedSize(128, 128)
        print(self.imageLabel.width())
        self.rightLayout.setContentsMargins(self.imageLabel.width() + 20, 0, 0, 0)
        self.rightLayout.addWidget(self.editButton, alignment=Qt.AlignmentFlag.AlignRight)
        self.rightLayout.addWidgets(
            [self.title, self.content],
            alignment=Qt.AlignmentFlag.AlignLeft
        )
        self.rightLayout.addLayout(self.rightToolLayout)

        info = [
            ['播放', '下载', '批量', '分享'],
            [FluentIcon.PLAY_SOLID.colored(QColor(0, 255, 0), QColor(0, 255, 0)), FluentIcon.DOWNLOAD, FluentIcon.ALIGNMENT, FluentIcon.SHARE]
        ]

        for text, icon in zip(info[0], info[1]):
            button = PushButton(icon, text, self)
            button.setFixedWidth(100)
            self.rightToolLayout.addWidget(button)
            self.rightToolLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.vBoxLayout.addWidget(self.musicListWidget)

        for i in range(20):
            self.musicListWidget.vBoxLayout.addWidget(
                ButtonCard(
                    FluentIcon.HOME,
                    'Music List',
                    '',
                    '播放音乐'
                )
            )

        self.imageLabel.setContentsMargins(100, 50, 0, 0)
        self.imageLabel.move(10, 24)

class Window(SplitFluentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window")

        self.musicInterface = MusicListWidget()
        self.musicInterface.setContentsMargins(0, 30, 0, 0)

        self.addSubInterface(
            self.musicInterface,
            FluentIcon.MUSIC,
            'Music List'
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # window = Window()
    window = CustomCardWidget()
    setTheme(Theme.AUTO)
    window.show()
    sys.exit(app.exec())