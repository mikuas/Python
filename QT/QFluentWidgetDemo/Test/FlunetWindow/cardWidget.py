import sys
import threading
from typing import Union

from PySide6.QtWidgets import QHBoxLayout, QApplication, QVBoxLayout, QWidget
from PySide6.QtGui import Qt, QIcon

from qfluentwidgets import FluentIcon, CardWidget, IconWidget, BodyLabel, CaptionLabel, PushButton, ElevatedCardWidget, \
    ImageLabel, PrimaryPushButton, InfoBarIcon, qconfig, Theme, PrimaryToolButton, InfoBar, InfoBarPosition, \
    TeachingTip, \
    EditableComboBox, ComboBoxSettingCard, OptionsConfigItem, OptionsValidator, Icon, SwitchSettingCard, ConfigItem, \
    BoolValidator, Flyout, FlyoutView, FlyoutAnimationType, SettingCardGroup, HyperlinkCard, PrimaryPushSettingCard, \
    SmoothScrollArea, VBoxLayout, ComboBox, ExpandLayout, TransparentPushButton, TransparentToolButton, ScrollArea, \
    PushSettingCard, PlainTextEdit, MessageBox, IndeterminateProgressRing, ProgressRing, FluentIconBase, SettingCard, \
    IndeterminateProgressBar

from PyMyMethod import FileControl, Regedit
# from PyMyMethod.ScreenControl import ScreenControl


