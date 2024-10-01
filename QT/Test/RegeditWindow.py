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

from QT.Test.method import Regedit
from method import FileControl  # 确保该模块和类是正确导入的

class RegeditWindow(QWidget):
    def __init__(self, width, height):
        super().__init__()

        # 设置窗口大小和标题
        self.setMinimumSize(width, height)
        self.setWindowTitle('Regedit')
        self.filePath = None
        self.iconPath = None

        # 设置主布局
        main_layout = QVBoxLayout(self)

        # 创建一个水平布局，用于控制控件居中
        centered_layout = QVBoxLayout()

        # 创建标签
        self.label = QLabel('添加注册表点击')
        self.label.setStyleSheet("font-size: 32px")
        self.label.setAlignment(Qt.AlignCenter)  # 标签居中
        centered_layout.addWidget(self.label)

        # 创建下拉菜单
        self.comboBox = QComboBox()
        self.comboBox.setCursor(Qt.PointingHandCursor)
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
        self.comboBox.setFixedSize(int(width * 0.6), 50)  # 设置为窗口宽度的 60%
        centered_layout.addWidget(self.comboBox, alignment=Qt.AlignCenter)

        # 创建文本编辑框
        self.addText = QTextEdit(self)
        self.addText.setPlaceholderText('输入要添加的名称')
        self.addText.setStyleSheet('font-size: 26px')
        self.addText.setFixedHeight(60)
        self.addText.setFixedWidth(int(width * 0.6))  # 设置为窗口宽度的 60%
        centered_layout.addWidget(self.addText, alignment=Qt.AlignCenter)

        # 创建选择文件路径按钮
        self.getPathButton = QPushButton('选择文件路径', self)
        self.getPathButton.setFixedHeight(60)
        self.getPathButton.setFixedWidth(int(width * 0.6))  # 设置为窗口宽度的 60%
        self.getPathButton.setObjectName("getPathButton")
        self.getPathButton.setCursor(Qt.PointingHandCursor)
        self.getPathButton.clicked.connect(lambda: self.click('filePath', True))
        centered_layout.addWidget(self.getPathButton, alignment=Qt.AlignCenter)

        # 图标
        self.getIconPathButton = QPushButton('选择图标ico(可选)', self)
        self.getIconPathButton.setFixedHeight(60)
        self.getIconPathButton.setFixedWidth(int(width * 0.6))
        self.getIconPathButton.setObjectName("getIconPathButton")
        self.getIconPathButton.setCursor(Qt.PointingHandCursor)
        self.getIconPathButton.clicked.connect(lambda: self.click('iconPath', True))
        centered_layout.addWidget(self.getIconPathButton, alignment=Qt.AlignCenter)

        # 参数
        self.argsLabel = QLabel('点击文件是否传参')
        self.argsLabel.setStyleSheet("font-size: 32px")
        centered_layout.addWidget(self.argsLabel, alignment=Qt.AlignCenter)

        self.getArgsButton = QPushButton('False', self)
        self.getArgsButton.setFixedHeight(60)
        self.getArgsButton.setFixedWidth(int(width * 0.6))
        self.getArgsButton.setObjectName("getArgsButton")
        self.getArgsButton.setCursor(Qt.PointingHandCursor)
        self.getArgsButton.clicked.connect(lambda: self.getArgsButton.setText('True' if self.getArgsButton.text() == 'False' else 'False'))
        centered_layout.addWidget(self.getArgsButton, alignment=Qt.AlignCenter)

        self.setStyleSheet(
            """
                QPushButton#getPathButton, #getIconPathButton, #getArgsButton {
                    background-color: pink;
                    font-size: 32px;
                }
            """
        )

        self.startButton = QPushButton('添加', self)
        self.startButton.setFixedHeight(60)
        self.startButton.setFixedWidth(int(width * 0.6))
        self.startButton.setStyleSheet("background-color: #00FF7F; font-size: 32px;")
        self.startButton.setCursor(Qt.PointingHandCursor)
        self.startButton.clicked.connect(lambda: self.start(
            self.comboBox.currentText(),
            self.addText.toPlainText(),
            self.filePath,
            self.iconPath,
            self.getArgsButton.text()
        ))
        centered_layout.addWidget(self.startButton, alignment=Qt.AlignCenter)

        self.delButton = QPushButton('删除(只需输入名称)', self)
        self.delButton.setFixedHeight(60)
        self.delButton.setFixedWidth(int(width * 0.6))
        self.delButton.setStyleSheet("background-color: #00FF7F; font-size: 32px;")
        self.delButton.setCursor(Qt.PointingHandCursor)
        self.delButton.clicked.connect(lambda: self.delete(self.addText.toPlainText()))

        centered_layout.addWidget(self.delButton, alignment=Qt.AlignCenter)

        # 添加到主布局中
        main_layout.addStretch()
        main_layout.addLayout(centered_layout)  # 将居中的布局加入主布局
        main_layout.addStretch()

    def closeEvent(self, event):
        event.ignore()
        self.hide()

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
    window = RegeditWindow(750, 550)
    window.show()
    sys.exit(app.exec())
