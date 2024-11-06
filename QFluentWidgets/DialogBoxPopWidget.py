import sys

from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import Qt, QColor

from qfluentwidgets import SmoothScrollArea, VBoxLayout, MessageDialog, PrimaryPushButton, Dialog, MessageBox, \
    ColorDialog, FolderListDialog, FlyoutView, FluentIconBase, FluentIcon, Flyout, FlyoutAnimationType, TeachingTipView, \
    TeachingTipTailPosition, TeachingTip, InfoBarIcon, PopupTeachingTip, FlyoutViewBase, MessageBoxBase, SubtitleLabel, \
    LineEdit, CaptionLabel, PushButton, ImageLabel


class DialogBoxPopWidget(SmoothScrollArea):
    def __init__(self, text, parent=None):
        super().__init__(parent)

        self.initWindow()
        self.initWidget()
        self.initLayout()

        self.setObjectName(text.replace(' ', '_'))

    def initWindow(self):
        self.scrollWidget = QWidget()
        self.vLayout = VBoxLayout(self.scrollWidget)
        self.vLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)

    def initWidget(self):
        '''
            MaskDialogBase  遮罩对话框基类
            MessageBoxBase  消息对话框基类
            FlyoutViewBase  弹出视图基类
        '''

        '''Win10风格对话框'''
        # self.winButton = PrimaryPushButton("Win10风格对话框", self)
        # self.winButton.clicked.connect(
        #     lambda:
        #     MessageDialog(
        #         'Title',
        #         'Connect',
        #         self
        #     ).show()
        # )

        '''无边框消息对话框'''
        self.dialogButton = PrimaryPushButton("无边框消息对话框", self)
        self.dialogWindow = Dialog(
            "Title",
            "无边框消息对话框",
        )
        self.dialogWindow.yesButton.clicked.connect(
            lambda: print('确认')
        )
        self.dialogWindow.cancelButton.clicked.connect(
            lambda: print('取消')
        )
        self.dialogButton.clicked.connect(
            lambda:
            self.dialogWindow.show()
        )

        '''遮罩消息对话框'''
        self.messageBoxButton = PrimaryPushButton("遮罩消息对话框", self)
        mb = MessageBox(
            "Title",
            "遮罩消息对话框",
            self
        )
        mb.hide()
        mb.yesButton.setText('好的')
        mb.cancelButton.setText('下次一定')
        # 隐藏按钮
        # mb.yesButton.hide()
        # mb.cancelButton.hide()
        mb.yesButton.clicked.connect(
            lambda: print('确定')
        )
        mb.cancelButton.clicked.connect(
            lambda: print('取消')
        )
        self.messageBoxButton.clicked.connect(
            lambda: mb.show()
        )

        '''颜色对话框'''
        self.colorDialogButton = PrimaryPushButton('颜色对话框', self)
        cd = ColorDialog(
                QColor(255, 255, 255),
                "Title",
                self,
                False
            )
        cd.hide()
        cd.colorChanged.connect(lambda color: print(color.name()))
        self.colorDialogButton.clicked.connect(lambda: cd.show())

        '''Win10分割文件夹列表对话框'''
        # self.folderListButton = PrimaryPushButton('Win10分割文件夹列表对话框', self)
        # self.folderListButton.clicked.connect(
        #     lambda:
        #     FolderListDialog(
        #         ["1", "2", "3", "4", "5"],
        #         "Title",
        #         "Connect",
        #         self
        #     ).show()
        # )

        '''自定义对话框'''
        self.customButton = PrimaryPushButton('显示自定义对话框', self)
        self.customButton.clicked.connect(
            lambda:
            self.showMessage(self)
        )

        '''自定义弹出窗口'''
        self.flyoutViewButton = PrimaryPushButton("自定义弹出窗口", self)

        self.flyoutViewButton.clicked.connect(
            lambda:
            self.showFlyout(self.flyoutButton)
        )

        '''弹出窗口'''
        self.flyoutButton = PrimaryPushButton('弹出窗口', self)
        self.flyoutButton.clicked.connect(
            lambda:
            # AcrylicFlyout 亚力克弹出窗口
            Flyout.create(
                "Title",
                "弹出窗口",
                InfoBarIcon.SUCCESS,
                # image=, 图片路径
                isClosable=True,
                target=self.flyoutButton,
                parent=self,
                aniType=FlyoutAnimationType.PULL_UP,
                isDeleteOnClose=True
            )
        )

        '''自定义气泡弹窗'''
        self.teachingViewButton = PrimaryPushButton('自定义气泡弹窗', self)
        self.teachingViewButton.clicked.connect(
            lambda:
            self.showTeachView(
                self.teachingViewButton
            )
        )

        '''气泡弹窗'''
        self.teachingButton = PrimaryPushButton('气泡弹窗', self)
        self.teachingButton.clicked.connect(
            lambda:
            TeachingTip.create(
                self.teachingButton,
                "Title",
                'Connect',
                # InfoBarIcon.SUCCESS,
                image=r"C:\Users\Administrator\OneDrive\Pictures\fs.gif",
                isClosable=True,
                duration=2500, # 消失时间
                tailPosition=TeachingTipTailPosition.TOP,
                parent=self
            )
        )

        '''模态气泡弹窗'''
        self.popTeachingButton = PrimaryPushButton('模态气泡弹窗', self)
        # 点击空白处可直接关闭
        self.popTeachingButton.clicked.connect(
            lambda:
            PopupTeachingTip.create(
                self.popTeachingButton,
                "Title",
                '模态气泡弹窗',
                FluentIcon.GAME,
                duration=2500,
                tailPosition=TeachingTipTailPosition.BOTTOM,
                parent=self
            )
        )

    def initLayout(self):
        # self.vLayout.addWidget(self.winButton)
        self.vLayout.addWidget(self.dialogButton)
        self.vLayout.addWidget(self.messageBoxButton)
        self.vLayout.addWidget(self.colorDialogButton)
        self.vLayout.addWidget(self.customButton)
        # self.vLayout.addWidget(self.folderListButton)
        self.vLayout.addWidget(self.flyoutButton)
        self.vLayout.addWidget(self.flyoutViewButton)
        self.vLayout.addWidget(self.teachingButton)
        self.vLayout.addWidget(self.teachingViewButton)
        self.vLayout.addWidget(self.popTeachingButton)

    def showMessage(self, parent):
        w = CustomMessageBox(parent)
        if w.exec():
            print(w.urlLineEdit.text())

    def showFlyout(self, target):
        view = FlyoutView(
            "Title",
            "Connect",
            InfoBarIcon.ERROR,
            isClosable=True,
            parent=self
        )
        # 添加按钮
        button = PushButton("Action")
        button.setFixedWidth(120)
        img = ImageLabel(r"C:\Users\Administrator\OneDrive\Pictures\fs.gif", self)

        view.addWidget(img, align=Qt.AlignCenter)
        view.addWidget(button, align=Qt.AlignCenter)
        # 调整布局
        view.widgetLayout.insertSpacing(1, 5)
        view.widgetLayout.addSpacing(5)
        w = Flyout.make(view, target, self)
        view.closed.connect(w.close)

    def showTeachView(self, target):
        view = TeachingTipView(
            icon=None,
            title='Lesson 5',
            content="最短的捷径就是绕远路，绕远路才是我的最短捷径。",
            image=r"C:\Users\Administrator\OneDrive\Pictures\49.jpg",
            isClosable=True,
            tailPosition=TeachingTipTailPosition.BOTTOM,
        )

        # 添加组件
        button = PushButton('Action')
        button.setFixedWidth(120)
        view.addWidget(button, align=Qt.AlignRight)

        w = TeachingTip.make(
            target=target,
            view=view,
            duration=-1,  # 关闭自动消失
            tailPosition=TeachingTipTailPosition.BOTTOM,
            parent=self
        )
        view.closed.connect(w.close)


class CustomMessageBox(MessageBoxBase):
    """ 自定义对话框 """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel('打开 URL', self)
        self.urlLineEdit = LineEdit(self)

        self.urlLineEdit.setPlaceholderText('输入文件、流或者播放列表的 URL')
        self.urlLineEdit.setClearButtonEnabled(True)

        self.warningLabel = CaptionLabel("URL 不正确")
        self.warningLabel.setTextColor("#cf1010", QColor(255, 28, 32))

        # add widget to view layout
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.urlLineEdit)
        self.viewLayout.addWidget(self.warningLabel)
        self.warningLabel.hide()

        self.widget.setMinimumWidth(350)

    def validate(self):
        """ 重写验证表单数据的方法 """
        isValid = QUrl(self.urlLineEdit.text()).isValid()
        self.warningLabel.setHidden(isValid)
        return isValid




if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = DialogBoxPopWidget("DP")
    w.resize(1000, 600)
    w.show()
    sys.exit(app.exec())
