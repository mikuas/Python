import sys

from PySide6.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QVBoxLayout, QWidget
from PySide6.QtGui import Qt
from qfluentwidgets import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 450)
        centerWindget = QWidget(self)
        mainLayout = QVBoxLayout(centerWindget)

        '''卡片组件'''
        self.card = AppCard(
            FluentIcon.HOME,
            "Title",
            "Hello World"
        )

        # 连接信号插槽
        self.card.clicked.connect(lambda : print(True))
        # 设置圆角大小
        self.card.setBorderRadius(8)

        self.card2 = AppCard(
            FluentIcon.GITHUB,
            "Title",
            "Hello World"
        )

        # 设置圆角大小
        self.card.setBorderRadius(8)
        self.card2.setBorderRadius(8)

        self.emoCard = EmojiCard(
            r"C:\Users\Administrator\OneDrive\Pictures\14.jpg",
            "Title",
        )

        self.groupCard = SettinsCard()
        mainLayout.addWidget(self.card)
        mainLayout.addWidget(self.card2)
        mainLayout.addWidget(self.emoCard)
        mainLayout.addWidget(self.groupCard)
        self.setCentralWidget(centerWindget)

# 卡片
class AppCard(CardWidget):

    def __init__(self, icon, title, content, parent=None):
        super().__init__(parent)
        self.iconWidget = IconWidget(icon)
        self.titleLabel = BodyLabel(title, self)
        self.contentLabel = CaptionLabel(content, self)
        self.openButton = PushButton('Open', self)
        self.openButton.clicked.connect(
            lambda : print("Click")
        )
        self.moreButton = TransparentToolButton(FluentIcon.MORE, self)
        self.moreButton.clicked.connect(self.showFlyout)

        self.hBoxLayout = QHBoxLayout(self)
        self.vBoxLayout = QVBoxLayout()

        self.setFixedHeight(73)
        self.iconWidget.setFixedSize(48, 48)
        self.contentLabel.setTextColor("#606060", "#d2d2d2")
        self.openButton.setFixedWidth(120)

        self.hBoxLayout.setContentsMargins(20, 11, 11, 11)
        self.hBoxLayout.setSpacing(15)
        self.hBoxLayout.addWidget(self.iconWidget)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.addWidget(self.titleLabel, 0, Qt.AlignVCenter)
        self.vBoxLayout.addWidget(self.contentLabel, 0, Qt.AlignVCenter)
        self.vBoxLayout.setAlignment(Qt.AlignVCenter)
        self.hBoxLayout.addLayout(self.vBoxLayout)

        self.hBoxLayout.addStretch(1)
        self.hBoxLayout.addWidget(self.openButton, 0, Qt.AlignRight)
        self.hBoxLayout.addWidget(self.moreButton, 0, Qt.AlignRight)

        self.moreButton.setFixedSize(32, 32)

    def showFlyout(self):
        Flyout.create(
            "Title",
            '暂未编写该功能😓',
            InfoBarIcon.WARNING,
            target=self.moreButton,
            parent=self
        )


class EmojiCard(ElevatedCardWidget):

    def __init__(self, iconPath: str, name: str, parent=None):
        super().__init__(parent)
        self.iconWidget = ImageLabel(iconPath, self)
        self.label = CaptionLabel(name, self)

        self.iconWidget.scaledToHeight(68)

        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.setAlignment(Qt.AlignCenter)
        self.vBoxLayout.addStretch(1)
        self.vBoxLayout.addWidget(self.iconWidget, 0, Qt.AlignCenter)
        self.vBoxLayout.addStretch(1)
        self.vBoxLayout.addWidget(self.label, 0, Qt.AlignHCenter | Qt.AlignBottom)

        self.setFixedSize(168, 176)

