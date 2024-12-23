import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWebEngineWidgets import QWebEngineView
from pyecharts.charts import Bar
from pyecharts.faker import Faker
import pyecharts.options as opts

class stats(QWidget):
    def __init__(self):
        super(stats,self).__init__()
        self.initUI()
    def initUI(self):#绘图pyecharts
        self.setWindowTitle("示例1")
        self.setGeometry(100,100,600,500)
        layout = QHBoxLayout()
        self.scrolla=QScrollArea()
        self.button=QPushButton('绘图')
        layout.addWidget(self.scrolla)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.button.clicked.connect(self.huitu)
    def huitu(self):
        bro = QWebEngineView()
        c = (Bar().add_xaxis(Faker.days_attrs).add_yaxis(
            "商家A", Faker.days_values).set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-水平）"),
            datazoom_opts=opts.DataZoomOpts(),
        ))
        bro.setHtml(c.render_embed())
        self.scrolla.setWidget(bro)

def main(self):
    app = QApplication(sys.argv)
    main = self()
    main.show()
    exit(app.exec_())

if __name__ == "__main__":
    main(stats)