from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from qfluentwidgets import *

import sys


class CustomMessageBox(MessageBoxBase):
    """ Custom message box """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel('打开 URL', self)
        self.urlLineEdit = LineEdit()

        self.urlLineEdit.setPlaceholderText('输入网站 URL')
        self.urlLineEdit.setClearButtonEnabled(True)

        # 将组件添加到布局中
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.urlLineEdit)

        # 设置对话框的最小宽度
        self.widget.setMinimumWidth(350)


    def showMessage(self, parent, webView):
        w = CustomMessageBox(parent)
        if w.exec():
            webView.setUrl(w.urlLineEdit.text())
            print(w.urlLineEdit.text())


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Web Browser")
        self.setGeometry(100, 100, 800, 600)

        self.web_view = QWebEngineView()
        self.setCentralWidget(self.web_view)

        layout = QVBoxLayout()
        self.button = TransparentPushButton(self)
        self.button.setText("切换URL")
        self.button.setIcon(FluentIcon.SEARCH)

        self.button.clicked.connect(lambda : CustomMessageBox(self).showMessage(self, self.web_view))

        layout.addWidget(self.button)
        layout.addWidget(self.web_view)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # 加载初始网页
        self.web_view.load("https://yiyan.baidu.com/")  # 替换为需要访问的 URL

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
