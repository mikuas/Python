import sys

from PySide6.QtWidgets import QApplication
from qfluentwidgets import ImageLabel

from QtFluentWidgets.FluentWidgetModule.FluentWidgets import (
    VerticalScrollWidget, HorizontalScrollWidget,
    ScrollWidget, SmoothScrollWidget,
    PrimaryButtonCard, WinFluentIcon, VBoxLayout
)


class VerticalWidget(VerticalScrollWidget):
    def __init__(self):
        super().__init__()
        for _ in range(10):
            button = PrimaryButtonCard(
                WinFluentIcon.WIFI,
                f"PrimaryButton{_}",
                '',
                '确定',
                parent=self
            )
            self.vBoxLayout.addWidget(button)


class HorizontalWidget(HorizontalScrollWidget):
    def __init__(self):
        super().__init__()
        self.vLayout = VBoxLayout(self)
        for _ in range(10):
            button = PrimaryButtonCard(
                WinFluentIcon.WIFI,
                f"PrimaryButton{_}",
                '',
                '确定',
                parent=self
            )
            self.hBoxLayout.addWidget(button)
        for _ in range(10):
            button = PrimaryButtonCard(
                WinFluentIcon.WIFI,
                f"PrimaryButton{_}",
                '',
                '确定',
                parent=self
            )
            self.vLayout.addWidget(button)
        self.hBoxLayout.addLayout(self.vLayout)


class ScrollWidget(ScrollWidget):
    def __init__(self):
        super().__init__()
        self.vBoxLayout = self.createVBoxLayout()
        self.hBoxLayout = self.createHBoxLayout()
        self.vBoxLayout.addLayout(self.hBoxLayout)
        for _ in range(10):
            button = PrimaryButtonCard(
                WinFluentIcon.WIFI,
                f"PrimaryButton{_}",
                '',
                '确定',
                parent=self
            )
            self.vBoxLayout.addWidget(button)
        for _ in range(10):
            button = PrimaryButtonCard(
                WinFluentIcon.WIFI,
                f"PrimaryButton{_}",
                '',
                '确定',
                parent=self
            )
            self.hBoxLayout.addWidget(button)


class SmoothScrollWidget(SmoothScrollWidget):
    def __init__(self):
        super().__init__()
        self.createVBoxLayout().addWidget(
            ImageLabel(r"C:\Users\Administrator\OneDrive\Pictures\15.jpg", self)
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = SmoothScrollWidget()
    w.resize(800, 600)
    w.show()
    sys.exit(app.exec())