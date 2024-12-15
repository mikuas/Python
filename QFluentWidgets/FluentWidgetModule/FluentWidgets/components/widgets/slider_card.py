# coding:utf-8
from typing import Union

from PySide6.QtGui import Qt, QIcon
from qfluentwidgets import Slider, CaptionLabel, FluentIconBase

from .custom_card import CardBase


class SliderCard(CardBase):
    """ 滑动条卡片 """
    def __init__(
            self, icon: Union[QIcon, str, FluentIconBase], title: str, content: str,
            minValue: int, maxValue: int, defaultValue=0, orientation=Qt.Orientation.Horizontal, parent=None
    ):
        super().__init__(parent=parent)
        self.initIcon(icon).initTitle(title).initContent(content).initLayout()
        self.initSliderLabel(defaultValue)
        self.initSlider(minValue, maxValue, defaultValue, orientation)

    def initSlider(self, minValue: int, maxValue: int, value: int, orientation=Qt.Orientation.Horizontal):
        self.slider = Slider(orientation, self)
        self.slider.setRange(minValue, maxValue)
        self.slider.setFixedWidth(200)
        self.slider.setValue(value)
        self.slider.valueChanged.connect(lambda: self.sliderLabel.setText(str(self.slider.value())))
        self.hBoxLayout.addWidget(self.slider, 0, Qt.AlignmentFlag.AlignRight)

    def initSliderLabel(self, value: int):
        self.sliderLabel = CaptionLabel(str(value), self)
        self.hBoxLayout.addWidget(self.sliderLabel, 0, Qt.AlignmentFlag.AlignRight)
