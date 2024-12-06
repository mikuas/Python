from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QScrollArea, QLabel, QPushButton
from PySide6.QtCore import Qt, QTimer

class LyricsDisplay(QWidget):
    def __init__(self):
        super().__init__()

        # 主布局
        self.layout = QVBoxLayout(self)

        # 滚动区域，用来显示歌词
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.lyrics_widget = QWidget(self)
        self.lyrics_layout = QVBoxLayout(self.lyrics_widget)

        # 添加滚动区域
        self.scroll_area.setWidget(self.lyrics_widget)
        self.layout.addWidget(self.scroll_area)

        # 初始歌词列表
        self.lyrics = [
            "Lyric 1: Starting song...",
            "Lyric 2: Getting closer...",
            "Lyric 3: Feeling the beat...",
            "Lyric 4: Almost there...",
            "Lyric 5: Here we go!",
            "Lyric 1: Starting song...",
            "Lyric 2: Getting closer...",
            "Lyric 3: Feeling the beat...",
            "Lyric 4: Almost there...",
            "Lyric 1: Starting song...",
            "Lyric 2: Getting closer...",
            "Lyric 3: Feeling the beat...",
            "Lyric 4: Almost there...",
            "Lyric 1: Starting song...",
            "Lyric 2: Getting closer...",
            "Lyric 3: Feeling the beat...",
            "Lyric 4: Almost there...",
        ]

        # 当前显示的歌词索引
        self.current_index = 0

        # 用于显示歌词的标签列表
        self.lyric_labels = []

        # 创建标签并添加到布局
        self.create_lyrics()

        # 创建按钮来控制显示的歌词
        self.button = QPushButton("Start Lyrics", self)
        self.button.clicked.connect(self.start_lyrics)
        self.layout.addWidget(self.button)

        # 定时器，用于模拟歌词播放
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_lyric)
        self.timer.setInterval(1000)  # 每秒更新一次歌词

        self.setLayout(self.layout)
        self.setWindowTitle("Lyrics Display")
        self.resize(400, 300)

    def create_lyrics(self):
        """创建所有歌词的标签并添加到布局"""
        for lyric in self.lyrics:
            label = QLabel(lyric, self)
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("font-size: 20px; padding: 5px;")
            self.lyric_labels.append(label)
            self.lyrics_layout.addWidget(label)

    def update_lyric(self):
        """更新当前歌词并高亮显示"""
        if self.current_index < len(self.lyric_labels):
            # 清除之前高亮的歌词
            for i, label in enumerate(self.lyric_labels):
                if i == self.current_index:
                    label.setStyleSheet("font-size: 20px; color: red; padding: 5px;")  # 高亮当前歌词
                else:
                    label.setStyleSheet("font-size: 20px; padding: 5px;")  # 恢复非当前歌词的样式

            # 滚动到当前歌词
            self.scroll_to_center(self.current_index)

            # 更新歌词索引
            self.current_index += 1

            # 如果播放完所有歌词，停止定时器
            if self.current_index >= len(self.lyric_labels):
                self.timer.stop()

    def start_lyrics(self):
        """开始播放歌词"""
        self.current_index = 0  # 重置歌词索引
        self.timer.start()  # 启动定时器

    def scroll_to_center(self, index):
        """将当前歌词滚动到中心位置"""
        # 获取当前歌词标签
        label = self.lyric_labels[index]

        # 获取标签的位置和高度
        label_pos = self.lyrics_layout.indexOf(label)
        label_height = label.sizeHint().height()
        print(label_height)

        # 获取滚动区域的可见高度
        scroll_area_height = self.scroll_area.viewport().height()

        # 计算要滚动的位置，使当前歌词居中
        scroll_bar = self.scroll_area.verticalScrollBar()
        scroll_position = (label_pos * label_height) - (scroll_area_height // 2) + (label_height // 2)

        # 滚动到该位置
        scroll_bar.setValue(scroll_position)

app = QApplication([])
window = LyricsDisplay()
window.show()
app.exec()
