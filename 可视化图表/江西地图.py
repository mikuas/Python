
import json
from pyecharts.charts import Map
from pyecharts.options import *

file_r = open("C:/疫情.txt", "r", encoding="UTF-8")

data = file_r.read()

data = json.loads(data)

dict_data = data['areaTree'][0]['children'][28]['children']

my_list = []

for i in dict_data:
    name = i['name'] + '市'
    confirm = i['total']['confirm']
    my_list.append((name, confirm))

print(my_list)


# print(type(dict_data))
# print(dict_data)
map = Map()

map.add("江西省地图", my_list, "江西")

map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {'min': 1, "max": 50, "label": "1-50人", "color": "#00F5FF"},
            {'min': 51, "max": 100, "label": "51-100人", "color": "#00EE76"},
            {'min': 101, "label": "101+人", "color": "#FFFF00"},
        ]
    )
)

map.render("江西.html")

