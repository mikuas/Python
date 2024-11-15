import sys

from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QWidget

from qfluentwidgets import SettingCardGroup, VBoxLayout, SmoothScrollArea, FluentIcon, setTheme, Theme, InfoBarIcon
from QFluentWidgets.FluentWidget.FluentCardWidget.ButtonCard.ButtonCard import ButtonCard, PrimaryButtonCard, \
    TransparentButtonCard, ToolButtonCard, PrimaryToolButtonCard, TransparentToolButtonCard, ComboBoxCard, \
    EditComboBoxCard, SwitchButtonCard, DropDownCard, PrimaryDropDownCard, TransparentDropDownCard, DropDownToolCard, \
    TransparentDropDownToolCard, PrimaryDropDownToolCard, PrimarySplitCard, SplitCard, SplitToolCard, \
    PrimarySplitToolCard, HyperLinkCard, ExpandGroupCard

from PyMyMethod.Method import FileControl

from QFluentWidgets.FluentWidget.FluentCardWidget.CustomCardWidget import ExpandButtonCard as eb

class Demo(SmoothScrollArea):
    def __init__(self):
        super().__init__()
        self.fc = FileControl()
        self.girls = dict(self.fc.readJsonFiles(r"C:\Projects\Items\Python\QT\QFluentWidget\Test\FlunetWindow\config\data.json"))['girlName']

        self.initWindow()
        self.initCard()
        self.initCardGroup()
        self.initLayout()

    def initWindow(self):
        self.scrollWidget = QWidget()
        self.vLayout = VBoxLayout(self.scrollWidget)
        self.vLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)
        self.resize(1200, 700)
        desktop = QApplication.primaryScreen().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

    def initLayout(self):
        self.vLayout.addWidget(self.buttonCardGroup)
        self.vLayout.addWidget(self.toolButtonCardGroup)
        self.vLayout.addWidget(self.expandCardGroup)
        self.vLayout.addWidget(self.comboBoxCardGroup)
        self.vLayout.addWidget(self.dropCardGroup)
        self.vLayout.addWidget(self.splitCardGroup)

    def initCardGroup(self):
        self.buttonCardGroup = SettingCardGroup('标准按钮卡片组', self)
        self.toolButtonCardGroup = SettingCardGroup('工具按钮卡片组', self)
        self.comboBoxCardGroup = SettingCardGroup('下拉框卡片', self)
        self.dropCardGroup = SettingCardGroup('下拉按钮卡片', self)
        self.splitCardGroup = SettingCardGroup('拆分按钮', self)


        self.buttonCardGroup.addSettingCards([
            self.buttonCard,
            self.primaryButtonCard,
            self.transparentButtonCard,
            self.statusButtonCard,
            self.linkButtonCard
        ])

        self.toolButtonCardGroup.addSettingCards([
            self.toolButtonCard,
            self.primaryToolButtonCard,
            self.transparentToolButtonCard
        ])

        self.comboBoxCardGroup.addSettingCards([
            self.comboBoxCard,
            self.editComboBoxCard
        ])

        self.dropCardGroup.addSettingCards([
            self.dropCard,
            self.primaryDropCard,
            self.tranDropCard,
            self.toolDropCard,
            self.priToolDropCard,
            self.tranToolDropCard
        ])

        self.splitCardGroup.addSettingCards([
            self.splitCard,
            self.priSplitCard,
            self.splitToolCard,
            self.priSplitToolCard
        ])

    def initCard(self):
        self.buttonCard = ButtonCard(
            FluentIcon.GITHUB,
            '标准按钮',
            'Content',
            '确定',
            parent=self
        )
        self.primaryButtonCard = PrimaryButtonCard(
            FluentIcon.WIFI,
            '主题色按钮',
            'Content',
            '确定',
            FluentIcon.CLOUD,
            self
        )
        self.transparentButtonCard = TransparentButtonCard(
            FluentIcon.POWER_BUTTON,
            '透明按钮',
            'Content',
            buttonIcon=InfoBarIcon.SUCCESS,
            parent=self
        )
        self.statusButtonCard = SwitchButtonCard(
            FluentIcon.WIFI,
            '状态开关按钮',
            'Content',
            False,
            self
        )
        self.linkButtonCard = HyperLinkCard(
            'https://www.bilibili.com',
            FluentIcon.VIDEO,
            '超链接按钮',
            'Content',
            '确定',
            FluentIcon.MORE,
            self
        )
        #####################################################
        self.toolButtonCard = ToolButtonCard(
            FluentIcon.MAIL,
            '标准工具按钮',
            'Content',
            FluentIcon.ALBUM,
            parent=self
        )
        self.primaryToolButtonCard = PrimaryToolButtonCard(
            FluentIcon.CLOUD,
            '主题色工具按钮',
            'Content',
            FluentIcon.ADD,
            self
        )
        self.transparentToolButtonCard = TransparentToolButtonCard(
            FluentIcon.DELETE,
            '透明工具按钮',
            'Content',
            FluentIcon.ADD,
            self
        )
        #########################################
        self.comboBoxCard = ComboBoxCard(
            FluentIcon.ADD_TO,
            '下拉框',
            'Content',
            self.girls,
            True,
            'Selected',
            self
        )
        self.editComboBoxCard = EditComboBoxCard(
            FluentIcon.CAR,
            '可编辑下拉框',
            '',
            self.girls,
            True,
            'Selected',
            self
        )
        self.editComboBoxCard.titleLabel.setContentsMargins(0, 15, 0, 0)
        #########################################
        self.dropCard = DropDownCard(
            FluentIcon.ALBUM,
            '下拉按钮',
            'Content',
            '',
            FluentIcon.MORE,
            ['SEND', 'ADD', 'DELETE'],
            [FluentIcon.SEND, FluentIcon.ADD, FluentIcon.DELETE],
            [lambda: print("SEND"), lambda: print("ADD"), lambda: print("DELETE")],
            self
        )
        self.primaryDropCard = PrimaryDropDownCard(
            FluentIcon.INFO,
            '主题色下拉按钮',
            'Content',
            '确定',
            None,
            ['ADD', 'SEND', 'DELETE'],
            [FluentIcon.ADD, FluentIcon.SEND, FluentIcon.BASKETBALL],
            [lambda: print('1'), lambda: print('2'), lambda: print('3')],
            self
        )
        self.tranDropCard = TransparentDropDownCard(
            FluentIcon.CAR,
            '透明下拉按钮',
            'Content',
            '确定',
            FluentIcon.MORE,
            ["SEND", "ADD", "DELETE"],
            [FluentIcon.SEND, FluentIcon.ADD, FluentIcon.DELETE],
            [lambda: print('SEND'), lambda: print('ADD'), lambda: print('DELETE')],
            self
        )
        self.toolDropCard = DropDownToolCard(
            FluentIcon.ASTERISK,
            '下拉工具按钮',
            'Content',
            '更多',
            # None,
            # FluentIcon.MORE,
            ["SEND", "ADD", "DELETE"],
            [FluentIcon.SEND, FluentIcon.ADD, FluentIcon.DELETE],
            [lambda: print('SEND'), lambda: print('ADD'), lambda: print('DELETE')],
            self
        )
        self.priToolDropCard = PrimaryDropDownToolCard(
            FluentIcon.BLUETOOTH,
            '主题色下拉工具按钮',
            'Content',
            FluentIcon.ADD,
            ["SEND", "ADD", "DELETE"],
            [FluentIcon.SEND, FluentIcon.ADD, FluentIcon.DELETE],
            [lambda: print('SEND'), lambda: print('ADD'), lambda: print('DELETE')],
            self
        )
        self.tranToolDropCard = TransparentDropDownToolCard(
            FluentIcon.CHAT,
            '透明下拉工具按钮',
            'Content',
            InfoBarIcon.INFORMATION,
            ["SEND", "ADD", "DELETE"],
            [FluentIcon.SEND, FluentIcon.ADD, FluentIcon.DELETE],
            [lambda: print('SEND'), lambda: print('ADD'), lambda: print('DELETE')],
            self
        )
        ################################################
        self.splitCard = SplitCard(
            FluentIcon.HOME,
            '拆分按钮',
            'Content',
            '确定',
            FluentIcon.SEND,
            ['添加', '删除', '查找'],
            [FluentIcon.ADD, FluentIcon.DELETE, FluentIcon.SEARCH],
            [lambda: print('添加'), lambda: print('删除'), lambda: print('查找')],
            self
        )
        self.priSplitCard = PrimarySplitCard(
            FluentIcon.BLUETOOTH,
            '主题色拆分按钮',
            'Content',
            '更多',
            FluentIcon.MORE,
            ["SEND", "ADD", "DELETE"],
            [FluentIcon.SEND, FluentIcon.ADD, FluentIcon.DELETE],
            [lambda: print('SEND'), lambda: print('ADD'), lambda: print('DELETE')],
            self
        )
        self.splitToolCard = SplitToolCard(
            FluentIcon.HOME,
            '拆分工具按钮',
            'Content',
            FluentIcon.MORE,
            ["SEND", "ADD", "DELETE"],
            [FluentIcon.SEND, FluentIcon.ADD, FluentIcon.DELETE],
            [lambda: print('SEND'), lambda: print('ADD'), lambda: print('DELETE')],
            self
        )
        self.priSplitToolCard = PrimarySplitToolCard(
            FluentIcon.GITHUB,
            '主题色拆分工具按钮',
            'Content',
            # '确定',
            FluentIcon.SEND,
            ["SEND", "ADD", "DELETE"],
            [FluentIcon.SEND, FluentIcon.ADD, FluentIcon.DELETE],
            [lambda: print('SEND'), lambda: print('ADD'), lambda: print('DELETE')],
            self
        )
        ###########################################################
        self.expandCardGroup = ExpandGroupCard(
            FluentIcon.POWER_BUTTON, '展开卡片', 'Content', self
        )
        self.expandCardGroup.addGroupWidgets([
            ButtonCard(
                FluentIcon.HOME,
                'ONE',
                "Content",
                None,
                FluentIcon.MORE,
                self
            ),
            ToolButtonCard(
                FluentIcon.HOME,
                "TWO",
                'Content',
                FluentIcon.MORE,
                self
            )
        ])
        self.expandCardGroup.addPrimaryButtonCard(
            '标题',
            FluentIcon.HOME,
            '确定'
        )
        self.expandCardGroup.addGroupWidget(
            SplitCard(
                FluentIcon.HOME,
                'Split',
                'Content',
                '确定',
                FluentIcon.MORE,
                ["复制", '粘贴', '撤销'],
                None,
                None,
                self
            )
        )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Demo()
    setTheme(Theme.DARK)
    window.show()
    sys.exit(app.exec())