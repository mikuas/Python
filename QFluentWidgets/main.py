import sys

from PySide6.QtWidgets import QApplication
from qfluentwidgets import MSFluentWindow, FluentIcon, Icon

from ButtonWidget import ButtonWidget
from DateTimeWidget import DateTimeWidget
from DialogBoxPopWidget import DialogBoxPopWidget
from MediaWidget import MediaWidget
from MenuCommandBar import MenuCommandBar
from NavWidget import NavWidget
from ScrollWidget import ScrollWidget
from StatusInfoWidget import StatusInfoWidget
from TextWidget import TextWidget

class Window(MSFluentWindow):
    def __init__(self):
        super().__init__()
        self.buttonWidget = ButtonWidget('BUTTON', self)
        self.dateTimeWidget = DateTimeWidget('DATETIME', self)
        self.dialogBoxPopWidget = DialogBoxPopWidget("FLYOUT", self)
        self.mediaWidget = MediaWidget("MEDIA", self)
        self.menuCommandBar = MenuCommandBar('MENUCOMMAND', self)
        self.navWidget = NavWidget("NAV", self)
        self.scrollWidget = ScrollWidget("SCROLL", self)
        self.statusInfoWidget = StatusInfoWidget("STATUS", self)
        self.textWidget = TextWidget("TEXT", self)

        self.initWindow()
        self.initNavigationInterface()

    def initWindow(self):
        self.setWindowTitle("QFluentWidgets")
        self.setWindowIcon(Icon(FluentIcon.GITHUB))
        desktop = QApplication.primaryScreen().availableGeometry()
        self.resize(1200, 700)
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

    def initNavigationInterface(self):
        self.addSubInterface(
            self.buttonWidget,
            FluentIcon.CHECKBOX,
            '基本输入',
        )
        self.addSubInterface(
            self.dateTimeWidget,
            FluentIcon.DATE_TIME,
            '日期时间'
        )
        self.addSubInterface(
            self.dialogBoxPopWidget,
            FluentIcon.SEND,
            "弹出组件"
        )
        self.addSubInterface(
            self.mediaWidget,
            FluentIcon.MEDIA,
            '视频组件'
        )
        self.addSubInterface(
            self.menuCommandBar,
            FluentIcon.EDIT,
            '菜单和命令栏'
        )
        self.addSubInterface(
            self.navWidget,
            FluentIcon.MENU,
            '导航'
        )
        self.addSubInterface(
            self.scrollWidget,
            FluentIcon.SCROLL,
            "滚动区域"
        )
        self.addSubInterface(
            self.statusInfoWidget,
            FluentIcon.CHAT,
            '状态和信息'
        )
        self.addSubInterface(
            self.textWidget,
            FluentIcon.FONT_SIZE,
            '文本'
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
