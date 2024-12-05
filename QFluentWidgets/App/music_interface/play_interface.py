from FluentWidgets import HBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from qfluentwidgets import ImageLabel, BodyLabel


class PlayWidget(QWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent)
        self.setObjectName(text.replace(" ", "_"))
        self.hLayout = HBoxLayout(self)
        with open(r"C:\Projects\Items\Python\QFluentWidgets\App\data\music\Bad Apple!!\Bad Apple!!.lrc", 'r', encoding='utf-8') as f:
            data = f.readlines()
        for i in data:
            print(i.replace('\n', ''))

        self.imageLabel = ImageLabel(r"C:\Projects\Items\Python\QFluentWidgets\App\data\music\Bad Apple!!\Bad Apple!!.jpg", self)
        self.bodyLabel = BodyLabel("暂无歌词信息", self)
        self.initLayout()
        self.initImgLabel()

    def initImgLabel(self):
        self.imageLabel.setBorderRadius(128, 128, 128, 128)
        self.imageLabel.setFixedSize(256, 256)
        self.imageLabel.move(120, int(self.height() / 2))

    def initLayout(self):
        self.hLayout.addWidget(self.imageLabel)
        self.hLayout.addWidget(self.bodyLabel, alignment=Qt.AlignmentFlag.AlignHCenter)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.imageLabel.move(120, int(self.height() / 2.8))