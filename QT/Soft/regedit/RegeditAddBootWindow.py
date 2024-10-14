import sys

from PySide6.QtWidgets import (
    QPushButton,
    QApplication,
    QTextEdit,
    QVBoxLayout,
    QWidget,
    QLabel,
    QComboBox,
    QMessageBox
)
from PySide6.QtCore import Qt

from PyMyMethods.Method import FileControl, Regedit


class RegeditAddBootWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(750, 500)
        self.setWindowTitle('添加开机启动项')
        self.closeEvent = lambda event: (event.ignore(), self.hide())
        self.path = None
        self.centerLayout = QVBoxLayout()

        self.textEdit = QTextEdit(self)
        self.textEdit.setPlaceholderText('名称')
        self.textEdit.setStyleSheet('font-size: 24px')
        self.textEdit.setFixedSize(300, 50)
        self.textEdit.setMinimumWidth(int(self.width() * 0.5))

        self.pathButton = QPushButton('选择启动路径', self)
        self.pathButton.setFixedSize(100, 60)
        self.pathButton.setObjectName('pathButton')
        self.pathButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.pathButton.setMinimumWidth(int(self.width() * 0.5))
        self.pathButton.clicked.connect(self.click)
        self.pathButton.setStyleSheet("background-color: pink; font-size: 32px")

        self.addButton = QPushButton('添加', self)
        self.addButton.setFixedSize(100, 60)
        self.addButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.addButton.setObjectName('addButton')
        self.addButton.setMinimumWidth(int(self.width() * 0.5))
        self.addButton.clicked.connect(lambda: self.addClick(self.textEdit.toPlainText()))

        self.delButton = QPushButton('删除', self)
        self.delButton.setFixedSize(100, 60)
        self.delButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.delButton.setObjectName('delButton')
        self.delButton.setMinimumWidth(int(self.width() * 0.5))
        self.delButton.clicked.connect(lambda: self.delClick(self.textEdit.toPlainText()))

        self.label = QLabel('为谁添加')
        self.label.setStyleSheet('font-size: 24px')

        self.queryButton = QPushButton('查询', self)
        self.queryButton.setFixedSize(100, 60)
        self.queryButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.queryButton.setObjectName('queryButton')
        self.queryButton.setMinimumWidth(int(self.width() * 0.5))
        self.queryButton.clicked.connect(lambda: QMessageBox.information(self, '查询结果', Regedit().queryRegeditContent('', True)))

        self.comboBox = QComboBox()
        self.comboBox.setMinimumSize(100, 60)
        self.comboBox.setMinimumWidth(int(self.width() * 0.5))
        self.comboBox.setStyleSheet(
            """
                QComboBox {
                    background-color: pink;
                    font-size: 20px;
                }
                QComboBox QAbstractItemView::item {
                    height: 50px;
                }
                QComboBox QAbstractItemView {
                    background-color: lightblue;
                }
            """
        )
        self.comboBox.setCursor(Qt.CursorShape.PointingHandCursor)
        self.comboBox.addItem('当前用户')
        self.comboBox.addItem('所有用户')

        mainLayout = QVBoxLayout(self)

        for i in [self.textEdit, self.pathButton, self.label, self.comboBox, self.queryButton, self.addButton, self.delButton]:
            self.centerLayout.addWidget(i, alignment=Qt.AlignmentFlag.AlignCenter)
            self.centerLayout.addStretch()

        mainLayout.addStretch()
        mainLayout.addLayout(self.centerLayout)  # 将居中的布局加入主布局
        mainLayout.addStretch()

        self.setStyleSheet(
            """
                QPushButton#addButton, #delButton, #queryButton {
                    background-color: #00FF7F;
                    font-size: 32px;
                }
                QPushButton#addButton:hover, #delButton:hover, #queryButton:hover, #pathButton:hover {
                    background-color: #00BFFF;
                }
            """
        )

    def addClick(self, name):
        text = self.comboBox.currentText()
        try:
            if not self.path:
                QMessageBox.warning(self, '警告', '请选择路径')
                return
            path = self.path.replace('/', '\\')
            if text == '当前用户':
                Regedit().addAutoBoot(name, path, True)
                QMessageBox.information(self, '提示', '添加成功')
            elif text == '所有用户':
                Regedit().addAutoBoot(name, path)
                QMessageBox.information(self, '提示', '添加成功')
        except Exception:
            return

    def delClick(self, name):
        text = self.comboBox.currentText()
        if text == '当前用户':
            Regedit().delAutoBoot(name, True)
            QMessageBox.information(self, '提示', '删除成功')
        elif text == '所有用户':
            Regedit().delAutoBoot(name)
            QMessageBox.information(self, '提示', '删除成功')

    def click(self):
        self.path = FileControl().getFilePathQT(self, True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegeditAddBootWindow()
    window.show()
    sys.exit(app.exec())
