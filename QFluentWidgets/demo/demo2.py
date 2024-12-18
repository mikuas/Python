import sys

from PySide6.QtWidgets import QApplication, QWidget
from qfluentwidgets import setTheme, Theme, FluentIcon, TitleLabel, FluentWindow, Action

from QtFluentWidgets.FluentWidgetModule.FluentWidgets import WinFluentIcon
from QtFluentWidgets.FluentWidgetModule.FluentWidgets.components import (
    PivotNav, SegmentedNav, SegmentedToolNav, SegmentedToggleToolNav, SystemTrayIcon, LabelBarWidget, Icon
)

from demo3 import CardWidget, ExpandCardWidget, ComboBoxCardWidget, MenuWidget


class Window(FluentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(Icon(WinFluentIcon.RADIUS_WIN_11_LOG))
        self.initWindow()
        self.initWidget()
        self.initNavigation()
        self.addNav()
        SystemTrayIcon(self).setIcon(
            self.windowIcon()
        ).addMenu(
            Action(FluentIcon.EDIT, "Exit", triggered=QApplication.exit)
        ).show()

    def initWindow(self):
        self.resize(1200, 700)
        desktop = QApplication.primaryScreen().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

    def initNavigation(self):
        self.navigationInterface.setExpandWidth(250)
        self.navigationInterface.setMinimumExpandWidth(1500)
        self.addSubInterface(
            self.pivotNav,
            FluentIcon.HOME,
            '导航栏'
        )
        self.addSubInterface(
            self.segmentedNav,
            FluentIcon.CARE_DOWN_SOLID,
            "卡片"
        )

    def initWidget(self):
        self.pivotNav = PivotNav("PIVOT_NAV", self).setNavWidth(500)
        self.labelBar = LabelBarWidget(self)

        self.segmentedNav = SegmentedNav("SEGMENTED_NAV", self)
        self.segmentedNav.addItems(
            ["CARD", "EXPAND_CARD", "COMBO_BOX_CARD", "MENU_WIDGET"],
            ["按钮卡片", "展开卡片", "下拉卡片", "Menu"],
            [CardWidget(), ExpandCardWidget(self), ComboBoxCardWidget(), MenuWidget()]
        ).setCurrentItem('CARD')

        self.segmentedToolNav = SegmentedToolNav("SEGMENTED_TOOL_NAV", self)
        self.segmentedToggleToolNav = SegmentedToggleToolNav("SEGMENTED_TOGGLE_TOOL_NAV", self)

    def addNav(self):
        self.pivotNav.addItems(
            ["TAB_LABEL_NAV", "SEGMENTED_TOOL_NAV", "SEGMENTED_TOGGLE_TOOL_NAV"],
            ["标签页组件", "分段工具导航", "分段可选中导航"],
            [self.labelBar, self.segmentedToolNav, self.segmentedToggleToolNav]
        ).setCurrentItem("TAB_LABEL_NAV")
        self.labelBar.addTabWidgets(
            ['BAR_HOME', 'BAR_MUSIC', "BAR_VIDEO"],
            ['HOME', 'MUSIC', "VIDEO"],
            [FluentIcon.HOME, FluentIcon.MUSIC, FluentIcon.VIDEO],
            [TitleLabel("HOME_INTERFACE", self), TitleLabel("MUSIC_INTERFACE", self), TitleLabel("VIDEO_INTERFACE", self)]
        ).hideCloseButton().hideAddButton()
        self.segmentedToolNav.addToolItems(
            ["SEG_HOME", "SEG_MUSIC", "SEG_VIDEO"],
            [FluentIcon.HOME, FluentIcon.MUSIC, FluentIcon.VIDEO],
            [TitleLabel("HOME_INTERFACE", self), TitleLabel("MUSIC_INTERFACE", self), TitleLabel("VIDEO_INTERFACE", self)]
        ).setCurrentItem("SEG_HOME")
        self.segmentedToggleToolNav.addToolItems(
            ["SEG_HOME", "SEG_MUSIC", "SEG_VIDEO"],
            [FluentIcon.HOME, FluentIcon.MUSIC, FluentIcon.VIDEO],
            [TitleLabel("HOME_INTERFACE", self), TitleLabel("MUSIC_INTERFACE", self), TitleLabel("VIDEO_INTERFACE", self)]
        ).setCurrentItem("SEG_HOME")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    #  启用云母特效
    window.setMicaEffectEnabled(True)
    setTheme(Theme.AUTO)
    window.show()
    sys.exit(app.exec())