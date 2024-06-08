import json

from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts, TitleOpts

# map = Map()
#
# data = [
#     ('北京', 99),
#     ('上海', 199),
#     ('湖南', 399),
#     ('台湾', 199),
#     ('安徽', 299),
#     ('广州', 499),
#     ('湖北', 599)
# ]
#
# map.add("cs地图", data, "china")
#
# map.set_global_opts(
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,
#         pieces=[
#             {'min': 1, "max": 100, "label": "1-100人", "color": "#00F5FF"},
#             {'min': 101, "max": 200, "label": "101-200人", "color": "#00EE76"},
#             {'min': 201, "max": 300, "label": "201-300人", "color": "#FFFF00"},
#             {'min': 301, "label": "301+人", "color": "#FFC1C1"}
#         ]
#     )
# )
# map.render('map.html')


file_r = open("C:/疫情.txt", 'r', encoding='UTF-8')

file_r = file_r.read()

data = json.loads(file_r)

data = data['areaTree'][0]['children']

my_list = []

for l in data:
    name = l["name"]
    name = name + "省"
    num = l['total']['confirm']
    my_list.append((name, num))

print(my_list)

map = Map()

map.add("地图", my_list)

map.set_global_opts(
    title_opts=TitleOpts(title="地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
                {'min': 1, "max": 900, "label": "1-900人", "color": "#00F5FF"},
                {'min': 901, "max": 2000, "label": "901-2000人", "color": "#00EE76"},
                {'min': 2001, "max": 3000, "label": "2001-3000人", "color": "#FFFF00"},
                {'min': 3001, "label": "3001+人", "color": "#FFC1C1"}
        ]
    )
)

map.render("疫情地图.html")