class CardsWidget(SmoothScrollArea):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        # self.sysCardGroup = None
        # self.switchCard = None
        # self.linkCard = None
        # self.languageCard = None
        # self.languageOption = None
        # self.kk = None
        # self.editCard = None
        # self.addCard = None
        # self.scrollWidget = None
        # self.expandLayout = None
        # self.filePath = None
        # self.message = None
        self.fc = FileControl()
        self.Regedit = Regedit()
        # self.ScreenControl = ScreenControl()
        self.lpData = [
            '绫地宁宁', '因幡爱瑠', '椎叶䌷', '亚托莉', ' 朝武芳乃', '丛雨', '常陆茉子', '上坂茅羽耶', '矢来美羽', '在原七海',
            '三司绫濑', '式部茉优', '二条院羽月', '和泉妃爱', '常盘华乃', '锦明日海', '镰仓诗樱', '结城明日奈', '小鸟游六花',
            '御坂美琴', '佐天泪子', '后藤一里', '山田凉', '伊地知虹夏', '喜多郁代'
        ]

        self.initWindow()
        self.initCard()
        self.connectSignalSlots()
        # self.initStyle()
        self.setObjectName(text.replace(' ', '_'))

    # --------------------------------------------------------------------------
    def initWindow(self):
        self.scrollWidget = QWidget()
        self.setViewportMargins(20, 20, 20, 20)
        self.vLayout = VBoxLayout(self.scrollWidget)
        self.vLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)

        self.sysCardGroup = SettingCardGroup("系统工具", self.scrollWidget)
        self.screenCardGroup = SettingCardGroup('屏幕工具', self.scrollWidget)
        self.lpCardGroup = SettingCardGroup('SELECT', self.screenCardGroup)
        self.vLayout.addWidget(self.sysCardGroup)

    def initCard(self):
        # sysCard
        self.switchCard = SwitchSettingCard(
            FluentIcon.WIFI,
            "WIFI",
            "连接wifi网络",
            ConfigItem('sys', 'wifi', False, BoolValidator()),
            self
        )
        self.switchCard.switchButton.setText('关')
        self.switchCard.setIconSize(24, 24)
        self.linkCard = HyperlinkCard(
            'https://www.github.com/mikuas',
            'GitHub', FluentIcon.GITHUB,
            'GitHub',
            'GitHub主页',
            self
        )
        self.linkCard.setIconSize(24, 24)
        self.kk = PrimaryPushSettingCard(
            "Help",
            FluentIcon.BASKETBALL,
            "Call CXK",
            '唱 跳 rap 打篮球',
            self
        )
        self.kk.setIconSize(24, 24)
        self.languageOption = OptionsConfigItem(
            'language',
            'language',
            "跟随系统设置",
            OptionsValidator(['跟随系统设置', '简体中文', '繁体中文', 'English', '日本語', '한국어'])
        )
        self.languageCard = ComboBoxSettingCard(
            self.languageOption,
            FluentIcon.LANGUAGE,
            "语言",
            '设置全局语言',
            ['跟随系统设置', '简体中文', '繁体中文', 'English', '日本語', '한국어'],
            self
        )
        self.languageCard.setIconSize(24, 24)
        # add card to cardGroup
        self.sysCardGroup.addSettingCards([self.switchCard, self.linkCard, self.languageCard, self.kk])
        # -------------------------------------------------
        self.editCard = EditCardWidget(
            FluentIcon.UPDATE,
            "更新",
            '设置Windows最大暂停更新天数',
            EditableComboBox,
            ['100', '500', '1000', '36500'],
            PrimaryToolButton,
            rightText='确定',
            parent=self
        )
        self.vLayout.addWidget(self.editCard)
        # -----------------------------------------
        self.addCard = ButtonCard(
            FluentIcon.SPEED_HIGH,
            "开机启动项",
            "设置开机启动项",
            PushButton,
            FluentIcon.FOLDER,
            '选择文件路径',
            PrimaryPushButton,
            '确定',
            self
        )
        self.vLayout.addWidget(self.addCard)
        # ----------------------------------------
        self.reNameCard = EditCardWidget(
            FluentIcon.FOLDER,
            '重命名',
            '根据选择的后缀名重命名文件,多个后缀名用空格隔开',
            EditableComboBox,
            ['jpg', 'png', 'gif', 'mp4', 'flac', 'ogg'],
            PrimaryToolButton,
            rightText='确定',
            parent=self
        )
        self.format = ComboBox(self)
        self.format.addItems(['纯数字命名(从0开始)', '纯英文命名(随机)'])
        self.selectDir = PushButton('选择文件目录', self)
        self.selectDir.setIcon(Icon(FluentIcon.FOLDER))
        self.reNameCard.hBoxLayout.insertWidget(4, self.selectDir, 0, Qt.AlignRight)
        self.reNameCard.hBoxLayout.insertWidget(3, self.format, 0, Qt.AlignRight)

        self.vLayout.addWidget(self.reNameCard)
        # ----------------------------------------------
        self.vLayout.addWidget(self.screenCardGroup)
        # screenCard
        self.screenCard = PrimaryPushSettingCard(
            '识别',
            FluentIcon.CLIPPING_TOOL,
            '捕获屏幕',
            '识别屏幕文字',
            self
        )
        self.textEdit = PlainTextEdit()
        self.vLayout.addWidget(self.textEdit)
        self.textEdit.hide()
        self.textEdit.setStyleSheet('font-size: 24px')
        self.screenCardGroup.addSettingCards([self.screenCard])
        # -----------------------------------------------------
        # lpCard
        self.vLayout.addWidget(self.lpCardGroup)
        self.l1 = EditComboBoxSettingCard(
            OptionsConfigItem(
                'lp',
                'l1',
                '',
                OptionsValidator(self.lpData)
            ),
            FluentIcon.HEART,
            'Girl',
            'Select you GirlFriend',
            self.lpData,
            self
        )
        self.l1.comboBox.setPlaceholderText('No Select')
        self.l1.comboBox.setCurrentIndex(-1)
        self.lpCardGroup.addSettingCards([self.l1])

    def initStyle(self, theme="LIGHT_CardWidget"):
        self.setStyleSheet(self.fc.readJsonFiles(f'./data/styles/{theme}.qss'))

    # def applyStyle(self, theme):
    #     if theme == Theme.DARK:
    #         theme = 'DARK_CardWidget'
    #     else:
    #         theme = 'LIGHT_CardWidget'
    #     self.initStyle(theme)

    def connectSignalSlots(self):
        qconfig.themeChanged.connect(lambda theme: None)#self.applyStyle(theme))
        self.switchCard.checkedChanged.connect(
            lambda b: (
                InfoBar.success(
                    'WIFI',
                    "已开启WIFI网络😊" if b else "已关闭WIFI网络😰",
                    isClosable=False,
                    duration=2000,
                    position=InfoBarPosition.TOP,
                    parent=self
                ),
                self.switchCard.switchButton.setText('开') if b else self.switchCard.switchButton.setText('关')
            )
        )
        self.languageOption.valueChanged.connect(
            lambda: InfoBar.success(
                '',
                '重启程序后生效',
                isClosable=False,
                duration=2500,
                position=InfoBarPosition.TOP,
                parent=self
            )
        )
        self.kk.clicked.connect(self.showKK)
        self.editCard.rightButton.clicked.connect(
            lambda: (
                Regedit().setWindowsUpdateDays(
                    int(self.editCard.comBox.text())
                ),
                TeachingTip.create(
                    self.editCard.rightButton,
                    "暂停天数",
                    f'成功设置最大暂停天数{self.editCard.comBox.text()}天🥰',
                    InfoBarIcon.SUCCESS,
                    isClosable=False,
                    duration=1500,
                    parent=self
                )
            )
        )
        self.addCard.rightButton_.clicked.connect(
            lambda: (
                self.updateFilePath(self.fc.getFilePathQT()),
                InfoBar.info(
                    '',
                    f'选择的目录是{self.filePath}',
                    position=InfoBarPosition.TOP,
                    duration=3000,
                    isClosable=False,
                    parent=self
                )
            )
        )
        self.addCard.rightButton__.clicked.connect(
            lambda: (
                self.Regedit.addAutoBoot(self.filePath.split('/')[-1].split('.')[0], self.filePath),
                InfoBar.info(
                    "",
                    f"成功添加{self.filePath}" if self.filePath else '添加失败,请选择正确的文件路径',
                    position=InfoBarPosition.TOP,
                    duration=2500,
                    parent=self
                )
            )
        )
        self.selectDir.clicked.connect(
            lambda: (
                self.updateFilePath(self.fc.getDirPathQT()),
                InfoBar.info(
                    '',
                    f'选择的目录是{self.filePath}',
                    position=InfoBarPosition.TOP,
                    duration=3000,
                    isClosable=False,
                    parent=self
                )
            )
        )
        self.reNameCard.rightButton.clicked.connect(
            lambda: (
                self.fc.fileReName(
                    self.filePath,
                    self.reNameCard.comBox.text().split(' '),
                    True if self.format.text() == '纯数字命名(从0开始)' else False
                ),
                InfoBar.success(
                    '',
                    '运行完成',
                    isClosable=False,
                    duration=2500,
                    position=InfoBarPosition.TOP,
                    parent=self
                )
            )
        )
        # self.screenCard.button.clicked.connect(
        #     lambda: (
        #         self.showMessage(),
        #         threading.Thread(
        #             target=lambda: (
        #                 self.textEdit.setPlainText(self.fc.getScreenFullText()),
        #                 self.textEdit.show(),
        #                 self.message.yesButton.show(),
        #             )
        #         ).start()
        #     )
        # )

    def showKK(self):
        view = FlyoutView(
            "蔡徐坤",
            '唱跳rap打篮球🏀',
            image='./data/images/icon/cxk.jpg',
            parent=self.kk.button
        )
        view.imageLabel.setFixedSize(300, 300)
        view.titleLabel.setStyleSheet('color: red')
        w = Flyout.make(view, self.kk.button, aniType=FlyoutAnimationType.SLIDE_LEFT)
        view.closed.connect(w.close)

    def showMessage(self):
        self.message = MessageBox('', '脚本将在5秒后开始运行,请准备好要截取的区域...', self)
        self.message.yesButton.hide(),
        self.message.yesButton.setText('识别完成')
        self.message.cancelButton.hide()
        self.ring = IndeterminateProgressBar(self)
        self.message.textLayout.addWidget(self.ring, Qt.AlignmentFlag.AlignVCenter)
        self.message.show()

    def updateFilePath(self, path):
        self.filePath = path

    def resizeEvent(self, event):
        self.scrollWidget.resize(self.width(), self.height())
        pass


