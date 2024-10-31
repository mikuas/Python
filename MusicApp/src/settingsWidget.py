from PySide6.QtWidgets import QWidget, QVBoxLayout, QSlider, QLabel
from PySide6.QtCore import Qt

from PyMyMethod.Method import SystemCtl


class SetWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(400)

        layout = QVBoxLayout(self)
        slider = QSlider(Qt.Orientation.Horizontal, self)
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setValue(SystemCtl().getAudioEndpointVolume()[1] * 100 + 0.1)

        slider.valueChanged.connect(lambda: (
            objLab[-1].setText(str(f"当前音量: {slider.value()}")),
            SystemCtl().setAudio(slider.value() / 100)
        ))

        labs = ["设置音量", f'当前音量: {slider.value()}']
        objLab = []

        layout.addWidget(slider)
        for lab in labs:
            label = QLabel(lab, self)
            label.setStyleSheet('font-size: 24px')
            layout.addWidget(label)
            objLab.append(label)