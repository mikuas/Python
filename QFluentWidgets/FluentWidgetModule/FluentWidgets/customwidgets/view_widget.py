from qfluentwidgets import (
    Dialog as View, MessageBoxBase, SubtitleLabel, LineEdit, MessageBox as MsbBox, ColorDialog as ColorD
)


class Dialog(View):
    """ 无边框对话框 """
    def __init__(self, title, content, parent):
        super().__init__(title, content, parent)
        setButtonText(self.yesButton, self.cancelButton)


class MessageBox(MsbBox):
    """ 带遮罩的对话框 """
    def __init__(self, title, content, parent=None):
        super().__init__(title, content, parent)
        setButtonText(self.yesButton, self.cancelButton)


class UrlDialog(MessageBoxBase):
    """ 链接对话框 """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel('打开 URL', self)
        self.urlLineEdit = LineEdit()

        self.urlLineEdit.setPlaceholderText('输入文件、流或者播放列表的 URL')
        self.urlLineEdit.setClearButtonEnabled(True)

        # add widget to layout
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.urlLineEdit)

        # set min width
        self.widget.setMinimumWidth(350)

        setButtonText(self.yesButton, self.cancelButton)


class ColorDialog(ColorD):
    def __init__(self, color, title, parent=None, enableAlpha=False):
        super().__init__(color, title, parent, enableAlpha)
        setButtonText(self.yesButton, self.cancelButton)

    def getColor(self):
        self.exec()
        return self.color.name()


def setButtonText(yesBt, cancelBt):
    yesBt.setText('确定')
    cancelBt.setText('取消')
