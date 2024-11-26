import sys
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QApplication,
    QPushButton,
    QLabel,
    QComboBox,
    QMessageBox
)
from PySide6.QtCore import Qt
from PyMyMethod import FileControl, Regedit

class RegeditAddLeftWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(750, 550)
        self.setWindowTitle('添加注册表点击值')
        self.closeEvent = lambda event: (event.ignore(), self.hide())
        self.filePath = None
        self.iconPath = None
        self.buttonDict = {}

        mainLayout = QVBoxLayout(self)
        self.centeredLayout = QVBoxLayout()

        self.label = QLabel('添加注册表点击值')
        self.label.setStyleSheet("font-size: 32px")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.centeredLayout.addWidget(self.label)

        self.comboBox = QComboBox()
        self.comboBox.setCursor(Qt.CursorShape.PointingHandCursor)
        self.comboBox.addItem('添加右键点击空白选项')
        self.comboBox.addItem('添加右键点击文件选项')
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
        self.comboBox.setFixedSize(int(self.width() * 0.6), 50)
        self.centeredLayout.addWidget(self.comboBox, alignment=Qt.AlignmentFlag.AlignCenter)

        self.addText = QTextEdit(self)
        self.addText.setPlaceholderText('输入要添加的名称')
        self.addText.setStyleSheet('font-size: 26px')
        self.addText.setFixedHeight(60)
        self.addText.setMinimumWidth(int(self.width() * 0.6))
        self.centeredLayout.addWidget(self.addText, alignment=Qt.AlignmentFlag.AlignCenter)

        self.createButtons()
        self.setButtonStyle(self.buttonDict)

        mainLayout.addStretch()
        mainLayout.addLayout(self.centeredLayout)
        mainLayout.addStretch()

    def createButtons(self):
        button_texts = ['选择文件路径', '选择图标ico(可选)', '点击文件是否传参', 'False', '添加', '删除(只需输入名称)']
        clickEvent = [
            lambda: self.click('filePath', True),
            lambda: self.click('iconPath', False),
            '',
            lambda: self.buttonDict['False'].setText('True' if self.buttonDict['False'].text() == 'False' else 'False'),
            lambda: self.start(self.comboBox.currentText(), self.addText.toPlainText().replace(' ', ''), self.filePath, self.iconPath, self.buttonDict['False'].text()),
            lambda: self.delete(self.addText.toPlainText().replace(' ', ''))
        ]

        for text in button_texts:
            if text == '点击文件是否传参':
                argsLabel = QLabel(text)
                argsLabel.setStyleSheet("font-size: 32px")
                self.centeredLayout.addWidget(argsLabel, alignment=Qt.AlignmentFlag.AlignCenter)
                continue
            button = QPushButton(text, self)
            button.setFixedSize(100, 60)
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            button.clicked.connect(clickEvent[button_texts.index(text)])
            button.setMinimumWidth(int(self.width() * 0.6))
            self.buttonDict[text] = button
            self.centeredLayout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)

    @staticmethod
    def setButtonStyle(buttonDict: dict):
        for key in buttonDict.keys():
            if key in ['选择文件路径', '选择图标ico(可选)', 'False']:
                buttonDict[key].setStyleSheet(
                    """
                    QPushButton {
                        background-color: pink;
                        font-size: 32px;
                    }
                    QPushButton:hover {
                        background-color: #00BFFF;
                    }
                    """
                )
            else:
                buttonDict[key].setStyleSheet(
                    """
                    QPushButton {
                        background-color: #00FF7F;
                        font-size: 32px;
                    }
                    QPushButton:hover {
                        background-color: aqua;
                    }
                    """
                )

    def delete(self, name):
        if not name:
            QMessageBox.warning(self, '警告', '请输入名称')
        elif self.comboBox.currentText() == '添加右键点击空白选项':
            Regedit().delLeftKeyClick(name)
            QMessageBox.information(self, '提示', '删除成功')
        elif self.comboBox.currentText() == '添加右键点击文件选项':
            Regedit().delFileLeftKeyClick(name)
            QMessageBox.information(self, '提示', '删除成功')

    def click(self, element, message=False):
        if element == 'filePath':
            self.filePath = FileControl().getFilePathQT(self, message=message)
        elif element == 'iconPath':
            self.iconPath = FileControl().getFilePathQT(self, message=message)

    def start(self, selector, name, filePath, iconPath, args):
        if not name:
            QMessageBox.warning(self, '警告', '参数有误')
        elif filePath is None:
            QMessageBox.warning(self, '警告', '参数有误')
        else:
            try:
                filePath = filePath.replace('/', '\\')
                if selector == '添加右键点击空白选项':
                    Regedit().addLeftKeyClick(name, filePath, iconPath)
                    QMessageBox.information(self, '提示', '添加成功')
                elif selector == '添加右键点击文件选项' and args == 'True':
                    Regedit().addFileLeftKeyClick(name, filePath, iconPath, True)
                    QMessageBox.information(self, '提示', '添加成功')
                elif selector == '添加右键点击文件选项' and args == 'False':
                    Regedit().addFileLeftKeyClick(name, filePath, iconPath, False)
                    QMessageBox.information(self, '提示', '添加成功')
            except Exception:
                QMessageBox.warning(self, '警告', '参数错误')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegeditAddLeftWindow()
    window.show()
    sys.exit(app.exec())
