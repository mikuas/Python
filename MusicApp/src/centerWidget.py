from PySide6.QtWidgets import (QMainWindow, QStackedWidget, QWidget, QHBoxLayout,
                               QVBoxLayout, QButtonGroup, QApplication, QToolButton)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QSize

from .mainWidget import MainWidget
from .vidoeWidget import VideoWidget
from .settingsWidget import SetWidget
from .helpWidget import HelpWidget
from .trayIconWIdget import TrayIconWidget

from MusicApp.src.fileControl import File


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建系统托盘
        TrayIconWidget(self, '../data/images/icon/icon.png')
        self.setWindowTitle("Music")
        self.resize(1100, 600)

        self.stackedWidget = QStackedWidget()  # 创建堆叠窗口小部件
        self.MainWidget = MainWidget()
        self.stackedWidget.addWidget(self.MainWidget)  # 添加主页面
        self.stackedWidget.addWidget(self.MainWidget.createMusicWidget())  # 添加音乐页面
        self.stackedWidget.addWidget(VideoWidget())  # 添加视频页面
        self.stackedWidget.addWidget(SetWidget())  # 添加设置页面
        self.stackedWidget.addWidget(HelpWidget())  # 添加帮助页面

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


    def createButton(self):
        BName = ['主页', '列表', '视频', "设置", '帮助', '退出']
        functions = [
            lambda: self.stackedWidget.setCurrentIndex(0),
            lambda: self.stackedWidget.setCurrentIndex(1),
            lambda: self.stackedWidget.setCurrentIndex(2),
            lambda: self.stackedWidget.setCurrentIndex(3),
            lambda: self.stackedWidget.setCurrentIndex(4),
            QApplication.quit
        ]
        icons = [
            # FluentIcon.HOME,
            # FluentIcon.MUSIC,
            # FluentIcon.VIDEO,
            # FluentIcon.SETTING,
            # FluentIcon.HELP,
            # FluentIcon.EDIT,
            r'../../data/images/icon/home.png',
            r'../../data/images/icon/list.png',
            r'../../data/images/icon/video.ico',
            r'../../data/images/icon/setting.png',
            r'../../data/images/icon/help.png',
            r'../../data/images/icon/exit.png'
        ]

        buttonGroup = QButtonGroup(self)
        buttonGroup.setExclusive(True)
        style = File.readFile('../data/styles/GroupButton.qss')
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