import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QWidget, QApplication, QHBoxLayout
from PySide6.QtGui import Qt, QColor

from qfluentwidgets import SmoothScrollArea, VBoxLayout, MessageDialog, PrimaryPushButton, Dialog, MessageBox, \
    InfoBadge, InfoLevel, PushButton, InfoBadgePosition, FluentIcon, DotInfoBadge, IconInfoBadge, FluentIconBase, \
    InfoBarIcon, InfoBar, InfoBarPosition, ProgressBar, IndeterminateProgressRing, IndeterminateProgressBar, BodyLabel, \
    TitleLabel, ProgressRing, ToolTip, ToolTipFilter, ToolTipPosition

from FluentWidgets import VerticalScrollWidget

class StatusInfoWidget(VerticalScrollWidget):
    def __init__(self, text, parent=None):
        super().__init__(parent)

        self.initWindow()
        self.initWidgets()
        self.initLayout()

        self.setObjectName(text.replace(' ', '_'))

    def initWindow(self):
        self.setWidgetResizable(True)

    def initWidgets(self):
        '''消息徽章'''
        # 通常附着在别的组件上 通过 target 指定
        self.infoBadge = InfoBadge(level=InfoLevel.SUCCESS)
        self.infoButton = PushButton(self)
        self.infoButton.setIcon(FluentIcon.GITHUB)
        # self.infoBadge.info()
        # self.infoBadge.attension()
        # self.infoBadge.warning()
        # self.infoBadge.error()
        # self.infoBadge.success(10, self, self.infoButton, InfoBadgePosition.TOP_RIGHT)
        self.infoBadge.custom("1W+", 'blue', 'green', self, self.infoButton, InfoBadgePosition.TOP_RIGHT)

        '''点状消息徽章'''
        self.dotInfo = DotInfoBadge(level=InfoLevel.SUCCESS)
        self.dotInfoButton = PushButton(self)
        self.dotInfoButton.setIcon(FluentIcon.HOME)
        self.dotInfo.warning(self, self.dotInfoButton, InfoBadgePosition.TOP_RIGHT)

        '''图标消息徽章'''
        self.iconInfo = IconInfoBadge(level=InfoLevel.SUCCESS)
        self.iconInfoButton = PushButton(self)
        self.iconInfoButton.setIcon(FluentIcon.MUSIC)
        self.iconInfo.attension(InfoBarIcon.ERROR, self, self.iconInfoButton, InfoBadgePosition.TOP_RIGHT)
        # self.iconInfo.warning(
        #
        # )

        '''消息条'''
        # 信息消息条
        self.infoButton = PrimaryPushButton('显示位于左上角信息消息条', self)
        self.infoButton.clicked.connect(
            lambda:
            InfoBar.info(
                '消息条',
                "这是一条信息消息条",
                duration=2500,
                position=InfoBarPosition.TOP_LEFT,
                parent=self
            )
        )

        # 成功消息条
        self.successButton = PrimaryPushButton('显示位于上方居中的成功消息条', self)
        self.successButton.clicked.connect(
            lambda:
            InfoBar.success(
                '消息条',
                '这是一条成功消息条',
                duration=2500,
                position=InfoBarPosition.TOP,
                parent=self
            )
        )

        # 失败消息条
        self.errorButton = PrimaryPushButton('显示位于左下角的失败消息条', self)
        self.errorButton.clicked.connect(
            lambda:
            InfoBar.error(
                "消息条",
                "这是一条失败消息条",
                duration=-1,
                position=InfoBarPosition.BOTTOM_LEFT,
                parent=self
            )
        )

        # 警告消息条
        self.warningButton = PrimaryPushButton('显示位于下方剧中的警告消息条', self)
        self.warningButton.clicked.connect(
            lambda:
            InfoBar.warning(
                '消息条',
                '这是一条警告消息条',
                duration=2500,
                position=InfoBarPosition.BOTTOM,
                parent=self
            )
        )

        # 自定义消息条
        self.newBarButton = PrimaryPushButton('显示自定义消息条', self)
        self.newBarButton.clicked.connect(
            lambda:
            InfoBar.new(
                FluentIcon.GITHUB,
                "消息条",
                '这是一条自定义消息条',
                orient=Qt.Horizontal,
                isClosable=True,
                duration=2500,
                position=InfoBarPosition.TOP_RIGHT,
                parent=self
            ).setCustomBackgroundColor('#2edebe', 'blue')
        )

        '''进度条'''
        self.pbl = TitleLabel('进度条', self)
        self.progressBar = ProgressBar(self)
        # set range
        self.progressBar.setRange(0, 100)
        # set current value
        self.progressBar.setValue(24)
        # set pause status, error status
        self.progressBar.pause()
        self.progressBar.error()
        # 恢复运行状态
        self.progressBar.resume()
        # 自定义进度条颜色
        self.progressBar.setCustomBackgroundColor(QColor(255, 0, 0), QColor(0, 255, 110))
        self.pbhLayout = QHBoxLayout()
        self.progressBarStartBt = PrimaryPushButton('启动进度条', self)
        self.progressBarStopBt = PrimaryPushButton('暂停', self)
        self.pbhLayout.addWidget(self.progressBarStartBt)
        self.pbhLayout.addWidget(self.progressBarStopBt)
        self.progressBarStartBt.clicked.connect(
            lambda: (
                print(self.progressBar.value()),
                self.startProgress(self.progressBar)
            )
        )
        self.progressBarStopBt.clicked.connect(
            lambda: self.time.stop()
        )

        '''不确定进度条'''
        self.ibl = TitleLabel('不确定进度条', self)
        self.indeterminateBar = IndeterminateProgressBar(self)
        # set pause status, error status
        # self.indeterminateBar.pause()
        # self.indeterminateBar.error()
        # 恢复运行状态
        # self.indeterminateBar.resume()


        '''进度环'''
        self.pr = TitleLabel('进度环', self)
        self.progressRing = ProgressRing(self)
        self.progressRing.setRange(0, 100)
        self.progressRing.setValue(24)
        # 显示进度环内文本
        self.progressRing.setTextVisible(True)
        # 调整进度换大小
        self.progressRing.setFixedSize(80, 80)
        # 调整厚度
        self.progressRing.setStrokeWidth(4)
        # 调整进度环文本格式, 比如显示温度
        # self.progressRing.setFormat('%v`C')

        '''不确定进度环'''
        self.ipr = TitleLabel('不确定进度环', self)
        self.indeterminateProgressRing = IndeterminateProgressRing(self)

        '''工具提示'''
        self.tipButton = PrimaryPushButton('悬停提示', self)
        self.tipButton.setToolTip('我是提示信息')
        self.tipButton.setToolTipDuration(1000)
        # 安装工具提示过滤器
        self.tipButton.installEventFilter(ToolTipFilter(self.tipButton, showDelay=300, position=ToolTipPosition.TOP))



    def initLayout(self):
        self.vLayout.addWidget(self.infoButton, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.dotInfoButton, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.iconInfoButton, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.infoButton, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.successButton, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.errorButton, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.warningButton, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.newBarButton, 0, Qt.AlignCenter)

        self.vLayout.addWidget(self.pbl, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.progressBar)
        self.vLayout.addLayout(self.pbhLayout)
        self.vLayout.addWidget(self.ibl, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.indeterminateBar)

        self.vLayout.addWidget(self.pr, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.progressRing, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.ipr, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.indeterminateProgressRing, 0, Qt.AlignCenter)

        self.vLayout.addWidget(self.tipButton, 0, Qt.AlignCenter)

    def startProgress(self, progress):
        self.time = QTimer(self)
        self.time.timeout.connect(lambda: progress.setValue(progress.value() + 1))
        self.time.start(500)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = StatusInfoWidget("MEDIA")
    w.resize(1000, 600)
    w.show()
    sys.exit(app.exec())

