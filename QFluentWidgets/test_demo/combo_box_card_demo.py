import sys

from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication
from qfluentwidgets import FluentIcon, SettingCardGroup, setTheme, Theme, TitleLabel

from FluentWidgets import VerticalScrollWidget
from QtFluentWidgets.FluentWidgetModule.FluentWidgets import (
    ComboBoxCard, EditComboBoxCard,
    AcrylicComboBoxCard, AcrylicEditComboBoxCard,
    ColorSelectCard,
    ExpandGroupCard,
    OptionsCard,
    FolderListCard
)

class Demo(VerticalScrollWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 520)
        self.comboBoxCardGroup = SettingCardGroup("下拉框卡片", self)
        self.acrylicComboBoxCardGroup = SettingCardGroup("亚力克下拉框卡片", self)
        self.expandGroupCard = ExpandGroupCard(FluentIcon.MORE, 'ExpandGroupCard', '', self)
        self.optionCardGroup = SettingCardGroup("选项卡", self)
        self.initCard()
        self.initCardGroup()
        self.initLayout()

    def initCardGroup(self):
        self.comboBoxCardGroup.addSettingCards([
            self.comboBoxCard,
            self.editComboBoxCard
        ])
        self.acrylicComboBoxCardGroup.addSettingCards([
            self.acrylicComboBoxCard,
            self.editAcrylicComboBoxCard,
            self.colorSelectCard
        ])
        self.optionCardGroup.addSettingCards([
            self.folderListCard,
            self.optionsCard
        ])
        self.optionsCard.optionChanged.connect(
            lambda v: print(v.value)
        )

        self.expandGroupCard.addButtonCard('ButtonCard', FluentIcon.PALETTE, '确定')
        self.expandGroupCard.addPrimaryButtonCard("PrimaryButtonCard", FluentIcon.PLAY, '确定')
        self.expandGroupCard.addTransparentButtonCard("TransparentButtonCard", FluentIcon.GITHUB, '确定')
        self.expandGroupCard.addSliderCard('SliderCard', 0, 100, 24)
        self.expandGroupCard.addCustomWidget(
            TitleLabel("This is Custom Widget", self),
            alignment=Qt.AlignmentFlag.AlignHCenter
        ).addWidget(TitleLabel("This is Custom Widget", self))

    def initCard(self):
        self.comboBoxCard = ComboBoxCard(
            FluentIcon.HOME,
            'ComboBoxCard',
            '',
            ['白金之星', '绿色法皇', '银色战车']
        )
        self.editComboBoxCard = EditComboBoxCard(
            FluentIcon.FOLDER,
            'EditComboBoxCard',
            '',
            ['白金之星', '绿色法皇', '银色战车'],
            True,
            '请选择你的替身'
        )
        ########################
        self.acrylicComboBoxCard = AcrylicComboBoxCard(
            FluentIcon.MOVIE,
            'AcrylicComboBoxCard',
            '',
            ['白金之星', '绿色法皇', '银色战车']
        )
        self.editAcrylicComboBoxCard = AcrylicEditComboBoxCard(
            FluentIcon.GITHUB,
            'EditComboBoxCard',
            '',
            ['白金之星', '绿色法皇', '银色战车'],
            True,
            '请选择你的替身'
        )
        self.colorSelectCard = ColorSelectCard(
            'ColorSelectCard',
            '',
            self
        )
        self.colorSelectCard.setCardFixedHeight(70)
        self.folderListCard = FolderListCard(
            'FolderListCard',
            '',
            'E:\\',
            self
        )
        self.folderListCard.setFixedHeight(70)

        self.optionsCard = OptionsCard(
            FluentIcon.RETURN,
            'OptionsCard',
            '',
            ['Item1', 'Item2', 'Item3'],
            'Item 2',
            self
        )

    def initLayout(self):
        self.vBoxLayout.addWidgets([
            self.comboBoxCardGroup,
            self.acrylicComboBoxCardGroup,
            self.expandGroupCard,
            self.optionCardGroup
        ])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    setTheme(Theme.AUTO)
    demo.show()
    sys.exit(app.exec())