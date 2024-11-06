import sys

from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import Qt, QColor

from qfluentwidgets import SmoothScrollArea, VBoxLayout, MessageDialog, PrimaryPushButton, Dialog, MessageBox, \
    ColorDialog, FolderListDialog, FlyoutView, FluentIconBase, FluentIcon, Flyout, FlyoutAnimationType, TeachingTipView, \
    TeachingTipTailPosition, TeachingTip, InfoBarIcon, PopupTeachingTip, FlyoutViewBase
from qfluentwidgets.multimedia import MediaPlayBarButton, SimpleMediaPlayBar, StandardMediaPlayBar, MediaPlayer, \
    VideoWidget
from qfluentwidgets.multimedia.media_play_bar import VolumeView
from qfluentwidgets.multimedia.video_widget import GraphicsVideoItem


class MediaWidget(SmoothScrollArea):
    def __init__(self, text, parent=None):
        super().__init__(parent)

        self.initWindow()
        self.initWidgets()
        self.initLayout()

        self.setObjectName(text.replace(' ', '_'))

    def initWindow(self):
        self.scrollWidget = QWidget()
        self.vLayout = VBoxLayout(self.scrollWidget)
        self.vLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)

    def initWidgets(self):
        '''
            MediaPlayBarBase    播放栏基类
            MediaPlayerBase     播放器基类
        '''

        '''播放栏按钮'''
        self.mediaPlayButton = MediaPlayBarButton(self)
        self.mediaPlayButton.clicked.connect(lambda: print(True))

        '''音量弹出视图'''
        self.volumeViewButton = PrimaryPushButton('音量弹出视图', self)
        self.volumeViewButton.clicked.connect(
            lambda:
            VolumeView(
                self
            ).show()
        )

        '''简单播放栏'''
        self.playBar = SimpleMediaPlayBar(self)

        '''标准播放栏'''
        self.standarPlayBar = StandardMediaPlayBar(self)

        '''播放器'''
        self.player = MediaPlayer(self)

        '''视频图元'''
        self.video = GraphicsVideoItem()

        '''视频播放组件'''
        self.videoWidget = VideoWidget()

    def initLayout(self):
        self.vLayout.addWidget(self.mediaPlayButton)
        self.vLayout.addWidget(self.volumeViewButton)
        self.vLayout.addWidget(self.playBar)
        self.vLayout.addWidget(self.standarPlayBar)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MediaWidget("MEDIA")
    w.resize(1000, 600)
    w.show()
    sys.exit(app.exec())