# 卡片
class ButtonCard(CardWidget):

    def __init__(self, lefiIcon, title, content, button, buttonIcon=None, buttonText='', rightButton=None,
                 rightText=None, parent=None):
        super().__init__(parent)
        self.hBoxLayout = QHBoxLayout(self)
        self.vBoxLayout = QVBoxLayout()
        self.setFixedHeight(80)

        self.leftIcon = IconWidget(lefiIcon)
        self.titleLabel = BodyLabel(title)
        self.contentLabel = CaptionLabel(content)
        self.rightButton_ = button(self)
        self.rightButton_.setText(buttonText)
        if buttonIcon:
            self.rightButton_.setIcon(Icon(buttonIcon))
        self.rightButton__ = rightButton(self)
        if rightText:
            self.rightButton__.setText(rightText)

        self.leftIcon.setFixedSize(24, 24)
        self.contentLabel.setTextColor("black", 'white')

        self.hBoxLayout.setContentsMargins(20, 11, 11, 11)
        self.hBoxLayout.setSpacing(15)
        self.hBoxLayout.addWidget(self.leftIcon)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.addWidget(self.titleLabel, 0, Qt.AlignVCenter)
        self.vBoxLayout.addWidget(self.contentLabel, 0, Qt.AlignVCenter)
        self.vBoxLayout.setAlignment(Qt.AlignVCenter)

        self.hBoxLayout.addLayout(self.vBoxLayout)

        self.hBoxLayout.addStretch(1)
        self.hBoxLayout.addWidget(self.rightButton_, 0, Qt.AlignRight)
        self.hBoxLayout.addWidget(self.rightButton__, 0, Qt.AlignRight)


