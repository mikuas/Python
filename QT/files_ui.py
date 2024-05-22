from PySide6.QtCore import *
from PySide6.QtUiTools import *
from PySide6.QtWidgets import *

uiLoader = QUiLoader()


class Stats:

    def __init__(self):
        # 从文件中加载UI定义
        qfile_stats = QFile('main.ui')
        qfile_stats.open(QFile.ReadOnly)
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = uiLoader.load(qfile_stats)
        self.ui.text_one = QPlainTextEdit(self.ui)
        self.ui.text_one.setPlaceholderText('Hello')

        # self.ui.button.clicked.connect(self.handleCalc)
        self.ui.button_one.click.connect(self.handleCalc())

    def handleCalc(self):
        QMessageBox.about(self.ui, 'Test', '123')
        pass


app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec()
