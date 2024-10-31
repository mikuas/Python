import sys
from symtable import Function

from PySide6.QtCore import QSize, QUrl
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget
from PySide6.QtGui import Qt
from qfluentwidgets import *


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

    def validate(self):
        """ 重写验证表单数据的方法 """
        isValid = QUrl(self.urlLineEdit.text()).isValid()
        self.warningLabel.setHidden(isValid)
        return isValid

    def showMessage(self, parent, webView):
        w = CustomMessageBox(parent)
        if w.exec():
            webView.setUrl(w.urlLineEdit.text())
            print(w.urlLineEdit.text())


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 450)
        centerWindget = QWidget(self)
        mainLayout = QVBoxLayout(centerWindget)

        '''无边框对话框'''
        # MessageBox()
        # Dialog()
        self.w = MessageBox('Title', 'Hello😍', self)

        # 覆盖默认文本
        self.w.yesButton.setText("✔️")
        self.w.cancelButton.setText("😍")

        # # 隐藏确认按钮
        # self.w.yesButton.hide()
        # self.w.buttonLayout.insertLayout(0, 1)
        #
        # # 隐藏取消按钮
        # self.w.cancelButton.hide()
        # self.w.buttonLayout.insertStretch(1)

        button = PushButton("OPEN")
        button.clicked.connect(self.w.open)

        mainLayout.addWidget(button)
        self.setCentralWidget(centerWindget)

    def open(self):
        if self.w.exec():
            print(True)
        else:
            print(False)

'''如果你想自定义对话框的内容，可继承 MessageBoxBase 并往 viewLayout 垂直布局中添加组件。下述代码创建了一个输入框对话框：'''
class CustomMessageBox(MessageBoxBase):
    """ Custom message box """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel('打开 URL')
        self.urlLineEdit = LineEdit()

        self.urlLineEdit.setPlaceholderText('输入文件、流或者播放列表的 URL')
        self.urlLineEdit.setClearButtonEnabled(True)

        # 将组件添加到布局中
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.urlLineEdit)

        # 设置对话框的最小宽度
        self.widget.setMinimumWidth(350)


def showMessage(window):
    w = CustomMessageBox(window)
    if w.exec():
        print(w.urlLineEdit.text())

# 对话框提供了 valdate() -> bool 方法，通过重写此方法，可在用户点击确定按钮时验证表单数据，
# 返回 True 代表表单数据正确，对话框会自动关闭。下面是一个示例：

class CustomMessageBox(MessageBoxBase):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel('打开 URL', self)
        self.urlLineEdit = LineEdit(self)

        self.urlLineEdit.setPlaceholderText('输入文件、流或者播放列表的 URL')
        self.urlLineEdit.setClearButtonEnabled(True)

        self.warningLabel = CaptionLabel("URL 不正确")
        self.warningLabel.setTextColor("#cf1010", QColor(255, 28, 32))

        # add widget to view layout
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.urlLineEdit)
        self.viewLayout.addWidget(self.warningLabel)
        self.warningLabel.hide()

        self.widget.setMinimumWidth(350)

    def validate(self):
        """ 重写验证表单数据的方法 """
        isValid = QUrl(self.urlLineEdit.text()).isValid()
        self.warningLabel.setHidden(isValid)
        return isValid


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())