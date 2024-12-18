from PySide6.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QFormLayout 示例")
        self.setGeometry(100, 100, 400, 300)

        # 创建QFormLayout布局
        form_layout = QFormLayout(self)

        # 创建控件
        self.name_label = QLabel("姓名:")
        self.name_input = QLineEdit()

        self.email_label = QLabel("电子邮件:")
        self.email_input = QLineEdit()

        self.gender_label = QLabel("性别:")
        self.gender_input = QComboBox()
        self.gender_input.addItems(["男", "女", "其他"])

        self.subscribe_label = QLabel("订阅:")
        self.subscribe_input = QCheckBox("订阅我们的新闻")

        self.submit_button = QPushButton("提交")

        # 将控件添加到表单布局
        form_layout.addRow(self.name_label, self.name_input)
        form_layout.addRow(self.email_label, self.email_input)
        form_layout.addRow(self.gender_label, self.gender_input)
        form_layout.addRow(self.subscribe_label, self.subscribe_input)
        form_layout.addRow(self.submit_button)

        # 连接按钮点击事件
        self.submit_button.clicked.connect(self.submit_form)

    def submit_form(self):
        # 获取表单数据并显示
        name = self.name_input.text()
        email = self.email_input.text()
        gender = self.gender_input.currentText()
        subscribe = self.subscribe_input.isChecked()

        # 打印表单数据
        print(f"姓名: {name}")
        print(f"电子邮件: {email}")
        print(f"性别: {gender}")
        print(f"订阅: {'是' if subscribe else '否'}")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
