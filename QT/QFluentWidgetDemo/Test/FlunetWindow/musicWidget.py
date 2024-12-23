import sys

from PySide6.QtCore import Qt, QSize, QTimer
from PySide6.QtGui import QStandardItemModel, QStandardItem, QIcon, QFont
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from qfluentwidgets import Icon, FluentIcon, BodyLabel, ListView, qconfig, Theme, TransparentToolButton, ToolTipFilter, \
    theme

from PyMyMethod import FileControl
from qfluentwidgets.multimedia import StandardMediaPlayBar, MediaPlayer


class MusicWidget(QWidget):

    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Music")
        self.setWindowIcon(Icon(FluentIcon.MUSIC))

        self.T = QTimer(self)
        self.hLayout = QHBoxLayout(self)
        self.vLayout = QVBoxLayout()
        self.hLayout.addLayout(self.vLayout)

        self.listWidget = ListView()
        self.mediaBar = StandardMediaPlayBar()
        self.label = BodyLabel("暂无歌曲信息", self)
        self.model = QStandardItemModel()

        self.initMediaButton()
        self.initMedia()
        self.initListWidget()
        self.initStyle()

        self.vLayout.addWidget(self.listWidget)
        self.vLayout.addWidget(self.mediaBar)

        # 连接信号槽
        self.connectSignalSlots()

        self.resize(1000, 600)
        self.setObjectName(text.replace(' ', '_'))

    def connectSignalSlots(self):
        self.listWidget.clicked.connect(
            lambda element: (
                print(self.model.data(element)),
                self.updateMediaSource(f'./data/musics/{self.model.data(element)}'),
                self.label.setText(self.model.data(element).split('.')[0]),
            )
        )

        self.mediaBar.player.mediaStatusChanged.connect(lambda status: self.mediaStatus(status))

        self.up.clicked.connect(lambda: self.updateMusic(-1))
        self.next.clicked.connect(lambda: self.updateMusic(1))

        qconfig.themeChanged.connect(lambda theme: self.applyStyle(theme))
        qconfig.themeColor.valueChanged.connect(lambda: self.applyStyle(theme()))

    def initListWidget(self):
        datas = [f'./data/musics/{i} ' for i in FileControl().getDirFiles('data/musics')]
        img = FileControl().getDirFiles('data/musicImg')
        for data in datas:
            name = data.split('/')[-1]
            self.model.appendRow(
                QStandardItem(
                    QIcon(f"./data/musicImg/{name.split('.')[0]}.png"
                          if f"{name.split('.')[0]}.png" in img
                          else './data/images/icon/neow.gif'), name
                )
            )

        self.listWidget.setModel(self.model)
        self.listWidget.setSelectRightClickedRow(True)

    def initMedia(self):
        self.mediaBar.leftButtonLayout.addWidget(self.label)
        self.mediaBar.rightButtonLayout.addWidget(self.mediaBar.volumeButton)
        self.mediaBar.player.setVolume(100)

        # 插入到第一位
        self.mediaBar.centerButtonLayout.insertWidget(0, self.up)
        self.mediaBar.centerButtonLayout.addWidget(self.next)

    def initMediaButton(self):
        self.up = TransparentToolButton(FluentIcon.LEFT_ARROW, self)
        self.next = TransparentToolButton(FluentIcon.RIGHT_ARROW, self)

        self.up.setToolTip("上一首")
        self.up.setToolTipDuration(-1)
        self.up.installEventFilter(ToolTipFilter(self.up))

        self.next.setToolTip("下一首")
        self.next.setToolTipDuration(-1)
        self.next.installEventFilter(ToolTipFilter(self.next))

        self.mediaBar.volumeButton.setToolTip("调整音量")
        self.mediaBar.volumeButton.setToolTipDuration(-1)
        self.mediaBar.volumeButton.installEventFilter(self.mediaBar.volumeButton)

        self.mediaBar.skipBackButton.setToolTip("后退10秒")
        self.mediaBar.skipBackButton.setToolTipDuration(-1)
        self.mediaBar.skipBackButton.installEventFilter(self.mediaBar.skipBackButton)

        self.mediaBar.skipForwardButton.setToolTip("前进30秒")
        self.mediaBar.skipForwardButton.setToolTipDuration(-1)
        self.mediaBar.skipForwardButton.installEventFilter(self.mediaBar.skipForwardButton)

    def initStyle(self, theme='LIGHT_ListView'):
        self.label.setStyleSheet('font-size: 24px; color: #ec48ac')

        self.listWidget.setSpacing(4)
        self.listWidget.setFocusPolicy(Qt.NoFocus)
        self.listWidget.setIconSize(QSize(48, 48))
        self.listWidget.setFont(QFont('Arial', 48))
        self.listWidget.setStyleSheet(FileControl().readQssFile(f'./data/styles/{theme}.qss'))

    def updateMediaSource(self, url):
        self.mediaBar.player.setSource(url)
        self.mediaBar.player.play()

    def applyStyle(self, theme):
        if theme == Theme.DARK:
            theme = 'DARK_ListView'
        else:
            theme = 'LIGHT_ListView'
        self.T.timeout.connect(lambda: (self.initStyle(theme), self.T.stop()))
        self.T.start(500)

    def updateMusic(self, num):
        index = self.listWidget.currentIndex()
        if index.isValid():
            nextIndex = self.listWidget.model().index(index.row() + num, index.column())
            if nextIndex.isValid():
                self.listWidget.setCurrentIndex(nextIndex)
                self.listWidget.clicked.emit(nextIndex)

    def mediaStatus(self, status):
        if status == MediaPlayer.MediaStatus.EndOfMedia:
            self.updateMusic(1)

    def setListStyle(self, theme):
        self.T.start(1000)
        if theme == Theme.DARK:
            self.listWidget.setStyleSheet('background-color: rgb(255, 255, 255);')

    def resizeEvent(self, event):
        self.mediaBar.leftButtonContainer.setMaximumWidth(self.width() / 3)

    def contextMenuEvent(self, event):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MusicWidget("MUSIC")
    w.show()
    sys.exit(app.exec())