class EditCardWidget(CardWidget):
    def __init__(self, lefiIcon, title, content, combox=None, items=None, button=None, buttonIcon=None, rightText='',
                 parent=None):
        super().__init__(parent)
        self.setFixedHeight(75)
        self.hBoxLayout = QHBoxLayout(self)
        self.vBoxLayout = QVBoxLayout()

        self.leftIcon = IconWidget(lefiIcon)
        self.titleLabel = BodyLabel(title)
        self.contentLabel = CaptionLabel(content)
        self.comBox = combox()
        self.comBox.addItems(items)

        self.rightButton = button()
        self.rightButton.setText(rightText)
        if buttonIcon:
            self.rightButton.setIcon(Icon(buttonIcon))

        self.leftIcon.setFixedSize(24, 24)
        self.contentLabel.setTextColor("black", 'white')
        self.comBox.setFixedWidth(120)

        self.hBoxLayout.setContentsMargins(20, 11, 11, 11)
        self.hBoxLayout.setSpacing(15)
        self.hBoxLayout.addWidget(self.leftIcon)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.addWidget(self.titleLabel, 0, Qt.AlignVCenter)
        self.vBoxLayout.addWidget(self.contentLabel, 0, Qt.AlignVCenter)
        self.vBoxLayout.setAlignment(Qt.AlignVCenter)

        self.hBoxLayout.addLayout(self.vBoxLayout)

        self.hBoxLayout.addStretch(1)
        self.hBoxLayout.addWidget(self.comBox, 0, Qt.AlignRight)
        self.hBoxLayout.addWidget(self.rightButton, 0, Qt.AlignRight)


class EditComboBoxSettingCard(SettingCard):
    """ Setting card with a edit combo box """
    def __init__(self, configItem: OptionsConfigItem, icon: Union[str, QIcon, FluentIconBase], title, content=None,
                 texts=None, parent=None):
        super().__init__(icon, title, content, parent)
        self.configItem = configItem
        self.comboBox = EditableComboBox(self)
        self.hBoxLayout.addWidget(self.comboBox, 0, Qt.AlignRight)
        self.hBoxLayout.addSpacing(16)

        self.optionToText = {o: t for o, t in zip(configItem.options, texts)}
        for text, option in zip(texts, configItem.options):
            self.comboBox.addItem(text, userData=option)

        self.comboBox.setCurrentText(self.optionToText[qconfig.get(configItem)])
        self.comboBox.currentIndexChanged.connect(self._onCurrentIndexChanged)
        configItem.valueChanged.connect(self.setValue)

    def _onCurrentIndexChanged(self, index: int):

        qconfig.set(self.configItem, self.comboBox.itemData(index))

    def setValue(self, value):
        if value not in self.optionToText:
            return

        self.comboBox.setCurrentText(self.optionToText[value])
        qconfig.set(self.configItem, value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CardsWidget("CARD")
    window.resize(1000, 650)
    window.show()
    sys.exit(app.exec())
