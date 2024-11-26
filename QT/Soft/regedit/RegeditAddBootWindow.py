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

from PyMyMethod import FileControl, Regedit


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

        self.createObj()

    def createObj(self):
        objDict = ['选择启动路径', '为谁添加', '查询', '添加', '删除']
        objMethod = [
            self.click,
            '',
            lambda: QMessageBox.information(self, '查询结果', Regedit().queryRegeditContent('', True)),
            lambda: self.addClick(self.textEdit.toPlainText()),
            lambda: self.delClick(self.textEdit.toPlainText())
        ]
        styles = [
            "background-color: pink; font-size: 32px",
            'font-size: 24px',
            """
                QPushButton {
                    background-color: #00FF7F;
                    font-size: 32px;
                }
                QPushButton:hover {
                    background-color: #00BFFF;
                }
            """,
            '',
            ''
        ]

        mainLayout = QVBoxLayout(self)
        self.centerLayout.addWidget(self.textEdit, alignment=Qt.AlignmentFlag.AlignCenter)
        self.centerLayout.addStretch()

        for obj, fc, style in zip(objDict, objMethod, styles):
            if obj in ['查询', '添加', '删除']:
                style = styles[2]
            if fc is None:
                label = QLabel(obj)
                label.setStyleSheet(style)
                self.centerLayout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
                continue
            if obj == '为谁添加':
                label = QLabel(obj)
                label.setStyleSheet(style)
                self.centerLayout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
                self.centerLayout.addWidget(self.comboBox, alignment=Qt.AlignmentFlag.AlignCenter)
                continue
            button = QPushButton(obj, self)
            button.setFixedSize(100, 60)
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            button.setMinimumWidth(int(self.width() * 0.5))
            button.setStyleSheet(style)
            button.clicked.connect(fc)
            self.centerLayout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)
        mainLayout.addStretch()
        mainLayout.addLayout(self.centerLayout)
        mainLayout.addStretch()

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
        if not name:
            QMessageBox.warning(self, '提示', '输入有误')
        else:
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
