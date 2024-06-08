from PySide6.QtWidgets import *
import sys


class RepeatDataClear:
    def __init__(self, file_path, save_path):
        self.file_path = file_path
        self.save_path = save_path

    def file_read(self) -> list:
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                element = file.readlines()
                if '\n' not in element[-1]:
                    element[-1] += '\n'
                return element
        except Exception as e:
            print(f'文件不存在:{e}')
            return []

    @staticmethod
    def clear_repeat(data) -> list:
        try:
            data = set(data)
            data.remove('\n')
            return list(data)
        except Exception as e:
            print(f'传入的文件为空:{e}')
            return []

    def file_write(self, data):
        if data:
            try:
                with open(self.save_path, 'w', encoding='utf-8') as file:
                    for line in data:
                        file.write(line)
                print('执行完毕')
            except Exception as e:
                print(e)
        else:
            print('没有数据可写入')


class Stats:
    def __init__(self, win_width, win_height, apptitle):
        # 创建主窗口对象
        self.window = QMainWindow()
        self.window.setWindowTitle(apptitle)
        self.window.setGeometry(100, 100, win_width, win_height)

        # 创建中心部件和布局
        central_widget = QWidget()
        self.window.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 创建QPlainTextEdit并确保正确初始化
        self.text_edit = QPlainTextEdit()
        print(f'text_edit type: {type(self.text_edit)}')  # 添加调试信息
        layout.addWidget(self.text_edit)

        self.win_width = win_width
        self.win_height = win_height
        self.window_two = QWidget()  # 更改为QWidget
        self.text = QPlainTextEdit(self.window_two)
        print(f'text type: {type(self.text)}')  # 添加调试信息

        self.file_path = None
        self.save_path = None

        self.box = QMessageBox(self.window)
        self.info = QMessageBox(self.window)

        # 设置按钮
        self.button = QPushButton('执行', self.window)
        self.button.move(win_width * 0.6, win_height * 0.3)
        # 设置按钮大小
        self.button.setFixedSize(100, 50)

        self.file_read_button = QPushButton('选择读取的文件', self.window)
        self.file_read_button.move(20, 50)
        self.file_read_button.setFixedSize(150, 50)

        self.file_save_button = QPushButton('选择保存路径', self.window)
        self.file_save_button.move(20, 130)
        self.file_save_button.setFixedSize(150, 50)

        # 按钮点击事件
        self.button.clicked.connect(self.handle_calculate)
        self.file_read_button.clicked.connect(self.open_file)
        self.file_save_button.clicked.connect(self.save_file)

    def handle_calculate(self):
        # 检查是否选择了文件路径
        if not self.file_path or not self.save_path:
            self.show_error_message("文件路径未选择", "请选择文件路径后再执行。")
            return

        try:
            repeat = RepeatDataClear(self.file_path, self.save_path)
            repeat.file_write(repeat.clear_repeat(repeat.file_read()))
            self.info.setText('执行完毕!')
            self.info.show()
        except Exception as e:
            self.show_error_message("执行错误", str(e))

    def open_file(self):
        file_dialog = QFileDialog()
        self.file_path, _ = file_dialog.getOpenFileName(self.window, "选择文件", "", "Text files (*.txt);;All files (*)")

    def save_file(self):
        file_dialog = QFileDialog()
        self.save_path, _ = file_dialog.getSaveFileName(self.window, "选择保存路径", "", "Text files (*.txt);;All files (*)")

    def show_error_message(self, title, message):
        error_msg = QMessageBox(self.window)
        error_msg.setIcon(QMessageBox.Critical)
        error_msg.setWindowTitle(title)
        error_msg.setText(message)
        error_msg.setStandardButtons(QMessageBox.Ok)
        error_msg.exec()


def main():
    app = QApplication(sys.argv)
    stats = Stats(500, 250, "应用程序")
    stats.window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
