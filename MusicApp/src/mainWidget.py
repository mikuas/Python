import time

from PySide6.QtWidgets import QWidget, QListWidget, QListWidgetItem, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QProgressBar
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtGui import QIcon, Qt
from PySide6.QtCore import QSize, QUrl, QTimer

from PyMyMethod.Method import FileControl
from .fileControl import File
from .qtControl import QC
from .createMainButton import createButton


# 主页控件
class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.startIcon = r'../../data/images/icon/start.png'
        self.stopIcon = r'../../data/images/icon/stop.png'
        self.flag = False
        self.stopButton = None
        # 定时器
        self.tlTimer = QTimer()
        self.startTimer = QTimer()
        self.imgButton = QPushButton()
        self.tLabel = QLabel()

        # 音乐列表控件
        self.listWidget = QListWidget()
        self.listWidget.setCursor(Qt.CursorShape.PointingHandCursor)
        self.listWidget.clicked.connect(lambda: (self.listItemClick(), self.startTime()))

        # 音频控件
        self.player = QMediaPlayer()
        # 音频输出控件
        self.audioOutput = QAudioOutput()
        self.player.setAudioOutput(self.audioOutput)
        # 连接信号插槽
        self.player.mediaStatusChanged.connect(self.status)

        self.createMainWidget()

        # 创建主窗口部件和布局
        # 设置横向布局
        self.mainWidget = QWidget()
        self.mainLayout = QHBoxLayout(self.mainWidget)

    def createMainWidget(self):
        mainLayout = QVBoxLayout(self)

        topLayout = QHBoxLayout()

        leftLayout = QVBoxLayout()
        self.imgButton.setIcon(QIcon('../data/images/icon/list.png'))
        self.imgButton.setFixedSize(200, 200)
        self.imgButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.imgButton.setIconSize(QSize(200, 200))
        leftLayout.addWidget(self.imgButton)

        titleLayout = QVBoxLayout()
        self.tLabel.setText("None")
        self.tLabel.setFixedSize(400, 100)
        self.tLabel.setStyleSheet('font-size: 32px; color: #13e559;')
        titleLayout.addWidget(self.tLabel, alignment=Qt.AlignmentFlag.AlignCenter)

        functions = [
            lambda: (
                self.startTime(),
                self.listWidget.setCurrentItem(self.listWidget.item(QC().getLastIndex(self.listWidget))),
                self.setIndex()),
            self.updatePlay,
            lambda: (
                self.startTime(),
                self.listWidget.setCurrentItem(self.listWidget.item(QC().getNextIndex(self.listWidget))),
                self.setIndex()),
        ]
        rt = createButton(
            ["上一首", "播放", "下一首"],
            [
                '../../data/images/icon/up.png',
                '../../data/images/icon/stop.png',
                '../../data/images/icon/next.png',
            ],
            File.readFile('../data/styles/Button.qss'),
            functions
        )
        self.stopButton = rt[1]
        titleLayout.addLayout(rt[0])

        downLayout = QHBoxLayout()
        self.timeLabel = QLabel(self)
        self.timeLabel.setStyleSheet("font-size: 24px")
        self.timeLabel.setText(f"Time: 00:00")
        self.progressBar = QProgressBar(self)
        self.progressBar.setMinimum(0)
        n = QLabel()
        n.setFixedSize(150, 50)
        downLayout.addWidget(n)
        downLayout.addWidget(self.timeLabel, stretch=1)
        downLayout.addWidget(self.progressBar, stretch=2)
        downLayout.addWidget(n)

        topLayout.addLayout(leftLayout)
        topLayout.addLayout(titleLayout)

        none = QLabel()
        none.setFixedHeight(100)

        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(downLayout)
        mainLayout.addWidget(none)

    def createMusicWidget(self):
        # set option height
        self.listWidget.setStyleSheet(File.readFile('../data/styles/QListStyle.qss'))
        for item, icon in zip(FileControl().getDirFiles(r'../data/musics'), File.getImagePath(
                '../data/images/musicPictures/')):
            # set icon
            item = QListWidgetItem(item)
            print(icon)
            item.setIcon(QIcon(icon))
            self.listWidget.addItem(item)
            self.listWidget.setIconSize(QSize(32, 32))
        return self.listWidget

    # 创建进度条更新定时器
    def startTime(self):
        if QMediaPlayer.MediaStatus.LoadedMedia:
            self.progressBar.setValue(0)
            time.sleep(0.2)
            # self.startTimer.timeout.connect(lambda: (print(f'播放位置: {self.player.position()}'),self.progressBar.setValue(self.player.position())))
            # 更新进度条的值
            self.startTimer.timeout.connect(lambda: self.progressBar.setValue(self.player.position()))
            self.startTimer.start(100)  # 0.1秒更新一次
            # 启动时间更新定时器
            self.startLabTime()

    # 创建时间更新定时器
    def startLabTime(self):
        # 更新时间的值
        self.tlTimer.timeout.connect(self.updateTime)
        self.tlTimer.start(100)  # 0.1秒更新一次

    def updateTime(self):
        print(f'Index     {self.listWidget.currentRow(), type(self.listWidget.currentRow())}')
        # 获取总时长
        ams = QMediaPlayer.duration(self.player) - self.player.position()
        print(f'总时间: {QMediaPlayer.duration(self.player)}')
        self.progressBar.setMaximum(QMediaPlayer.duration(self.player) - 2)
        ms = ams / 1000
        MIN = int(ms / 60)
        MS = int(ms - MIN * 60)
        print(f'时间: {MIN}分钟 {ms}秒')
        if MS < 10:
            MS = "0" + str(MS)
        # 更新时间
        self.timeLabel.setText(f"Time: {MIN}:{MS}")

    def listItemClick(self):
        self.flag = True
        QC.setIT(self.stopButton, self.startIcon, '暂停')
        self.play()

    def play(self):
        try:
            self.player.stop()
            time.sleep(0.1)
            print(True)
            path = fr"../../../../MusicApp/data/musics/{self.listWidget.selectedItems()[0].text()}"
            print(path)
            self.player.setSource(QUrl.fromLocalFile(path))
            self.player.play()
            self.tLabel.setText(self.listWidget.selectedItems()[0].text().split('.')[0])
            self.imgButton.setIcon(QIcon(File.getImagePath(
                '../data/images/musicPictures/')[QC.getListIndex(self.listWidget)]))
        except IndexError:
            pass

    def updatePlay(self):
        if self.flag:
            File.saveJsonFile('position', self.player.position(), '../data/json/position.json')
            time.sleep(0.1)
            self.player.stop()
            self.flag = False
            QC.setIT(self.stopButton, self.stopIcon, '播放')
            try:
                self.startTimer.stop()
                self.tlTimer.stop()
            except Exception:
                pass
        else:
            data = File.readJsonFile('../data/json/position.json')
            time.sleep(0.1)
            self.player.setPosition(data['position'])
            self.player.play()
            QC.setIT(self.stopButton, self.startIcon, '暂停')
            self.flag = True
            try:
                self.startTimer.start(100)
                self.tlTimer.start(100)
            except Exception:
                pass

    def status(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            # 获取当前项的索引
            self.listWidget.setCurrentItem(self.listWidget.item(QC.getListIndex(self.listWidget) + 1))
            self.listWidget.itemClicked.emit(self.listItemClick())
            self.startTime()
            print('END')
        # elif status == QMediaPlayer.MediaStatus.LoadedMedia:

    def setIndex(self):
        try:
            self.listWidget.itemChanged.connect(self.listItemClick())
            self.tLabel.setText(self.listWidget.selectedItems()[0].text().split('.')[0])
            self.imgButton.setIcon(QIcon(File.getImagePath(
                '../data/images/musicPictures/')[QC.getListIndex(self.listWidget)]))
        except IndexError:
            pass