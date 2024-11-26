from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox
from PySide6.QtCore import Qt

from PyMyMethod import FileControl

class ImageRenameWindow(QWidget):
    def __init__(self, width, height):
        super().__init__()
        self.dirFiles = None
        self.dirPath = None
        self.closeEvent = lambda event: (event.ignore(), self.hide())
        self.setMinimumSize(width / 1.5, height / 1.5)
        self.setWindowTitle('图片重命名')

        self.filePathButton = QPushButton('选择目录', self)
        self.filePathButton.setFixedSize(200, 80)
        self.filePathButton.setObjectName("filePathButton")
        self.filePathButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.filePathButton.clicked.connect(self.getDir)

        self.button = QPushButton('开始执行', self)
        self.button.setFixedSize(200, 80)
        self.button.setObjectName("button")
        self.button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.button.clicked.connect(self.click)

        self.setStyleSheet(
            """
                QPushButton#filePathButton, #button {
                    font-size: 20px;
                }
                
                QPushButton#filePathButton:hover, #button:hover {
                    background-color: pink;
                }
            """
        )

        layout = QVBoxLayout(self)
        layout.addWidget(self.filePathButton, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch(1)
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch(1)

    def getDir(self):
        self.dirPath = FileControl().getDirPathQT(self, True)

    def click(self):
        if not self.dirPath:
            QMessageBox.warning(self, '错误', '请选择目录!')
            return
        result = FileControl().imageReName(self.dirPath)
        QMessageBox.information(self, '提示', f'执行完毕! 以下文件被修改:{result[1]}\n{result[0]}')