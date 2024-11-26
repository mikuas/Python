from PyMyMethod import KeyboardControl

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QMessageBox,
    QSizePolicy
)
from PySide6.QtCore import QTimer, Qt


class KeyboardTaskWindow(QWidget):
    def __init__(self, width, height):
        super().__init__()
        self.closeEvent = lambda event: (event.ignore(), self.hide())
        self.setMinimumSize(width, height)
        self.setWindowTitle('执行依次点击键盘任务')

        self.keyboardEdit = QLineEdit(self)
        self.keyboardEdit.setPlaceholderText('请输入按键,多个按键之间用空格隔开')
        self.keyboardEdit.setStyleSheet('font-size:18px;')
        self.keyboardEdit.setMinimumSize(200, 80)
        self.keyboardEdit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        self.keyboardTimeEdit = QLineEdit(self)
        self.keyboardTimeEdit.setPlaceholderText('请输入时间/s,不写默认为0')
        self.keyboardTimeEdit.setStyleSheet('font-size:18px;')
        self.keyboardTimeEdit.setMinimumSize(200, 80)
        self.keyboardTimeEdit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        self.keyboardTaskButton = QPushButton('开始执行', self)
        self.keyboardTaskButton.setFixedSize(150, 50)
        self.keyboardTaskButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.keyboardTaskButton.clicked.connect(self.keyboardClick)

        layout = QVBoxLayout(self)
        layout.addWidget(self.keyboardEdit)
        layout.addStretch(1)
        layout.addWidget(self.keyboardTimeEdit)
        layout.addStretch(1)
        layout.addWidget(self.keyboardTaskButton, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch(1)

    def keyboardClick(self):
        try:
            if self.keyboardTimeEdit.text():
                time_min = float(self.keyboardTimeEdit.text()) * 1000
            else:
                time_min = 0
            keys = self.keyboardEdit.text()

            if not keys:
                QMessageBox.warning(self, '提示', '请输入按键!')
                return

            QTimer.singleShot(time_min, lambda: KeyboardControl().keyClick(keys))
            if time_min:
                QMessageBox.information(self, '提示', '任务已启动!')
            else:
                QMessageBox.information(self, '提示', '执行完毕!')
            print(self.keyboardTimeEdit.text())
        except ValueError:
            QMessageBox.warning(self, '错误', '请输入正确的时间!')