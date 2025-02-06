import sys

from PySide6.QtCore import QUrl, QTime, QDate
from PySide6.QtWidgets import QWidget, QApplication, QHBoxLayout, QCompleter, QLineEdit
from PySide6.QtGui import Qt, QColor, QAction

from qfluentwidgets import SmoothScrollArea, VBoxLayout, FluentLabelBase, CaptionLabel, BodyLabel, StrongBodyLabel, \
    SubtitleLabel, TitleLabel, LargeTitleLabel, DisplayLabel, ImageLabel, AvatarWidget, HyperlinkLabel, LineEdit, \
    setFont, SearchLineEdit, FluentIcon, PasswordLineEdit, PlainTextEdit, TextEdit, SpinBox, CompactSpinBox, \
    DoubleSpinBox, CompactDoubleSpinBox, TimeEdit, CompactTimeEdit, DateEdit, CompactDateEdit, DateTimeEdit, \
    CompactDateTimeEdit, TextBrowser


class TextWidget(SmoothScrollArea):
    def __init__(self, text, parent=None):
        super().__init__(parent)

        self.initWindow()
        self.initWidgets()
        self.initLayout()

        self.setObjectName(text.replace(' ', '_'))

    def initWindow(self):
        self.scrollWidget = QWidget()
        self.vLayout = VBoxLayout(self.scrollWidget)
        self.vLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)

    def initWidgets(self):
        '''
            FluentLabelBase     流畅标签
        '''

        '''小标题标签'''
        self.captionLabel = CaptionLabel('小标题标签', self)


        '''主题内容标签'''
        self.bodyLabel = BodyLabel('主体内容标签', self)

        '''强调主体内容标签'''
        self.strongBodyLabel = StrongBodyLabel("强调主体内容标签", self)

        '''子标题标签'''
        self.subTitleLabel = SubtitleLabel('子标题标签', self)

        '''标题标签'''
        self.titleLabel = TitleLabel('标题标签', self)

        '''大标题标签'''
        self.largeTitleLabel = LargeTitleLabel('大标题标签', self)

        '''巨大标题标签'''
        self.displayLabel = DisplayLabel('巨大标题标签', self)

        '''超链接标签'''
        self.linkLabel = HyperlinkLabel(QUrl('https://www.bilibili.com'), '超链接标签', self)
        # 显示下划线
        self.linkLabel.setUnderlineVisible(True)
        # 跟换链接
        # self.linkLabel.setUrl()
        setFont(self.linkLabel, 24)

        '''图像标签'''
        self.imageLabel = ImageLabel(r"C:\Users\Administrator\OneDrive\FORZA\1.png", self)
        self.imageLabel.setFixedSize(950, 600)
        # 按比例缩放到指定高度
        # self.imageLabel.scaledToHeight(300)
        # 圆角
        self.imageLabel.setBorderRadius(8, 8, 8, 8)
        self.imageLabel.setToolTip('图像标签')

        '''头像组件'''
        self.avatarWidget = AvatarWidget(r"C:\Users\Administrator\OneDrive\Pictures\30.jpg", self)
        # 设置头像半径
        self.avatarWidget.setRadius(64)
        # 如果不设置图片, 头像也可以居中显示文本首字母
        # self.avatarWidget.setText('蔡徐坤')

        '''单行编辑框'''
        self.lineEditLabel = TitleLabel('单行编辑框', self)
        self.lineEdit = LineEdit(self)
        self.lineEdit.setFixedWidth(300)
        # 设置提示内容
        self.lineEdit.setPlaceholderText('请输入文本')
        # 启用清空按钮
        self.lineEdit.setClearButtonEnabled(True)
        # 设置补全菜单
        stands = ["Star Rail", 'Genshin Impact', 'HonKai Impact']
        completer = QCompleter(stands)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setMaxVisibleItems(10)
        self.lineEdit.setCompleter(completer)
        # 自定义动作
        # 在后面添加按钮
        # self.lineEdit.addAction(
        #     QAction(FluentIcon.CALENDAR.qicon(), '', triggered=lambda: print('LineEdit'))
        # )
        # # 在前面添加按钮 @@@@@@@@@@@@@@@@
        # self.lineEdit.addAction(
        #     QAction(FluentIcon.ADD, '', triggered=lambda: print("LineEdit"))
        # )
        # 连接信号插槽
        self.lineEdit.textChanged.connect(
            lambda text: print(text)
        )

        '''搜索框'''
        self.searchEditLabel = TitleLabel('搜索框', self)
        self.searchEdit = SearchLineEdit(self)
        self.searchEdit.setPlaceholderText('请输入内容')
        self.searchEdit.setFixedWidth(300)
        self.searchEdit.textChanged.connect(
            lambda text: print(text)
        )

        '''密码输入框'''
        self.passwdEditLabel = TitleLabel('密码输入框', self)
        self.passwdEdit = PasswordLineEdit(self)
        self.passwdEdit.setPlaceholderText('请输入密码')
        self.passwdEdit.setClearButtonEnabled(True)
        self.passwdEdit.setText("123456")
        # set display password
        # self.passwdEdit.setPasswordVisible(True)
        self.passwdEdit.textChanged.connect(
            lambda passwd: print(passwd)
        )

        '''多行文本富编辑框'''
        self.textEditLabel = TitleLabel('多行文本富编辑框', self)
        self.textEdit = TextEdit(self) # TextBrowser()
        self.textEdit.setPlaceholderText("请输入文本")
        # 可以渲染HTML和Markdown格式的文本
        self.textEdit.setMarkdown('## Markdown File \n * Hello World \n * Hello Python')
        # self.textEdit.setReadOnly(True)
        self.textEdit.textChanged.connect(
            lambda: (
                print(self.textEdit.toPlainText()), # 获取普通文本
                print(self.textEdit.toMarkdown()) # 获取富文本
            )
        )

        '''多行编辑框'''
        self.plainTextEditLabel = TitleLabel('多行编辑框', self)
        self.plainTextEdit = PlainTextEdit(self)
        self.plainTextEdit.setPlaceholderText('请输入文本')
        # 不允许输入
        # self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setPlainText('Hello')
        self.plainTextEdit.textChanged.connect(
            lambda: print(self.plainTextEdit.toPlainText())
        )

        '''数字编辑框'''
        self.numberBoxLabel = TitleLabel('数字编辑框', self)
        self.numberBox = SpinBox(self)
        self.numberBox.setRange(0, 100)
        self.numberBox.valueChanged.connect(
            lambda value: print(value)
        )
        self.numberBox.setFixedWidth(150)

        '''紧凑数字编辑框'''
        self.compactNumberBoxLabel = TitleLabel('紧凑数字编辑框', self)
        self.compactNumberBox = CompactSpinBox(self)
        self.compactNumberBox.setRange(0, 10000)
        self.compactNumberBox.valueChanged.connect(
            lambda value: print(value)
        )
        self.compactNumberBox.setFixedWidth(100)

        '''浮点数编辑框'''
        self.doubleBoxLabel = TitleLabel('浮点数编辑框', self)
        self.doubleBox = DoubleSpinBox(self)
        self.doubleBox.setRange(0, 1)
        self.doubleBox.valueChanged.connect(
            lambda value: print(value)
        )
        self.doubleBox.setFixedWidth(150)

        '''紧凑浮点数编辑框'''
        self.compactDoubleBoxLabel = TitleLabel('紧凑浮点数编辑框', self)
        self.compactDoubleBox = CompactDoubleSpinBox(self)
        self.compactDoubleBox.setRange(0, 1)
        self.compactDoubleBox.valueChanged.connect(
            lambda value: print(value)
        )
        self.compactDoubleBox.setFixedWidth(100)

        '''时间编辑框'''
        self.timeEditLabel = TitleLabel('时间编辑框', self)
        self.timeEdit= TimeEdit(self)
        self.timeEdit.setTimeRange(QTime(11, 45), QTime(19, 19)) # 时 分 秒 毫秒
        self.timeEdit.setFixedWidth(150)
        self.timeEdit.timeChanged.connect(
            lambda time: print(time.toString())
        )

        '''紧凑时间编辑框'''
        self.compactTimeEditLabel = TitleLabel('紧凑时间编辑框', self)
        self.compactTimeEdit = CompactTimeEdit(self)
        self.compactTimeEdit.setTimeRange(QTime(0, 0), QTime(24, 0))
        self.compactTimeEdit.setFixedWidth(100)
        self.compactTimeEdit.timeChanged.connect(
            lambda time: print(time.toString())
        )

        '''日期编辑框'''
        self.dateEditLabel = TitleLabel('日期编辑框', self)
        self.dateEdit = DateEdit(self)
        self.dateEdit.setDateRange(QDate(2024, 1, 1), QDate(2034, 1, 1)) # 年 月 ri
        self.dateEdit.setFixedWidth(200)
        self.dateEdit.dateChanged.connect(
            lambda date: print(date.toString())
        )

        '''紧凑日期编辑框'''
        self.compactDateEditLabel = TitleLabel('日期编辑框', self)
        self.compactDateEdit = CompactDateEdit(self)
        self.compactDateEdit.setDateRange(QDate(2024, 1, 1), QDate(2034, 1, 1))  # 年 月 ri
        self.compactDateEdit.setFixedWidth(200)
        self.compactDateEdit.dateChanged.connect(
            lambda date: print(date.toString())
        )

        '''日期时间编辑框'''
        self.dateTimeEditLabel = TitleLabel('日期时间编辑框', self)
        self.dateTimeEdit = DateTimeEdit(self)
        self.dateTimeEdit.setDateRange(QDate(2024, 1, 1), QDate(2034, 1, 1))
        self.dateTimeEdit.setTimeRange(QTime(0, 0), QTime(24, 0))
        self.dateTimeEdit.setFixedWidth(250)
        self.dateTimeEdit.dateTimeChanged.connect(
            lambda e: print(e.toString())
        )

        '''紧凑日期时间编辑框'''
        self.compactDateTimeEditLabel = TitleLabel('紧凑日期时间编辑框', self)
        self.compactDateTimeEdit = CompactDateTimeEdit(self)
        self.compactDateTimeEdit.setDateRange(QDate(2024, 1, 1), QDate(2034, 1, 1))
        self.compactDateTimeEdit.setTimeRange(QTime(0, 0), QTime(24, 0))
        self.compactDateTimeEdit.setFixedWidth(200)
        self.compactDateTimeEdit.dateTimeChanged.connect(
            lambda e: print(e.toString())
        )

    def initLayout(self):
        self.vLayout.addWidget(self.captionLabel)
        self.vLayout.addWidget(self.bodyLabel)
        self.vLayout.addWidget(self.strongBodyLabel)
        self.vLayout.addWidget(self.subTitleLabel)
        self.vLayout.addWidget(self.titleLabel)
        self.vLayout.addWidget(self.largeTitleLabel)
        self.vLayout.addWidget(self.displayLabel)
        self.vLayout.addWidget(self.linkLabel)
        self.vLayout.addWidget(self.imageLabel, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.avatarWidget, 0, Qt.AlignCenter)

        self.vLayout.addWidget(self.lineEditLabel, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.lineEdit, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.searchEditLabel, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.searchEdit, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.passwdEditLabel, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.passwdEdit, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.textEditLabel, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.textEdit, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.plainTextEditLabel, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.plainTextEdit, 0, Qt.AlignCenter)

        self.vLayout.addWidget(self.numberBoxLabel, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.numberBox, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.compactNumberBoxLabel, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.compactNumberBox, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.doubleBoxLabel, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.doubleBox, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.compactDoubleBoxLabel, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.compactDoubleBox, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.timeEditLabel, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.timeEdit, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.compactTimeEditLabel, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.compactTimeEdit, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.dateEditLabel, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.dateEdit, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.compactDateEditLabel, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.compactDateEdit, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.dateTimeEditLabel, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.dateTimeEdit, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.compactDateTimeEditLabel, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.compactDateTimeEdit, 0, Qt.AlignCenter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = TextWidget("TEXT")
    w.resize(1000, 600)
    w.show()
    sys.exit(app.exec())

