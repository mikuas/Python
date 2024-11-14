import sys

from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QWidget

from qfluentwidgets import SettingCardGroup, VBoxLayout, SmoothScrollArea, FluentIcon, setTheme, Theme, InfoBarIcon

from QFluentWidgets.FluentWidget.FluentCardWidget.ButtonCard.ButtonCard import PushButtonCard, PrimaryButtonCard, \
    TransparentButtonCard, ToolButtonCard, PrimaryToolButtonCard, TransparentToolButtonCard, ComboBoxCard, \
    EditComboBoxCard, SwitchButtonCard

from PyMyMethod.Method import FileControl


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
        self.vLayout.addWidget(self.comboBoxCardGroup)

    def initCardGroup(self):
        self.buttonCardGroup = SettingCardGroup('标准按钮卡片组', self)
        self.toolButtonCardGroup = SettingCardGroup('工具按钮卡片组', self)
        self.comboBoxCardGroup = SettingCardGroup('下拉框卡片', self)

        self.buttonCardGroup.addSettingCards([
            self.buttonCard,
            self.primaryButtonCard,
            self.transparentButtonCard,
            self.statusButtonCard
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

    def initCard(self):
        self.buttonCard = PushButtonCard(
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
        #####################################################
        self.toolButtonCard = ToolButtonCard(
            FluentIcon.MAIL,
            '标准工具按钮',
            'Content',
            '确定',
            parent=self
        )
        self.primaryToolButtonCard = PrimaryToolButtonCard(
            FluentIcon.CLOUD,
            '主题色工具按钮',
            'Content',
            buttonIcon=FluentIcon.ADD,
            parent=self
        )
        self.transparentToolButtonCard = TransparentToolButtonCard(
            FluentIcon.DELETE,
            '透明工具按钮',
            'Content',
            '确定',
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Demo()
    setTheme(Theme.DARK)
    window.show()
    sys.exit(app.exec())