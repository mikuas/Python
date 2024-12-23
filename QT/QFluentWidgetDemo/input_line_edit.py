import sys

from PySide6.QtWidgets import QWidget, QApplication, QCompleter, QLineEdit, QVBoxLayout
from qfluentwidgets import *
from PySide6.QtGui import Qt, QAction
from pyecharts.charts import Bar
from pyecharts import options as opts


class Window(QWidget):
    def __init__(self):
        super().__init__()
        '''输入框'''
        layout = QVBoxLayout(self)
        lineEdit = LineEdit(self)

        # 提示文本
        lineEdit.setPlaceholderText("Input Email")

        # 设置文本
        lineEdit.setText("example@example.com")
        # 启用清空按钮
        lineEdit.setClearButtonEnabled(True)

        # 设置补全菜单
        stands = [
            "Star Platinum", "Hierophant Green", "Made in Haven",
            "King Crimson", "Silver Chariot", "Crazy diamond"
        ]
        completer = QCompleter(stands, lineEdit)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setMaxVisibleItems(10)

        lineEdit.setCompleter(completer)


        # 自定义动作
        # 在后面添加按钮
        action1 = QAction(FluentIcon.CALENDAR.qicon(), "", triggered=lambda: print("action1 triggered"))
        lineEdit.addAction(action1, QLineEdit.TrailingPosition)

        # 在前面添加按钮
        action2 = Action(FluentIcon.ADD, "", triggered=lambda: print("action2 triggered"))
        lineEdit.addAction(action2, QLineEdit.LeadingPosition)

        # 添加搜索按钮
        lineEdit2 = SearchLineEdit(self)
        # 连接信号插槽
        lineEdit2.searchSignal.connect(lambda text: print(text))

        # 密码输入框
        pl = PasswordLineEdit(self)
        pl.setText('123456')

        # 显示密码
        # pl.setPasswordVisible(True)
        layout.addWidget(lineEdit)
        layout.addWidget(lineEdit2)
        layout.addWidget(pl)

        # 多行文本输入框
        te = TextEdit(self)
        # 可渲染HTML,Markdown
        te.setMarkdown('## Hello \n * Markdown \n * HTML')
        # te.setHtml(create_chart('HTML'))
        # 获取普通文本
        print(te.toPlainText())
        # 获取富文本
        print(te.toHtml())
        layout.addWidget(te)

    # 创建图表并返回 HTML 字符串
    def create_chart(self, page_name):
        bar = (
            Bar()
            .add_xaxis(["A", "B", "C", "D", "E"])
            .add_yaxis("Series 1", [1, 2, 3, 4, 5])
            .set_global_opts(title_opts=opts.TitleOpts(title=f"{page_name} Chart"))
        )

        return bar.render_embed()  # 返回图表的 HTML 内容

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
