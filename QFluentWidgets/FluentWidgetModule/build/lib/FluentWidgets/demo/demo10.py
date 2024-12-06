from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPainter, QColor, QImage, QBrush, QPixmap
from PySide6.QtWidgets import QWidget, QApplication, QGraphicsBlurEffect
import sys

class AcrylicWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Transparent Acrylic Effect")
        self.setGeometry(100, 100, 800, 600)

        # 设置窗口为透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)  # 使窗口背景透明

        # 默认设置模糊半径，色调和亮度
        self.blurRadius = 30
        self.tintColor = QColor(255, 255, 255, 180)  # 白色色调
        self.luminosityColor = QColor(255, 255, 255, 50)  # 亮度
        self.noiseOpacity = 0.05  # 噪点透明度


        # 使用 QGraphicsBlurEffect 为窗口设置模糊效果
        self.blurEffect = QGraphicsBlurEffect()
        self.blurEffect.setBlurRadius(self.blurRadius)
        self.setGraphicsEffect(self.blurEffect)

    def paintEvent(self, event):
        """绘制透明窗口的背景以及亚力克效果"""
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

        # 绘制透明的背景和亚力克效果
        self.drawAcrylicBackground(painter)

        # 绘制色调、亮度和噪点
        self.paintAcrylicEffect(painter)

    def drawAcrylicBackground(self, painter: QPainter):
        """绘制透明的窗口背景"""
        # 在窗口上绘制一个透明的色调背景
        backgroundColor = QColor(255, 255, 255, 150)  # 半透明白色背景
        painter.fillRect(self.rect(), backgroundColor)

        # 添加透明效果来模拟亚力克的磨砂玻璃效果
        painter.setOpacity(0.5)  # 设置透明度
        painter.fillRect(self.rect(), QColor(255, 255, 255, 100))  # 半透明的白色层

    def paintAcrylicEffect(self, painter: QPainter):
        """绘制亚力克效果的色调、亮度和噪点"""

        # 绘制色调
        painter.setOpacity(self.tintColor.alpha() / 255.0)

        # 绘制噪点
        painter.setOpacity(self.noiseOpacity)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = AcrylicWidget()
    window.show()

    sys.exit(app.exec())
