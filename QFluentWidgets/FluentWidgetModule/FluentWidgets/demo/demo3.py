import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget, QApplication, QListWidgetItem, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import Qt
from qfluentwidgets import setTheme, Theme, FluentIcon

from QFluentWidgets.FluentWidgetModule.FluentWidgets import PrimaryButtonCard, ToolButtonCard, ExpandGroupCard
from QFluentWidgets.FluentWidgetModule.FluentWidgets.customwidgets import (
    WinPngFluentIcon as WPFI, ListWidget, WinSvgFluentIcon as WSFI
)
from QFluentWidgets.FluentWidgetModule.FluentWidgets.widgets import ButtonCard
from QFluentWidgets.FluentWidgetModule.FluentWidgets.customwidgets import OneWayScrollWidget

class Demo(OneWayScrollWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 700)
        self.listWidget = ListWidget(self)

        self.listWidget.addIconItem(
            [FluentIcon.SETTING, FluentIcon.FOLDER, FluentIcon.HELP, FluentIcon.EXPRESSIVE_INPUT_ENTRY],
            ["SETTING", "FOLDER", "HELP", "EXPLORER"],
            60
        ).setIconSize(QSize(28, 28))
        # 默认情况下，右键单击某个列表项时不会更新该列的选中状态，如需立即选中可调用下述方法
        self.listWidget.setSelectRightClickedRow(True)
        # 连接信号插槽
        self.listWidget.clicked.connect(
            lambda value: print(self.listWidget.model().data(value))
        )
        # 取消焦点
        self.listWidget.setFocusPolicy(Qt.NoFocus)
        self.listWidget.setFixedSize(self.width(), self.height() / 2)

        self.expand = ExpandGroupCard(WPFI.SETTING, "光翼--展开", "", self)
        self.expand.addGroupWidgets([
            ButtonCard(
                WPFI.COLOR_WIFI,
                "CUSTOM",
                "EXPLORER",
                '确定',
                parent=self
            ),
            PrimaryButtonCard(
                WPFI.MSF_STORE,
                "FLUENT",
                "HOME",
                '确定',
                parent=self
            ),
            ButtonCard(
                WPFI.MUSIC_FOLDER,
                "DOWNLOAD",
                "FOLDER",
                '确定',
                parent=self
            ),
            PrimaryButtonCard(
                WPFI.NO_NETWORK,
                "DOWNLOAD",
                "FOLDER",
                '确定',
                parent=self
            ),
            ButtonCard(
                WPFI.NOTEPAD,
                "DOWNLOAD",
                "FOLDER",
                '确定',
                parent=self
            ),
            PrimaryButtonCard(
                WPFI.PAINT,
                "DOWNLOAD",
                "FOLDER",
                '确定',
                parent=self
            ),
            ButtonCard(
                WPFI.PICTURE_FOLDER,
                "DOWNLOAD",
                "FOLDER",
                '确定',
                parent=self
            ),
            PrimaryButtonCard(
                WPFI.PLAY,
                "DOWNLOAD",
                "FOLDER",
                '确定',
                parent=self
            ),
            ButtonCard(
                WPFI.QUICK_SHARK,
                "DOWNLOAD",
                "FOLDER",
                '确定',
                parent=self
            ),
            PrimaryButtonCard(
                WPFI.RADIUS_WIN11_LOG,
                "DOWNLOAD",
                "FOLDER",
                '确定',
                parent=self
            ),
            ButtonCard(
                WPFI.REGEDIT,
                "DOWNLOAD",
                "FOLDER",
                '确定',
                parent=self
            ),
            PrimaryButtonCard(
                WSFI.FINISH,
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
