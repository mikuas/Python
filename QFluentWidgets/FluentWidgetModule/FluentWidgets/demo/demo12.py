import sys

from PySide6.QtWidgets import QWidget, QApplication
from qfluentwidgets import FluentTitleBar
from qfluentwidgets.window.fluent_window import FluentWindowBase, FluentWindow
from qframelesswindow import AcrylicWindow
from qframelesswindow.windows import WindowsWindowEffect, WindowsFramelessMainWindow

from QFluentWidgets.FluentWidgetModule.FluentWidgets import FluentWidget


class Demo(FluentWindow):
    def __init__(self):
        super().__init__()
        self.setTitleBar(FluentTitleBar(self))
        self.setWindowTitle("AcrylicWindow")
        self.resize(800, 600)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec())