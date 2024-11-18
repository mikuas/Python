from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout
from qfluentwidgets import TitleLabel, PushButton, PrimaryPushButton, TransparentPushButton, Slider, CaptionLabel
from .CustomWidget.CustomCard import CustomExpandGroupCard


class ExpandGroupCard(CustomExpandGroupCard):
    """展开按钮卡片"""
    def __init__(self, icon, title, content, parent=None):
        super().__init__(icon, title, content, parent)
        self.card.setContentsMargins(0, 0, 20, 0)
        self.viewLayout.setSpacing(0)
        self.setExpandFixedHeight(80)

    def setExpandFixedHeight(self, height):
        self.card.setFixedHeight(height)
        self.setFixedHeight(self.card.height())
        self.setViewportMargins(0, self.card.height(), 0, 0)
        return self

    def addGroupWidgets(self, widgets):
        for widget in widgets:
            self.addGroupWidget(widget)
        return self

    def __initButton(self, title, icon, text, parent=None, btType=None):
        hLayout = self._initWidget()
        hLayout.addWidget(TitleLabel(title, parent))
        button = btType(icon, text, parent)
        button.setFixedWidth(120)
        hLayout.addStretch(1)
        hLayout.addWidget(button, 0, Qt.AlignmentFlag.AlignRight)

    def addButtonCard(self, title, icon, text, parent=None):
        return self.__initButton(title, icon, text, parent, PushButton)

    def addPrimaryButtonCard(self, title, icon, text, parent=None):
        return self.__initButton(title, icon, text, parent, PrimaryPushButton)

    def addTransparentButtonCard(self, title, icon, text, parent=None):
        return self.__initButton(title, icon, text, parent, TransparentPushButton)

    def addSliderCard(self, title, ranges, defaultValue, orientation=Qt.Orientation.Horizontal, parent=None):
        slider = Slider(orientation, parent)
        slider.setRange(ranges[0], ranges[1])
        slider.setValue(defaultValue)
        slider.setFixedWidth(250)
        label = CaptionLabel(str(slider.value()), parent)

        hLayout = self._initWidget()
        hLayout.addWidget(label)
        hLayout.addStretch(1)
        hLayout.addWidget(label, 0, Qt.AlignmentFlag.AlignRight)
        hLayout.addWidget(slider, 0, Qt.AlignmentFlag.AlignRight)

        slider.valueChanged.connect(
            lambda: label.setText(str(slider.value()))
        )

        return slider

    def _initWidget(self):
        window = QWidget()
        window.setFixedHeight(65)
        hLayout = QHBoxLayout(window)
        hLayout.setContentsMargins(48, 12, 48, 12)
        self.addGroupWidget(window)

        return hLayout