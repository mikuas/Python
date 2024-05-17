from PySide6.QtWidgets import *


class Stats:

    def __init__(self, win_width, win_height, apptitle, text_width, text_height):
        # 创建主窗口对象
        self.window = QMainWindow()
        # 设置窗口的大小
        self.window.resize(win_width, win_height)
        # 设置窗口显示的位置
        self.window.move(300, 300)
        # 设置窗口的标题
        self.window.setWindowTitle(apptitle)

        # 设置文本控件
        self.textEdit = QPlainTextEdit(self.window)
        # 设置提示内容
        self.textEdit.setPlaceholderText('请输入资薪表')
        # 设置文本控件位置
        self.textEdit.move(10, 10)
        # 文本控件大小
        self.textEdit.resize(text_width, text_height)

        # 设置按钮
        self.button = QPushButton('统计', self.window)
        self.button.move(text_width + 50, text_height / 2)

        # 按钮点击事件
        self.button.clicked.connect(self.handeCale)

    def handeCale(self):

        # 获取文本控件内容
        info = self.textEdit.toPlainText()
        # 薪资20000 以上 和 以下 的人员名单
        salary_above_20k = ''
        salary_below_20k = ''
        for line in info.splitlines():
            if not line.strip():
                continue
            parts = line.split(' ')
            # 去掉列表中的空字符串内容
            parts = [p for p in parts if p]
            name, salary, age = parts
            if int(salary) >= 20000:
                salary_above_20k += name + '\n'
            else:
                salary_below_20k += name + '\n'

        QMessageBox.about(self.window,
                          '统计结果',
                          f'''薪资20000 以上的有：\n{salary_above_20k}
                        \n薪资20000 以下的有：\n{salary_below_20k}'''
                          )


if __name__ == '__main__':
    app = QApplication([])
    stats = Stats(500, 500, 'Title', 300, 480)
    stats.window.show()
    app.exec()


