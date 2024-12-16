import sys

from PySide6.QtWidgets import QApplication
from qfluentwidgets import FluentIcon

from QFluentWidgets.FluentWidgetModule.FluentWidgets import MoreButtonCard, VBoxLayout, MorePrimaryButtonCard, \
    MoreTransparentButtonCard, VerticalScrollWidget


class Demo(VerticalScrollWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 650)
        self.vLayout = VBoxLayout(self)

        self.vLayout.addWidgets([
            MoreButtonCard(
                FluentIcon.GITHUB,
                'MoreButtonCard',
                '',
                '确定'
            ),
            MorePrimaryButtonCard(
                FluentIcon.HOME,
                'MorePrimaryButtonCard',
                '',
                '确定'
            ),
            MoreTransparentButtonCard(
                FluentIcon.WIFI,
                'MoreTransparentButtonCard',
                '',
                '确定'
            )
        ])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Demo()
    window.show()
    sys.exit(app.exec())