import sys

from PySide6.QtWidgets import QWidget, QApplication, QSystemTrayIcon, QHBoxLayout, QLabel
from PySide6.QtGui import QIcon
from qfluentwidgets import *


# 系统托盘
class SystemTrayIcon(QSystemTrayIcon):

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setIcon(parent.windowIcon())

        self.menu = SystemTrayMenu(parent=parent)
        self.menu.addActions([
            Action('🎤   唱'),
            Action('🕺   跳'),
            Action('🤘🏼   RAP'),
            Action('🎶   Music'),
            Action('🏀   篮球', triggered=self.ikun),
        ])
        self.setContextMenu(self.menu)

    def ikun(self):
        print("""巅峰产生虚伪的拥护，黄昏见证真正的使徒 🏀

                       ⠰⢷⢿⠄
                   ⠀⠀⠀⠀⠀⣼⣷⣄
                   ⠀⠀⣤⣿⣇⣿⣿⣧⣿⡄
                   ⢴⠾⠋⠀⠀⠻⣿⣷⣿⣿⡀
                   ⠀⢀⣿⣿⡿⢿⠈⣿
                   ⠀⠀⠀⢠⣿⡿⠁⠀⡊⠀⠙
                   ⠀⠀⠀⢿⣿⠀⠀⠹⣿
                   ⠀⠀⠀⠀⠹⣷⡀⠀⣿⡄
                   ⠀⠀⠀⠀⣀⣼⣿⠀⢈⣧
        """)


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.setLayout(QHBoxLayout())
        self.label = QLabel('Right-click system tray icon', self)
        self.layout().addWidget(self.label)

        self.resize(500, 500)
        self.setWindowIcon(Icon(FluentIcon.GITHUB))
        self.systemTrayIcon = SystemTrayIcon(self)
        self.systemTrayIcon.setToolTip('Ciallo～(∠・ω< )⌒☆')
        self.systemTrayIcon.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Demo()
    ex.show()
    sys.exit(app.exec())