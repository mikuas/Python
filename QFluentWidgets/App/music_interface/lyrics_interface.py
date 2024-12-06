from FluentWidgets import HBoxLayout, VerticalScrollWidget
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from qfluentwidgets import ImageLabel, SubtitleLabel, TitleLabel


class LyricsInterface(QWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent)
        self.setObjectName(text.replace(" ", "_"))
        self.lyricsWidget = VerticalScrollWidget(self)
        self.hLayout = HBoxLayout(self)
        self.imageLabel = ImageLabel(r"C:\Projects\Items\Python\QFluentWidgets\App\data\music\Bad Apple!!\Bad Apple!!.jpg", self)

        self.setLyrics(r"C:\Projects\Items\Python\QFluentWidgets\App\data\music\Bad Apple!!\Bad Apple!!.lrc")
        self.lyricsWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.initLayout()
        self.initImgLabel()

    def setLyrics(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            f = f.readlines()
        self.clearWidget()
        print("Set Lyrics")
        title = f[0].split(']')[-1].split('-')
        for t in title:
            self.lyricsWidget.vBoxLayout.addWidget(
                TitleLabel(t, self),
                alignment=Qt.AlignmentFlag.AlignHCenter
            )
        for item in f[1::]:
            item = item.replace('\n', '').split(']')[-1]
            if len(item) > 40:
                item = item[40::]
                self.lyricsWidget.vBoxLayout.addWidget(
                    SubtitleLabel(item, self),
                    alignment=Qt.AlignmentFlag.AlignHCenter
                )
            else:
                self.lyricsWidget.vBoxLayout.addWidget(
                    SubtitleLabel(item, self),
                    alignment=Qt.AlignmentFlag.AlignHCenter
                )

    def clearWidget(self):
        print("Clear Widget")
        while self.lyricsWidget.vBoxLayout.count():
            item = self.lyricsWidget.vBoxLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

    def initImgLabel(self):
        self.imageLabel.setContentsMargins(100, 0, 0, 0)
        self.imageLabel.setBorderRadius(64, 64, 64, 64)
        self.imageLabel.setFixedSize(256, 256)
        self.imageLabel.move(int(self.width() / 3), int(self.height() / 2))

    def setImageLabelPath(self, path):
        self.imageLabel.setImage(path)
        self.initImgLabel()

    def initLayout(self):
        self.hLayout.addWidget(self.imageLabel, 1, alignment=Qt.AlignmentFlag.AlignHorizontal_Mask)
        self.hLayout.addWidget(self.lyricsWidget, 2, alignment=Qt.AlignmentFlag.AlignHCenter)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.lyricsWidget.setFixedWidth(self.width() / 1.5)