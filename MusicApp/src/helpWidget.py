from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon


class HelpWidget(QWidget):
    def __init__(self):
        super().__init__()
        mainLayout = QHBoxLayout(self)

        button = QPushButton(self)
        button.setFixedSize(350, 477)
        button.setIconSize(QSize(350, 477))
        button.setIcon(QIcon('../data/images/icon/money.png'))

        mainLayout.addWidget(button)