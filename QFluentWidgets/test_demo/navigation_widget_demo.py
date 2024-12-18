import sys

from PySide6.QtWidgets import QWidget, QApplication, QMainWindow
from qfluentwidgets import TitleLabel, FluentIcon

from QtFluentWidgets.FluentWidgetModule.FluentWidgets import (
    PivotNav, SegmentedNav, SegmentedToolNav, SegmentedToggleToolNav
)


class Demo(PivotNav):
# class Demo(SegmentedNav):
# class Demo(SegmentedToolNav):
# class Demo(SegmentedToggleToolNav):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(800, 520)
        self.addSubInterface(
            "Item 1",
            "HOME",
            TitleLabel("HOME_INTERFACE", self)
        ).addSubInterface(
            "Item 2",
            "TOOL",
            TitleLabel("TOOL_INTERFACE", self)
        ).enableNavCenter().addNavigationSeparator(2).addSubInterface(
            "Item 3",
            "SETTING",
            TitleLabel("SETTING_INTERFACE", self)
        ).addSeparator()

        # self.addSubInterface(
        #     "Item 1",
        #     TitleLabel("HOME_INTERFACE", self),
        #     FluentIcon.HOME
        # ).addSubInterface(
        #     "Item 2",
        #     TitleLabel("TOOL_INTERFACE", self),
        #     FluentIcon.ERASE_TOOL
        # ).addSubInterface(
        #     "Item 3",
        #     TitleLabel("SETTING_INTERFACE", self),
        #     FluentIcon.SETTING
        # ).addSeparator()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Demo()
    window.show()
    sys.exit(app.exec())