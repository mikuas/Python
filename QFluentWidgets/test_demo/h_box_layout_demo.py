import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QApplication, QGridLayout
from qfluentwidgets import TitleLabel, Theme, setTheme

from QFluentWidgets.FluentWidgetModule.FluentWidgets import VBoxLayout, HBoxLayout


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 650)
        self.vBoxLayout = VBoxLayout(self)
        self.hBoxLayout = HBoxLayout(self)
        self.gLayout = QGridLayout(self)

        # self.vBoxLayout.addLayout(self.hBoxLayout)
        self.vBoxLayout.addLayout(self.gLayout)

        # for _ in range(5):
        #     self.vBoxLayout.addWidget(
        #         TitleLabel(f"VBoxLayout{_}", self),
        #         alignment=Qt.AlignmentFlag.AlignCenter,
        #     )

        # for _ in range(5):
        #     self.hBoxLayout.addWidget(
        #         TitleLabel(f"HBoxLayout{_}", self)
        #     )
        self.gLayout.addWidget(
            TitleLabel("item1", self)
        )
        self.gLayout.addWidget(
            TitleLabel("item2", self),
            1, 2
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    setTheme(Theme.AUTO)
    demo.show()
    sys.exit(app.exec())