import json
import time
import sys

from iconWidget import TrayIconWidget

from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (
    QApplication, QPushButton, QListWidget, QMainWindow, QToolButton, QVBoxLayout, QWidget, QButtonGroup, QHBoxLayout,
    QListWidgetItem, QStackedWidget, QSlider, QLabel, QSizePolicy, QProgressBar, QAbstractItemView)
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, Qt, QUrl, QTimer
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

from PyMyMethod.Method import FileControl, SystemCtl


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 创建修改时间标签QTimer对象
        self.videoButton = None
        self.utime = None  # QTimer()
        # 创建时间Label对象
        self.timeLabel = None  # QLabel()
        # 创建视频播放对象
        self.media = None  # QMediaPlayer()
        # 创建进度条QTimer对象
        self.timer = QTimer()
        self.progressBar = None  # QProgressBar()
        # 创建系统托盘
        TrayIconWidget(self, './data/images/icon/icon.png')
        self.setWindowTitle("Music")
        self.resize(1100, 600)
        # 暂停 播放按钮对象
        self.stopButton = None
        self.startIcon = r'./data/images/icon/start.png'
        self.stopIcon = r'./data/images/icon/stop.png'
        self.flag = True
        # 创建时间QLabel对象
        self.tLabel = QLabel()
        self.imgButton = QPushButton()

        # 列表布局
        self.listWidget = QListWidget()
        self.listWidget.setCursor(Qt.CursorShape.PointingHandCursor)
        self.listWidget.clicked.connect(lambda: (self.listClick(), self.startTime()))

        # 创建音频播放对象
        self.player = QMediaPlayer()
        # 创建音频输出对象
        self.audioOutput = QAudioOutput()
        self.player.setAudioOutput(self.audioOutput)
        self.player.mediaStatusChanged.connect(self.status)

        # 创建窗口叠堆对象
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(self.createMainWidget())
        self.stackedWidget.addWidget(self.createMusicWidget())
        self.stackedWidget.addWidget(self.createSetWidget())
        self.stackedWidget.addWidget(self.createVideoWidget())
        self.stackedWidget.addWidget(self.createHelpWidget())

        # 创建主窗口部件和布局
        # 设置横向布局
        self.mainWidget = QWidget()
        self.mainLayout = QHBoxLayout(self.mainWidget)
        # 纵向布局
        self.leftLayout = QVBoxLayout()
        self.rightLayout = QVBoxLayout()

        self.mainLayout.addLayout(self.leftLayout)
        self.mainLayout.addLayout(self.rightLayout)

        self.rightLayout.addWidget(self.stackedWidget)

        # 创建按钮对象
        self.createButton()

        # 设置布局对齐
        self.leftLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.rightLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setCentralWidget(self.mainWidget)

    # 创建主页对象
    def createMainWidget(self):
        widget = QWidget()
        mainLayout = QVBoxLayout(widget)

        topLayout = QHBoxLayout()

        leftLayout = QVBoxLayout()
        self.imgButton.setIcon(QIcon('./data/images/icon/list.png'))
        self.imgButton.setFixedSize(200, 200)
        self.imgButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.imgButton.setIconSize(QSize(200, 200))
        leftLayout.addWidget(self.imgButton)

        titleLayout = QVBoxLayout()
        self.tLabel.setText("None")
        self.tLabel.setFixedSize(400, 100)
        self.tLabel.setStyleSheet('font-size: 32px; color: #13e559;')
        titleLayout.addWidget(self.tLabel, alignment=Qt.AlignmentFlag.AlignCenter)

        rightLayout = QHBoxLayout()
        bts = ["上一首", "播放", "下一首"]
        icons = [
            './data/images/icon/up.png',
            './data/images/icon/stop.png',
            './data/images/icon/next.png'
        ]
        functions = [
            lambda: (self.startTime(), self.listWidget.setCurrentItem(self.listWidget.item(self.getListIndex() - 1)), self.setIndex()),
            self.updatePlay,
            lambda: (self.startTime(), self.listWidget.setCurrentItem(self.listWidget.item(self.getListIndex() + 1)), self.setIndex()),
        ]
        with open('./data/styles/Button.qss', 'r', encoding='utf-8') as f:
            style = f.read()
        for bt, ico, fc in zip(bts, icons, functions):
            button = QPushButton(bt)
            if bt == '播放':
                self.stopButton = button
            button.setIcon(QIcon(ico))
            button.setIconSize(QSize(40, 40))
            button.setStyleSheet(style)
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            button.clicked.connect(fc)
            button.setFixedSize(150, 80)
            rightLayout.addWidget(button, alignment=Qt.AlignmentFlag.AlignTop)
        titleLayout.addLayout(rightLayout)

        downLayout = QHBoxLayout()
        self.timeLabel = QLabel(widget)
        self.timeLabel.setStyleSheet("font-size: 24px")
        self.timeLabel.setText(f"Time: 00:00")
        self.progressBar = QProgressBar(widget)
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

        return widget

    # 创建进度条更新定时器
    def startTime(self):
        if QMediaPlayer.MediaStatus.LoadedMedia:
            self.progressBar.setValue(0)
            time.sleep(0.2)
            self.timer.timeout.connect(lambda: (print(f'播放位置: {self.player.position()}'), self.progressBar.setValue(self.player.position())))
            # 更新进度条的值
            # self.timer.timeout.connect(lambda: self.progressBar.setValue(self.player.position()))
            self.timer.start(100) # 0.1秒更新一次
            # 启动时间更新定时器
            self.startLabTime()

    # 创建时间更新定时器
    def startLabTime(self):
        self.utime = QTimer()
        # 更新时间的值
        self.utime.timeout.connect(self.updateTime)
        self.utime.start(100) # 0.1秒更新一次

    def updateTime(self):
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

    def setIndex(self):
        try:
            self.listWidget.itemChanged.connect(self.listClick())
            self.tLabel.setText(self.listWidget.selectedItems()[0].text().split('.')[0])
            self.imgButton.setIcon(QIcon(fr'./data/images/musicPictures/{self.getImgPath()[self.getListIndex()]}'))
        except IndexError:
            pass

    def listClick(self):
        self.flag = True
        self.stopButton.setIcon(QIcon(r'./data/images/icon/start.png'))
        self.stopButton.setText("暂停")
        self.play()

    def createMusicWidget(self):
        # set option height
        with open('./data/styles/QListStyle.qss', 'r', encoding='utf-8') as f:
            self.listWidget.setStyleSheet(f.read())
        for item, icon in zip(FileControl().getDirFiles(r'./data/musics'), self.getImgPath()):
            # set icon
            item = QListWidgetItem(item)
            print(icon)
            item.setIcon(QIcon(f'./data/images/musicPictures/{icon}'))
            self.listWidget.addItem(item)
            self.listWidget.setIconSize(QSize(32, 32))
        return self.listWidget

    def savePlayStatus(self):
        position = self.player.position()
        with open('position.json', 'w', encoding='utf-8') as f:
            json.dump({"position": position}, f)

    @staticmethod
    def sort(fileName):
        return int(fileName.split('.')[0])

    @staticmethod
    def createSetWidget():
        widget = QWidget()
        widget.setFixedHeight(400)

        layout = QVBoxLayout(widget)
        slider = QSlider(Qt.Orientation.Horizontal, widget)
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setValue(SystemCtl().getAudioEndpointVolume()[1] * 100 + 0.1)

        slider.valueChanged.connect(lambda: (
            objLab[-1].setText(str(f"当前音量: {slider.value()}")),
            SystemCtl().setAudio(slider.value() / 100)
        ))

        labs = ["设置音量", f'当前音量: {slider.value()}']
        objLab = []

        layout.addWidget(slider)
        for lab in labs:
            label = QLabel(lab, widget)
            label.setStyleSheet('font-size: 24px')
            layout.addWidget(label)
            objLab.append(label)

        return widget

    @staticmethod
    def createHelpWidget():
        widget = QWidget()
        mainLayout = QHBoxLayout(widget)

        button = QPushButton(widget)
        button.setFixedSize(350, 477)
        button.setIconSize(QSize(350, 477))
        button.setIcon(QIcon('./data/images/icon/money.png'))

        mainLayout.addWidget(button)

        return widget

    def status(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            # 获取当前项的索引
            self.listWidget.setCurrentItem(self.listWidget.item(self.getListIndex() + 1))
            self.listWidget.itemClicked.emit(self.listClick())
            self.startTime()
            print('END')
        # elif status == QMediaPlayer.MediaStatus.LoadedMedia:

    def createButton(self):
        BName = ['主页', '列表', '设置', "视频", '帮助', '退出']
        functions = [
            lambda: self.stackedWidget.setCurrentIndex(0),
            lambda: self.stackedWidget.setCurrentIndex(1),
            lambda: self.stackedWidget.setCurrentIndex(2),
            lambda: self.stackedWidget.setCurrentIndex(3),
            lambda: self.stackedWidget.setCurrentIndex(4),
            QApplication.quit
        ]
        icons = [
            r'./data/images/icon/home.png',
            r'./data/images/icon/list.png',
            r'./data/images/icon/setting.png',
            r'./data/images/icon/video.ico',
            r'./data/images/icon/help.png',
            r'./data/images/icon/exit.png'
        ]

        buttonGroup = QButtonGroup(self)
        buttonGroup.setExclusive(True)
        with open('./data/styles/GroupButton.qss', 'r', encoding='utf-8') as f:
            style = f.read()
        for name, fc, icon in zip(BName, functions, icons):
            button = QToolButton()
            if name == '主页':
                # 默认激活
                button.animateClick()
            button.setText(name)  # set button name
            button.setIcon(QIcon(icon))  # set icon
            button.setIconSize(QSize(40, 40))  # set icon size
            button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)  # set button style
            button.setFixedSize(80, 80)  # set fixed size
            button.setCheckable(True)
            button.setCursor(Qt.CursorShape.PointingHandCursor)  # set button hover style
            button.clicked.connect(fc)  # set click event
            button.setStyleSheet(style)  # set style
            buttonGroup.addButton(button)  # add group
            self.leftLayout.addWidget(button)

    def getListIndex(self):
        index = self.listWidget.currentRow()
        length = len(self.getImgPath())
        if index == 0:
            return 0
        elif index == length - 1:
            return length - 1
        elif 0 < index < length:
            return index
        else:
            return 1

    def updatePlay(self):
        if self.flag:
            self.savePlayStatus()
            time.sleep(0.1)
            self.player.stop()
            self.flag = False
            self.stopButton.setIcon(QIcon(self.stopIcon))
            self.stopButton.setText('播放')
            try:
                self.timer.stop()
                self.utime.stop()
            except Exception:
                pass
        else:
            with open('position.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
            time.sleep(0.1)
            self.player.setPosition(data['position'])
            self.player.play()
            self.stopButton.setIcon(QIcon(self.startIcon))
            self.stopButton.setText('暂停')
            self.flag = True
            try:
                self.timer.start(100)
                self.utime.start(100)
            except Exception:
                pass

    def getImgPath(self):
        return sorted(FileControl().getDirFiles(r'./data/images/musicPictures'), key=self.sort)

    def createVideoWidget(self):
        widget = QWidget()
        mainLayout = QVBoxLayout(widget)

        self.media = QMediaPlayer(widget)
        video = QVideoWidget(widget)
        video.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        video.setGeometry(self.rect())
        audio = QAudioOutput(widget)
        self.media.setVideoOutput(video)
        self.media.setAudioOutput(audio)
        self.media.setSource(QUrl("./data/videos/0.mp4"))

        buttonLayout = QHBoxLayout()
        btm = ["上一个", "播放", "下一个"]
        functions = [
            lambda: (self.unVideo(-1), self.updateBIT('暂停', self.startIcon)),
            self.updateVideoButton,
            lambda: (self.unVideo(1), self.updateBIT('暂停', self.startIcon))
        ]
        icons = [
            r'./data/images/icon/up.png',
            r'./data/images/icon/stop.png',
            r'./data/images/icon/next.png'
        ]
        with open('./data/styles/Button.qss', 'r', encoding='utf-8') as f:
            style = f.read()
        for b, fc, icon in zip(btm, functions, icons):
            button = QPushButton(b)
            if b == '播放':
                self.videoButton = button
            button.setIcon(QIcon(icon))
            button.setIconSize(QSize(40, 40))
            button.setStyleSheet(style)
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            button.setFixedHeight(100)
            button.clicked.connect(fc)
            buttonLayout.addWidget(button)

        mainLayout.addWidget(video)
        mainLayout.addLayout(buttonLayout)
        return widget

    def updateVideoButton(self):
        if self.videoButton.text() == '播放':
            self.updateBIT('暂停', self.startIcon)
            self.media.play()
        else:
            self.updateBIT('播放', self.stopIcon)
            self.media.pause()

    def updateBIT(self, text, icon):
        self.videoButton.setText(text)
        self.videoButton.setIcon(QIcon(icon))

    def play(self):
        try:
            self.player.stop()
            time.sleep(0.1)
            print(True)
            path = fr"./data/musics/{self.listWidget.selectedItems()[0].text()}"
            print(path)
            self.player.setSource(QUrl.fromLocalFile(path))
            self.player.play()
            self.tLabel.setText(self.listWidget.selectedItems()[0].text().split('.')[0])
            self.imgButton.setIcon(QIcon(fr'./data/images/musicPictures/{self.getImgPath()[self.getListIndex()]}'))
        except IndexError:
            pass

    def unVideo(self, num):
        with open('../Test/MusicAppTS/videoPath.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.media.stop()
        time.sleep(0.1)
        key = int(self.media.source().url().split('/')[-1].split('.')[-2][-1]) + num
        length = len(data)
        if key >= length:
            key = 0
        elif key < 0:
            key = str(length - 1)
        self.media.setSource(QUrl(data[str(key)]))
        print(data[str(key)])
        time.sleep(0.1)
        self.media.play()

    @staticmethod
    def quitApp():
        # 关闭所有窗口
        for widget in QApplication.topLevelWidgets():
            widget.close()
        # 退出软件
        QApplication.quit()

    def closeEvent(self, event):
        event.ignore()
        self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
