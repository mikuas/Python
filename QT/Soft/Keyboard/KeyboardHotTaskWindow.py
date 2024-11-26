from PyMyMethod import KeyboardControl

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QSizePolicy,
    QMessageBox
)
from PySide6.QtCore import Qt, QTimer


class KeyboardHotTaskWindow(QWidget):
    def __init__(self, width, height):
        super().__init__()
        self.closeEvent = lambda event: (event.ignore(), self.hide())
        self.setMinimumSize(width, height)
        self.setWindowTitle('执行组合键盘任务')

        self.keyboardHotEdit = QLineEdit(self)
        self.keyboardHotEdit.setPlaceholderText('请输入按键,多个按键之间用空格隔开')
        self.keyboardHotEdit.setStyleSheet('font-size:18px;')
        self.keyboardHotEdit.setMinimumSize(200, 80)
        self.keyboardHotEdit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        self.keyboardTimeHotEdit = QLineEdit(self)
        self.keyboardTimeHotEdit.setPlaceholderText('请输入时间/s,不写默认为0')
        self.keyboardTimeHotEdit.setStyleSheet('font-size:18px;')
        self.keyboardTimeHotEdit.setMinimumSize(200, 80)
        self.keyboardTimeHotEdit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        self.keyboardTaskHotButton = QPushButton('开始执行', self)
        self.keyboardTaskHotButton.setFixedSize(150, 50)
        self.keyboardTaskHotButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.keyboardTaskHotButton.clicked.connect(self.keyboardHotClick)

        layout = QVBoxLayout(self)
        layout.addWidget(self.keyboardHotEdit)
        layout.addStretch(1)
        layout.addWidget(self.keyboardTimeHotEdit)
        layout.addStretch(1)
        layout.addWidget(self.keyboardTaskHotButton, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch(1)

    def keyboardHotClick(self):
        try:
            if not self.keyboardTimeHotEdit.text():
                time_min = 0
            else:
                time_min = float(self.keyboardTimeHotEdit.text()) * 1000
            hotKeys = self.keyboardHotEdit.text()

            if not hotKeys:
                QMessageBox.warning(self, '提示', '请输入按键!')
                return

            QTimer.singleShot(time_min, lambda: KeyboardControl().Hotkey(hotKeys))
            if time_min:
                QMessageBox.information(self, '提示', '任务已启动!')
            else:
                QMessageBox.information(self, '提示', '执行完毕!')

        except ValueError:
            QMessageBox.warning(self, '错误', '请输入正确的时间!')