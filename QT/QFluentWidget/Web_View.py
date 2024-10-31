from PySide6.QtCore import QUrl, Qt
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from qfluentwidgets import *

import sys


class CustomSearchLineEdit(SearchLineEdit):
    def __init__(self, webView, parent=None):
        super().__init__(parent)
        self.webView = webView

    # 输入回车更新URL
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.webView.setUrl(self.text())
        super().keyPressEvent(event)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Web Browser")
        self.setGeometry(0, 0, 1300, 700)

        self.web_view = QWebEngineView()
        self.setCentralWidget(self.web_view)

        layout = QVBoxLayout()

        self.lineEdit = CustomSearchLineEdit(self.web_view, self)
        self.lineEdit.setPlaceholderText('请输入网址')
        self.lineEdit.searchSignal.connect(lambda text: self.web_view.setUrl(text))

        layout.addWidget(self.lineEdit)
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
