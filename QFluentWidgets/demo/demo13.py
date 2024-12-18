import sys

from PySide6.QtWidgets import QApplication, QWidget
from qfluentwidgets import TitleLabel, FluentIcon, FolderListSettingCard, ConfigItem, FolderListValidator, \
    ExpandSettingCard, PushButton

from QtFluentWidgets.FluentWidgetModule.FluentWidgets import FluentWindow, VBoxLayout


class Demo(FluentWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(800, 520)
        self.vBoxLayout.addWidget(TitleLabel("Bottom", self))
        self.widget = QWidget(self)
        self.widget.setObjectName("widget")
        self.vBoxLayout.addWidget(self.widget)
        self.vLayout = VBoxLayout(self.widget)
        self.customFolder = ExpandSettingCard(
            FluentIcon.DOWN,
            '本地音乐库',
            '',
            self
        )
        self.toolButton = PushButton(FluentIcon.FOLDER_ADD, '添加文件夹', self)
        self.customFolder.addWidget(self.toolButton)
        self.folder = FolderListSettingCard(
            ConfigItem("Folders", "LocalMusic", '', FolderListValidator()),
            "本地音乐库",
            "",
            '',
            self
        )
        self.vLayout.addWidget(self.folder)
        self.vLayout.addWidget(self.customFolder)

        self.addSubInterface(
            self.widget,
            FluentIcon.HOME,
            'Home'
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Demo()
    window.show()
    sys.exit(app.exec())