import sys

from PySide6.QtWidgets import QApplication
from qfluentwidgets import FluentIcon

from QtFluentWidgets.FluentWidgetModule.FluentWidgets import SliderCard, VerticalScrollWidget


class Demo(VerticalScrollWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.slider = SliderCard(
            FluentIcon.VOLUME,
            'SliderCard',
            '',
            0,
            100,
            10,
            parent=self
        )
        self.slider.setFixedWidth(self.width() - 20)
        self.vBoxLayout.addWidget(self.slider)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec())