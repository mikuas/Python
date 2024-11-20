import sys

from PySide6.QtWidgets import QWidget, QApplication, QListWidgetItem, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import Qt
from qfluentwidgets import setTheme, Theme, FluentIcon

from QFluentWidgets.FluentWidgetModule.FluentWidgets import PrimaryButtonCard, ToolButtonCard, ExpandGroupCard
from QFluentWidgets.FluentWidgetModule.FluentWidgets.customwidgets import CustomFluentIcon as CFI, ListWidget
from QFluentWidgets.FluentWidgetModule.FluentWidgets.widgets import ButtonCard
from QFluentWidgets.FluentWidgetModule.FluentWidgets.customwidgets import OneWayScrollWidget

class Demo(OneWayScrollWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 700)
        self.listWidget = ListWidget(self)

        self.listWidget.addIconItem(
            [CFI.C_SETTING, CFI.DOWNLOAD_FOLDER, FluentIcon.HOME, CFI.EXPLORER],
            ["SETTING", "FOLDER", "HELP", "EXPLORER"]
        )
        # 默认情况下，右键单击某个列表项时不会更新该列的选中状态，如需立即选中可调用下述方法
        self.listWidget.setSelectRightClickedRow(True)
        # 连接信号插槽
        self.listWidget.clicked.connect(
            lambda value: print(self.listWidget.model().data(value))
        )
        # 取消焦点
        self.listWidget.setFocusPolicy(Qt.NoFocus)
        self.listWidget.setFixedSize(self.width(), self.height() / 2)

        self.expand = ExpandGroupCard(CFI.WIN_LOG_, "光翼--展开", "", self)
        self.expand.addGroupWidgets([
            ButtonCard(
                CFI.LOW_POWER,
                "CUSTOM",
                "EXPLORER",
                '确定',
                parent=self
            ),
            PrimaryButtonCard(
                CFI.STORE,
                "FLUENT",
                "HOME",
                '确定',
                parent=self
            ),
            ButtonCard(
                CFI.DOWNLOAD_FOLDER,
                "DOWNLOAD",
                "FOLDER",
                '确定',
                parent=self
            ),
            PrimaryButtonCard(
                CFI.XIN_HAO,
                "DOWNLOAD",
                "FOLDER",
                '确定',
                parent=self
            ),
            ButtonCard(
                CFI.TWITTER,
                "DOWNLOAD",
                "FOLDER",
                '确定',
                parent=self
            ),
            PrimaryButtonCard(
                CFI.NOTEPAD,
                "DOWNLOAD",
                "FOLDER",
                '确定',
                parent=self
            ),
            ButtonCard(
                CFI.XIAN_JI,
                "DOWNLOAD",
                "FOLDER",
                '确定',
                parent=self
            ),
            PrimaryButtonCard(
                CFI.XBOX,
                "DOWNLOAD",
                "FOLDER",
                '确定',
                parent=self
            ),
            ButtonCard(
                CFI.EXPLORER,
                "DOWNLOAD",
                "FOLDER",
                '确定',
                parent=self
            ),
            PrimaryButtonCard(
                CFI.TERMINAL,
                "DOWNLOAD",
                "FOLDER",
                '确定',
                parent=self
            ),
            ButtonCard(
                CFI.REGEDIT,
                "DOWNLOAD",
                "FOLDER",
                '确定',
                parent=self
            ),
            PrimaryButtonCard(
                CFI.RI_LI,
                "DOWNLOAD",
                "FOLDER",
                '确定',
                parent=self
            )
            ])

        self.layout.addWidget(self.listWidget)
        self.layout.addWidget(self.expand)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Demo()
    setTheme(Theme.AUTO)
    w.show()
    sys.exit(app.exec())
