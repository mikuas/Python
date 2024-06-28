import os
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QMessageBox
from PySide6.QtCore import QTimer, Qt

class Windows(QWidget):

    def __init__(self, w, h):
        super().__init__()

        self.setWindowTitle('Timing Task')
        self.resize(w, h)

        # 创建控件
        self.textEdit = QLineEdit()
        # 设置宽高
        self.textEdit.setMinimumSize(w * 0.8, h * 0.2)
        self.textEdit.move(w * 0.1, h * 0.2)
        self.textEdit.setPlaceholderText('请输入时间/s')

        self.textCommand = QLineEdit()
        # 设置宽高
        self.textCommand.setMinimumSize(w * 0.8, h * 0.2)
        self.textCommand.move(w * 0.1, h * 0.6)
        self.textCommand.setPlaceholderText('请输入要执行的命令')

        # 设置按钮
        self.button = QPushButton('开始执行')
        self.button.setMinimumSize(w * 0.3, h * 0.2)
        # 添加点击功能
        self.button.clicked.connect(self.click)

        # 创建布局管理器并设置布局
        layout = QVBoxLayout(self)  # 创建一个垂直布局管理器，并将其绑定到当前窗口（self）上
        layout.addWidget(self.textEdit)  # 将文本输入框 (self.textEdit) 添加到垂直布局中
        layout.addWidget(self.textCommand)  # 将命令输入框 (self.textCommand) 添加到垂直布局中
        layout.addWidget(self.button)  # 将按钮 (self.button) 添加到垂直布局中

        self.setLayout(layout)

    def click(self):
        try:
            time_min = float(self.textEdit.text()) * 1000
            command = self.textCommand.text()

            if not command:
                # 警告窗口 warning
                QMessageBox.warning(self, '提示', '请输入命令!')
                return

            # 执行命令
            QTimer.singleShot(time_min, lambda: os.system(command))
            # 提示窗口 information
            QMessageBox.information(self, '提示', '任务已启动!')

        except ValueError:
            QMessageBox.warning(self, '错误', '请输入正确的时间!')

def main():
    app = QApplication([])
    main_window = Windows(500, 300)
    main_window.show()
    app.exec()


if __name__ == '__main__':
    main()
