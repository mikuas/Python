import sys
from PySide6.QtWidgets import QWidget, QHBoxLayout, QApplication

from qfluentwidgets import ExpandGroupSettingCard, FluentIcon, PrimaryPushButton, PrimaryToolButton, ToolButton, \
BodyLabel, Theme, setTheme


class ServerCard(ExpandGroupSettingCard):

    def __init__(self, parent=None):
        super().__init__(FluentIcon.SHARE, "服务器", "配置流媒体服务器", parent)
        self.addButton = PrimaryPushButton(FluentIcon.ADD, "添加服务器")
        self.addWidget(self.addButton)
        self.addButton.clicked.connect(self.addServerCard)

    def addServerCard(self):
        item = ServerItem(self)
        item.removeButton.clicked.connect(lambda: self.removeServerCard(item))
        self.addGroupWidget(item)

    def removeServerCard(self, card):
        self.removeGroupWidget(card)
        card.hide()
        card.deleteLater()


class ServerItem(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.addButton = PrimaryToolButton(FluentIcon.EDIT, self)
        self.removeButton = ToolButton(FluentIcon.DELETE, self)

        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.addWidget(BodyLabel("服务器"))
        self.hBoxLayout.addStretch(1)
        self.hBoxLayout.addWidget(self.addButton)
        self.hBoxLayout.addWidget(self.removeButton)

        self.hBoxLayout.setContentsMargins(20, 12, 20, 12)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ServerItem()
    setTheme(Theme.AUTO)
    w.show()
    app.exec()