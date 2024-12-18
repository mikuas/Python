import sys

from PySide6.QtWidgets import QApplication, QRadioButton, QCheckBox, QProgressBar, QDial, QStatusBar

from FluentWidgets import VerticalScrollWidget
from qfluentwidgets import RadioButton


class Demo(VerticalScrollWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 350)
        self.radioButton = QRadioButton(self)
        self.radioButton.setStyleSheet('background-color:none')

        self.checkBox = QCheckBox(self)

        self.progressBar = QProgressBar(self)
        self.progressBar.setRange(0, 100)

        self.dial = QDial(self)
        self.dial.setRange(0, 100)
        self.dial.setNotchesVisible(True)
        self.dial.valueChanged.connect(
            lambda value: print(value)
        )

        self.statusBar = QStatusBar(self)
        self.statusBar.showMessage('Hello World', -1)

        self.initLayout()

    def initLayout(self):
        self.vBoxLayout.addWidgets([
            self.radioButton,
            self.checkBox,
            self.progressBar,
            self.dial,
            self.statusBar,
        ])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec())