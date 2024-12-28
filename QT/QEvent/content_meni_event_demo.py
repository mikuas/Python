import sys

from PySide6.QtWidgets import QWidget, QApplication

from FluentWidgets import AcrylicRoundMenu
from qfluentwidgets.components.material import AcrylicMenu

from FluentWidgets import WinFluentIcon


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.menu = AcrylicRoundMenu(self)
        self.menu.menu.insertSeparator(
            self.menu.addItems(
                [WinFluentIcon.HOME, WinFluentIcon.WIN_11_LOG, WinFluentIcon.WIFI],
                ['Home', 'Windows', 'Wifi']
            )[0]
        )
        self.menu.addSeparator()
        self.menu.addItem(WinFluentIcon.XIN_HAO, "XinHao")


    def contextMenuEvent(self, event):
        super().contextMenuEvent(event)
        self.menu.exec(event.globalPos())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec())