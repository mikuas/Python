from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QListWidget,
    QListWidgetItem,
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class MusicItemWidget(QWidget):
    def __init__(self, song_data, parent=None):
        super().__init__(parent)
        self.song_data = song_data

        # 图片
        self.image_label = QLabel()
        pixmap = QPixmap(song_data["image"]).scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(pixmap)
        self.image_label.setFixedSize(50, 50)

        # 歌曲信息
        self.title_label = QLabel(song_data["name"])
        self.title_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        self.artist_label = QLabel(song_data["artist"])
        self.artist_label.setStyleSheet("color: gray; font-size: 12px;")

        # 播放按钮
        self.play_button = QPushButton("▶")
        self.play_button.setFixedSize(30, 30)
        self.play_button.setStyleSheet(
            """
            QPushButton {
                border: 1px solid lightgray;
                border-radius: 15px;
                background-color: white;
            }
            QPushButton:hover {
                background-color: lightblue;
            }
            """
        )
        self.play_button.clicked.connect(self.play_song)

        # "我喜欢" 按钮
        self.favorite_button = QPushButton("❤" if song_data["favorite"] else "♡")
        self.favorite_button.setFixedSize(30, 30)
        self.favorite_button.setStyleSheet(
            """
            QPushButton {
                border: none;
                font-size: 18px;
                color: red;
                background: transparent;
            }
            QPushButton:hover {
                font-size: 20px;
            }
            """
        )
        self.favorite_button.clicked.connect(self.toggle_favorite)

        # 布局
        text_layout = QVBoxLayout()
        text_layout.addWidget(self.title_label)
        text_layout.addWidget(self.artist_label)

        button_layout = QVBoxLayout()
        button_layout.addWidget(self.play_button)
        button_layout.addWidget(self.favorite_button)

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.image_label)
        main_layout.addLayout(text_layout)
        main_layout.addLayout(button_layout)
        main_layout.setContentsMargins(5, 5, 5, 5)

        self.setLayout(main_layout)

    def play_song(self):
        print(f"正在播放: {self.song_data['name']}")

    def toggle_favorite(self):
        self.song_data["favorite"] = not self.song_data["favorite"]
        self.favorite_button.setText("❤" if self.song_data["favorite"] else "♡")
        print(f"更新喜欢状态: {self.song_data['name']} -> {self.song_data['favorite']}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("嵌入小部件的 QListWidget")

        # 数据
        self.data = [
            {"name": "Song 1", "artist": "Artist 1", "image": "song1.png", "favorite": False},
            {"name": "Song 2", "artist": "Artist 2", "image": "song2.png", "favorite": True},
            {"name": "Song 3", "artist": "Artist 3", "image": "song3.png", "favorite": False},
        ]

        # 列表视图
        self.list_widget = QListWidget(self)

        for song in self.data:
            item = QListWidgetItem()
            widget = MusicItemWidget(song)
            item.setSizeHint(widget.sizeHint())
            self.list_widget.addItem(item)
            self.list_widget.setItemWidget(item, widget)

        self.setCentralWidget(self.list_widget)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(400, 300)
    window.show()
    sys.exit(app.exec())
