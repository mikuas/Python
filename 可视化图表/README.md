# 可视化图表(Pyecharts)

### 折线图

~~~python
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, VisualMapOpts, TooltipOpts, LabelOpts

# 得到折线图对象 line = Line()
line = Line()

# 添加x轴数据line.add_xaxis
line.add_xaxis(["中国", "美国", "英国"])
# 添加y轴数据line.add_yaxis
line.add_yaxis("GDP", [100, 20, 10])

'''
全局配置: set_global_opts
title_opts = TitleOpts(title="标题名称", pos_left="位置", pos_bottom="上下")
legend_opts = LegendOpts(is_show=True/False) 图例
tooltip_opts = LegendOpts(is_show=True/False) 工具箱
visualmap_opts = VisualMapOpts(is_show=True/False) 视觉映射
'''
~~~

### 地图

~~~python
import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts, TitleOpts

map = Map()

data = [
    ('北京', 99),
    ('上海', 199),
    ('湖南', 399),
    ('台湾', 199),
    ('安徽', 299),
    ('广州', 499),
    ('湖北', 599)
]

map.add("cs地图", data, "china")

map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {'min': 1, "max": 100, "label": "1-100人", "color": "#00F5FF"},
            {'min': 101, "max": 200, "label": "101-200人", "color": "#00EE76"},
            {'min': 201, "max": 300, "label": "201-300人", "color": "#FFFF00"},
            {'min': 301, "label": "301+人", "color": "#FFC1C1"}
        ]
    )
)
map.render('map.html')
~~~

### 动态柱状图

~~~python
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import *

bar = Bar()
# 添加x轴数据
bar.add_xaxis(['中国', '美国', '英国'])
# 添加y轴数据
bar.add_yaxis('GDP', [100, 20, 10], label_opts=LabelOpts(
    position='right'    # 设置数值标签在右侧
))
# 反转xy轴
bar.reversal_axis()

# 生成 
bar.render("基础柱状图.html")

### 时间线柱状图
Timeline()
### 通过时间线绘图
# timeline.render(name)
~~~


























