import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication
from PySide6.QtCore import Qt

from qfluentwidgets import SearchLineEdit
from qframelesswindow.webengine import FramelessWebEngineView

class CustomSearchLineEdit(SearchLineEdit):
    def __init__(self, webView, target, parent=None):
        super().__init__(parent)
        self.target = target
        self.webView = webView

    # 输入回车更新URL
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.webView.setUrl(self.target(self.text()))
        super().keyPressEvent(event)


class WebView(QWidget):
    def __init__(self, text, url, parent=None):
        super().__init__(parent)
        self.setWindowTitle("WebView")
        self.setWindowIcon(QIcon('data/images/icon/chrome.png'))
        self.resize(1200, 700)
        self.qHboxLayout = QVBoxLayout(self)
        self.web_view = FramelessWebEngineView(self)

        self.lineEdit = CustomSearchLineEdit(self.web_view, self.fillUrl, self)
        self.lineEdit.setPlaceholderText('请输入网址')
        self.lineEdit.searchSignal.connect(lambda text: self.web_view.setUrl(self.fillUrl(text)))
        # 加载初始网页
        self.web_view.load(url)  # 替换为需要访问的 URL

        self.qHboxLayout.addWidget(self.lineEdit)
        self.qHboxLayout.addWidget(self.web_view)
        self.setObjectName(text.replace(" ", "_"))

    @staticmethod
    def fillUrl(url):
        if '//' not in url:
            return 'https://' + url
        else:
            return url

    # def closeEvent(self, event):
    #     event.ignore()
    #     self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WebView("WEBVIEW", "www.baidu.com")
    window.show()
    sys.exit(app.exec())