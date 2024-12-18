from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPainter, QColor, QImage, QBrush
from PySide6.QtWidgets import QWidget, QApplication, QGraphicsBlurEffect
import sys

from qfluentwidgets import FluentIcon, TitleLabel, setTheme, Theme, MSFluentWindow

from QtFluentWidgets.FluentWidgetModule.FluentWidgets import NavigationWidget, MSNavigationWidget


class Window(MSFluentWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.addSubInterface(
            MsNav(),
            FluentIcon.HOME_FILL,
            'HOME'
        )


# class MsNav(MSNavigationWidget):
class MsNav(NavigationWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('MsNav')
        self.setWindowTitle("Windows 11 Acrylic Effect")
        self.addSubInterface(
            'route1',
            FluentIcon.HOME,
            'HOME',
            TitleLabel("HOME_INTERFACE", self)
        ).addSubInterface(
            'route2',
            FluentIcon.SETTING,
            'SETTING',
            TitleLabel("SETTING", self)
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    ms = MsNav()
    setTheme(Theme.LIGHT)
    window.show()
    ms.show()
    sys.exit(app.exec())
