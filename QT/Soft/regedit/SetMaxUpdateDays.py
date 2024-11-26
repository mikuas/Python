import sys

from PySide6.QtWidgets import (
    QPushButton,
    QApplication,
    QTextEdit,
    QVBoxLayout,
    QWidget,
    QMessageBox
)
from PySide6.QtCore import Qt

from PyMyMethod import Regedit


class SetMaxUpdateDays(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(500, 320)
        self.setWindowTitle('设置最大暂停更新天数')
        self.closeEvent = lambda event: (event.ignore(), self.hide())
        self.centerLayout = QVBoxLayout(self)

        self.textEdit = QTextEdit(self)
        self.textEdit.setPlaceholderText('暂停天数')
        self.textEdit.setStyleSheet('font-size: 32px')
        self.textEdit.setFixedSize(300, 60)
        self.textEdit.setMinimumWidth(int(self.width() * 0.5))

        self.centerLayout.addStretch()
        self.centerLayout.addWidget(self.textEdit, alignment=Qt.AlignmentFlag.AlignCenter)
        self.centerLayout.addStretch()

        self.button = QPushButton("确定", self)
        self.button.setFixedSize(200, 60)
        self.button.setStyleSheet(
            """
                QPushButton {
                    font-size: 24px;
                    background-color: pink
                }
                QPushButton:hover {
                    background-color: #00BFFF;
                }
            """
        )
        self.button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.button.setMinimumWidth(int(self.width() * 0.5))
        self.button.clicked.connect(self.click)

        self.centerLayout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.centerLayout.addStretch()

        mainLayout = QVBoxLayout(self)

        mainLayout.addStretch()
        mainLayout.addLayout(self.centerLayout)
        mainLayout.addStretch()

    def click(self):
        days = self.textEdit.toPlainText()
        try:
            if days:
                Regedit().setWindowsUpdateDays(int(days))
                QMessageBox.information(self, "提示", f"设置成功,暂停最大天数为{days}天")
            else:
                QMessageBox.warning(self, "提示", "未输入天数")
        except ValueError:
                QMessageBox.warning(self, "警告", "请输入数字")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SetMaxUpdateDays()
    window.show()
    sys.exit(app.exec())
