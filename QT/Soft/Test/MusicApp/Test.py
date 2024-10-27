from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QCheckBox, QApplication, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class SettingsRow(QWidget):
    def __init__(self):
        super().__init__()

        # 创建布局
        layout = QHBoxLayout(self)

        # 创建图标
        icon_label = QLabel(self)
        pixmap = QPixmap('play_icon.png')  # 假设你有一个播放图标
        icon_label.setPixmap(pixmap.scaled(30, 30, Qt.KeepAspectRatio))

        # 创建标题和描述的垂直布局
        text_layout = QVBoxLayout()
        title_label = QLabel("启动音频")
        description_label = QLabel("设置程序启动时的音频播放")
        description_label.setStyleSheet("color: gray; font-size: 10px;")
        text_layout.addWidget(title_label)
        text_layout.addWidget(description_label)

        # 创建开关按钮（QCheckBox 作为示例）
        toggle_switch = QCheckBox()
        toggle_switch.setChecked(True)  # 默认打开
        toggle_switch.setText("On")

        # 将组件添加到布局
        layout.addWidget(icon_label)
        layout.addLayout(text_layout)
        layout.addStretch()  # 添加一个伸缩因子，保证开关按钮靠右
        layout.addWidget(toggle_switch)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication([])
    window = SettingsRow()
    window.show()
    app.exec()
