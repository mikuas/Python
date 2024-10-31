from PySide6.QtWidgets import QHBoxLayout, QPushButton
from PySide6.QtGui import QIcon, Qt
from PySide6.QtCore import QSize


def createButton(btName, icons, style, functions):
    stopButton = None
    layout = QHBoxLayout()
    for bt, icon, fc in zip(btName, icons, functions):
        button = QPushButton(bt)
        button.setIcon(QIcon(icon))
        button.setIconSize(QSize(40, 40))
        button.setStyleSheet(style)
        button.setCursor(Qt.CursorShape.PointingHandCursor)
        button.clicked.connect(fc)
        button.setFixedSize(150, 80)
        layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignTop)
        if bt == '播放':
            stopButton = button

    return layout, stopButton
