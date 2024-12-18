import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from qfluentwidgets import FluentWindow, NavigationInterface, FluentIcon, setTheme, Theme, PopUpAniStackedWidget, \
    TitleLabel

from QtFluentWidgets.FluentWidgetModule.FluentWidgets import FluentWindow


class MicaEffect(FluentWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 520)
        qw = QWidget(self)
        qw.setObjectName('MicaEffect')
        TitleLabel("WORLD", qw)

        self.homeInterface = TitleLabel("HOME_INTERFACE", self)
        self.homeInterface.setObjectName("HOME_INTERFACE")
        self.settingInterface = TitleLabel("SETTINGS_INTERFACE", self)
        self.settingInterface.setObjectName("SETTINGS_INTERFACE")
        self.codeInterface = TitleLabel("CODE_INTERFACE", self)
        self.codeInterface.setObjectName("CODE_INTERFACE")

        self.addSubInterface(
            self.homeInterface,
            FluentIcon.HOME,
            'r1',
        )
        self.addSubInterface(
            self.settingInterface,
            FluentIcon.SETTING,
            'r2',
        )
        self.addSubInterface(
            self.codeInterface,
            FluentIcon.CODE,
            'r3',
        )
        self.addSubInterface(
            qw,
            FluentIcon.FONT,
            'f'
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MicaEffect()
    setTheme(Theme.AUTO)
    window.show()  # 确保显示窗口
    sys.exit(app.exec())
