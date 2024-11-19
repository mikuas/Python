from PySide6.QtGui import Qt
from qfluentwidgets import Slider, CaptionLabel

from ...widgetdoc import SliderCardParent
from ..cards import CustomCard


class SliderCard(SliderCardParent, CustomCard):
    """ 滑动条卡片 """
    def __init__(self, icon, title, content, ranges, defaultValue=0, orientation=Qt.Orientation.Horizontal, parent=None):
        CustomCard.__init__(self, parent=parent)
        self.initIcon(icon).initTitle(title).initContent(content).initLayout()
        self.initSliderLabel(defaultValue).initSlider(ranges, defaultValue, orientation)

    def initSlider(self, ranges, value, orientation=Qt.Orientation.Horizontal):
        self.slider = Slider(orientation, self)
        self.slider.setRange(ranges[0], ranges[1])
        self.slider.setFixedWidth(200)
        self.slider.setValue(value)
        self.slider.valueChanged.connect(
            lambda: self.sliderLabel.setText(str(self.slider.value()))
        )
        self.hBoxLayout.addWidget(self.slider, 0, Qt.AlignmentFlag.AlignRight)
        return self

    def initSliderLabel(self, value):
        self.sliderLabel = CaptionLabel(str(value), self)
        self.hBoxLayout.addWidget(self.sliderLabel, 0, Qt.AlignmentFlag.AlignRight)
        return self