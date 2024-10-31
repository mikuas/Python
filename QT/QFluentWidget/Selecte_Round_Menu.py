import sys

from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import QActionGroup

from qfluentwidgets import *


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.createTimeAction = Action(FluentIcon.CALENDAR, "创建日期", checkable=True)
        self.shootTimeAction = Action(FluentIcon.CAMERA, "拍摄日期", checkable=True)
        self.modifiedTimeAction = Action(FluentIcon.EDIT, "修改日期", checkable=True)
        self.nameAction = Action(FluentIcon.FONT, "名字", checkable=True)

        self.ascendAction = Action(FluentIcon.UP, "升序", checkable=True)
        self.descendAction = Action(FluentIcon.DOWN, "降序", checkable=True)

        # 将动作添加到动作组
        self.actionGroup1 = QActionGroup(self)
        self.actionGroup1.addAction(self.createTimeAction)
        self.actionGroup1.addAction(self.shootTimeAction)
        self.actionGroup1.addAction(self.modifiedTimeAction)
        self.actionGroup1.addAction(self.nameAction)

        self.actionGroup2 = QActionGroup(self)
        self.actionGroup2.addAction(self.ascendAction)
        self.actionGroup2.addAction(self.descendAction)

        # 选中动作
        self.shootTimeAction.setChecked(True)
        self.ascendAction.setChecked(True)

    def contextMenuEvent(self, e):
        menu = CheckableMenu(parent=self, indicatorType=MenuIndicatorType.RADIO)

        menu.addActions([
            self.createTimeAction, self.shootTimeAction,
            self.modifiedTimeAction, self.nameAction
        ])
        menu.addSeparator()
        menu.addActions([self.ascendAction, self.descendAction])

        menu.exec(e.globalPos(), aniType=MenuAnimationType.DROP_DOWN)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    sys.exit(app.exec())