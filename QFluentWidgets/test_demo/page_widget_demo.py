import sys

from PySide6.QtWidgets import QWidget, QApplication

from qfluentwidgets import TitleLabel, PrimaryPushButton, ComboBox

from QtFluentWidgets.FluentWidgetModule.FluentWidgets import HorizontalPagerWidget, VBoxLayout


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 520)
        self.number = 4
        self.vLayout = VBoxLayout(self)

        self.button = PrimaryPushButton("Delete Page", self)
        self.addButton = PrimaryPushButton("Add Page", self)
        self.comboBox = ComboBox(self)
        self.comboBox.setCurrentIndex(-1)
        self.comboBox.setPlaceholderText("选择要删除页数的下标")

        self.pager = HorizontalPagerWidget(self)
        for _ in range(self.number):
            title = TitleLabel(f"Pager {_}", self)
            self.pager.addWidget(title)

        self.pager.setVisibleNumber(50)

        self.pager.setStyleSheet('background-color: skyblue')
        self.pager.hoverDisplayNextButton().hoverDisplayPrevButton()
        self.updateComboBox()

        self.vLayout.addWidgets([self.pager, self.button, self.comboBox, self.addButton])

        self.button.clicked.connect(
            lambda: (
                self.pager.removeWidget(int(self.comboBox.currentText())),
                self.updateComboBox()
            )
        )
        self.addButton.clicked.connect(
            lambda: (
                self.pager.addWidget(TitleLabel(f"Page {self.number}", self)),
                self.updateNumber(1),
                self.updateComboBox()
            )
        )

    def updateNumber(self, number: int):
        self.number += number

    def updateComboBox(self):
        self.comboBox.clear()
        self.comboBox.addItems([str(number) for number in range(self.pager.getPageNumber())])

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # self.pager.setFixedSize(self.size())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Demo()
    window.show()
    sys.exit(app.exec())