# 组卡片
class SettinsCard(GroupHeaderCardWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle("基本设置")
        self.setBorderRadius(8)

        self.chooseButton = PushButton("选择")
        self.chooseButton.clicked.connect(
            self.showTeaching
        )
        self.comboBox = ComboBox()
        self.lineEdit = SearchLineEdit()

        self.hintIcon = IconWidget(InfoBarIcon.INFORMATION)
        self.hintLabel = BodyLabel("点击编译按钮以开始打包 👉")
        self.compileButton = PrimaryPushButton(FluentIcon.PLAY_SOLID, "编译")
        self.openButton = PushButton(FluentIcon.VIEW, "打开")
        self.bottomLayout = QHBoxLayout()

        self.chooseButton.setFixedWidth(120)
        self.lineEdit.setFixedWidth(320)
        self.comboBox.setFixedWidth(320)
        self.comboBox.addItems(["始终显示（首次打包时建议启用）", "始终隐藏"])
        self.lineEdit.setPlaceholderText("输入入口脚本的路径")

        # 设置底部工具栏布局
        self.hintIcon.setFixedSize(16, 16)
        self.bottomLayout.setSpacing(10)
        self.bottomLayout.setContentsMargins(24, 15, 24, 20)
        self.bottomLayout.addWidget(self.hintIcon, 0, Qt.AlignLeft)
        self.bottomLayout.addWidget(self.hintLabel, 0, Qt.AlignLeft)
        self.bottomLayout.addStretch(1)
        self.bottomLayout.addWidget(self.openButton, 0, Qt.AlignRight)
        self.bottomLayout.addWidget(self.compileButton, 0, Qt.AlignRight)
        self.bottomLayout.setAlignment(Qt.AlignVCenter)

        # 添加组件到分组中
        self.addGroup(FluentIcon.GITHUB, "构建目录", "选择 Nuitka 的输出目录", self.chooseButton)
        self.addGroup(FluentIcon.MUSIC, "运行终端", "设置是否显示命令行终端", self.comboBox)
        group = self.addGroup(FluentIcon.VIEW, "入口脚本", "选择软件的入口脚本", self.lineEdit)
        group.setSeparatorVisible(True)

        # 添加底部工具栏
        self.vBoxLayout.addLayout(self.bottomLayout)

    def showTeaching(self):
        TeachingTip.create(
            self.chooseButton,
            "Title",
            "没有该功能",
            InfoBarIcon.WARNING,
            duration=2000,
            parent=self
        )


# 组卡片
class GroupCard(GroupHeaderCardWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle("系统工具")
        self.setBorderRadius(8)

        self.initLayout()
        self.initGroup()
        self.connectSignalSlots()

    def initGroup(self):
        self.wifiButton = SwitchButton(self)
        self.addGroup(
            FluentIcon.WIFI,
            "WIFI",
            "连接wifi网络",
            self.wifiButton
        ).setSeparatorVisible(True)

        # 添加底部工具栏
        self.vBoxLayout.addLayout(self.pauseLayout)
        self.vBoxLayout.addLayout(self.addBootLayout)

    # 连接信号插槽
    def connectSignalSlots(self):
        self.wifiButton.checkedChanged.connect(
            lambda b: TeachingTip.create(
                self.wifiButton,
                'WIFI',
                "已开启WIFI网络😊" if b else "已关闭WIFI网络😰",
                InfoBarIcon.SUCCESS,
                isClosable=False,
                duration=1500,
                parent=self
            )
        )
        self.pauseButton.clicked.connect(
            lambda: (
                Regedit().setWindowsUpdateDays(int(self.daysEidt.text())),
                TeachingTip.create(
                    self.pauseButton,
                    "暂停天数",
                    f'成功设置最大暂停天数{self.daysEidt.text()}天🥰',
                    InfoBarIcon.SUCCESS,
                    isClosable=False,
                    duration=1500,
                    parent=self
                )
            )
        )

    def initLayout(self):
        self.pauseLayout = QHBoxLayout()
        self.addBootLayout = QHBoxLayout()

        self.pauseIcon = IconWidget(FluentIcon.UPDATE)
        self.daysLabel = BodyLabel("设置Windows最大暂停更新天数")

        self.daysEidt = EditableComboBox()
        self.daysEidt.setPlaceholderText("暂停天数")
        self.daysEidt.addItems(['100', '500', '1000', '36500'])

        self.pauseButton = PrimaryToolButton()
        self.pauseButton.setText('确定')

        self.pauseIcon.setFixedSize(20, 20)
        self.pauseLayout.setSpacing(10)
        self.pauseLayout.setContentsMargins(24, 15, 24, 20)

        self.pauseLayout.addWidget(self.pauseIcon, 0, Qt.AlignLeft)
        self.pauseLayout.addWidget(self.daysLabel, 0, Qt.AlignLeft)
        self.pauseLayout.addStretch(1)
        self.pauseLayout.addWidget(self.daysEidt, 0, Qt.AlignRight)
        self.pauseLayout.addWidget(self.pauseButton, 0, Qt.AlignRight)
        self.pauseLayout.setAlignment(Qt.AlignVCenter)
        # --------------------------------------------------------------------
        self.addButton = PrimaryToolButton()
        self.addButton.setText("确定")
        self.addIcon = IconWidget(FluentIcon.POWER_BUTTON)
        self.addLabel = BodyLabel("添加开机自启动项")
        self.selectButton = PushButton()
        self.selectButton.setText('选择文件路径')
        self.selectButton.setIcon(Icon(FluentIcon.FOLDER))
        self.addIcon.setFixedSize(20, 20)

        self.addBootLayout.setSpacing(10)
        self.addBootLayout.setContentsMargins(24, 15, 24, 20)

        self.addBootLayout.addWidget(self.addIcon, 0, Qt.AlignLeft)
        self.addBootLayout.addWidget(self.addLabel, 0, Qt.AlignLeft)
        self.addBootLayout.addStretch(1)
        self.addBootLayout.addWidget(self.selectButton, 0, Qt.AlignRight)
        self.addBootLayout.addWidget(self.addButton, 0, Qt.AlignRight)
        self.addBootLayout.setAlignment(Qt.AlignVCenter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())