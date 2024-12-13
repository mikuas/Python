import sys
from typing import Union

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QColor, QIcon, QImage, QPixmap
from PySide6.QtWidgets import QWidget, QApplication, QListWidgetItem, QListView, QTableWidgetItem, QTableWidget

from FluentWidgets import SplitFluentWindow, VBoxLayout, VerticalScrollWidget, HBoxLayout, TableWidget
from qfluentwidgets import FluentIcon, ImageLabel, TitleLabel, BodyLabel, TransparentPushButton, \
    PushButton, setTheme, Theme, IconWidget, ToolButton, FluentIconBase, ListWidget, SmoothMode, TransparentToolButton


class MusicWidget(QWidget):
    def __init__(self, image: Union[str, QImage, QPixmap] = None, content: str = None, parent=None):
        super().__init__(parent)
        self.hBoxLayout = HBoxLayout(self)
        self.leftLayout = HBoxLayout()
        self.centerLayout = HBoxLayout()
        self.rightLayout = HBoxLayout()
        self.hBoxLayout.addLayouts_(
            [self.leftLayout, self.centerLayout, self.rightLayout],
            [1, 2, 1]
        )

        self.icon = ImageLabel(image, self)
        self.icon.setFixedSize(32, 32)
        self.content = BodyLabel(content, self)
        self.playButton = TransparentToolButton(FluentIcon.PLAY, self)

        self.leftLayout.addWidgets([self.icon, self.content, self.playButton])
        self.content.setContentsMargins(10, 0, 0, 0)

        self.rightLayout.setContentsMargins(0, 0, 50, 0)

    def setIconSize(self, width: int, height: int):
        self.icon.setFixedSize(width, height)
        return self

    def setIcon(self, image: Union[str, QImage, QPixmap]):
        self.icon.setImage(image)
        return self

    def setContent(self, content: str):
        self.content.setText(content)
        return self

    def insertWidget(self, index: int = -1, widget: QWidget = None):
        self.hBoxLayout.insertWidget(index, widget)
        return self


class MusicListWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('MusicListWidget')
        self.vBoxLayout = VBoxLayout(self)
        self.infoWidget = QWidget(self)
        self.infoWidget.setFixedHeight(150)
        self.rightLayout = VBoxLayout(self.infoWidget)
        self.rightToolLayout = HBoxLayout()
        self.table = TableWidget(self)
        self.table.verticalHeader().hide()
        self.table.horizontalHeader().hide()
        self.table.setItemMinHeight(58)

        self.vBoxLayout.addWidget(self.infoWidget)

        self.title = TitleLabel("我的音乐", self)
        self.content = BodyLabel("精心完善歌单信息有机会获得推荐,让更多用户看到你的大作", self)
        self.editButton = TransparentPushButton(FluentIcon.LABEL, "Edit", self)
        self.imageLabel = ImageLabel(r"C:\Projects\Items\Python\QFluentWidgets\App\data\music\星座になれたら-結束バンド\星座になれたら-結束バンド.jpg", self.infoWidget)

        self.imageLabel.setFixedSize(128, 128)
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

    @staticmethod
    def getText(widget: QWidget):
        for child in widget.children():
            if isinstance(child, BodyLabel):
                return child.text()


class Window(SplitFluentWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1150, 680)
        desktop = QApplication.primaryScreen().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)
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
    window = Window()
    # window = MusicListItem(
    #     r"C:\Projects\Items\Python\QFluentWidgets\App\data\music\星座になれたら-結束バンド\星座になれたら-結束バンド.jpg",
    #     'Music List'
    # )
    setTheme(Theme.AUTO)
    window.show()
    sys.exit(app.exec())