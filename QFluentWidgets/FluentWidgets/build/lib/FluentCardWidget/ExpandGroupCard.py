from PySide6.QtGui import Qt
from qfluentwidgets import TitleLabel, PushButton, PrimaryPushButton, TransparentPushButton, Slider, CaptionLabel
from .CustomWidget import ExpandGroupCard


class ExpandGroupCard(ExpandGroupCard):
    """展开按钮卡片"""
    def __init__(self, icon, title, content, parent=None):
        super().__init__(icon, title, content, parent)
        self.card.setContentsMargins(0, 0, 20, 0)
        self.viewLayout.setSpacing(0)
        self.setCardMinHeight(80)

    def setCardMinHeight(self, height):
        self.card.setFixedHeight(height)

    def addGroupWidgets(self, widgets):
        for widget in widgets:
            self.addGroupWidget(widget)

    def addButtonCard(self, title, icon, text, __type=None):
        hLayout = self._initWidget()
        hLayout.addWidget(TitleLabel(title, self))
        button = PushButton(icon, text, self)
        button.setFixedWidth(120)
        hLayout.addStretch(1)
        hLayout.addWidget(button, 0, Qt.AlignmentFlag.AlignRight)

        return button

    def addPrimaryButtonCard(self, title, icon, text):
        return self.addButtonCard(title, icon, text, PrimaryPushButton)

    def addTransparentButtonCard(self, title, icon, text):
        return self.addButtonCard(title, icon, text, TransparentPushButton)

    def addSliderCard(self, title, ranges, defaultValue, orientation=Qt.Orientation.Horizontal):
        slider = Slider(orientation, self)
        slider.setRange(ranges[0], ranges[1])
        slider.setValue(defaultValue)
        slider.setFixedWidth(250)
        label = CaptionLabel(str(slider.value()), self)

        hLayout = self._initWidget()
        hLayout.addWidget(label)
        hLayout.addStretch(1)
        hLayout.addWidget(label, 0, Qt.AlignmentFlag.AlignRight)
        hLayout.addWidget(slider, 0, Qt.AlignmentFlag.AlignRight)

        slider.valueChanged.connect(
            lambda: label.setText(str(slider.value()))
        )

        return slider

    def setAllCardHeight(self):
        pass