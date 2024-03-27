import json
from pyecharts.charts import Map
from pyecharts.options import *
file = open("C:/疫情.txt", 'r', encoding='UTF-8')

data = file.read()

data = json.loads(data)

# 取到河南省每个市的数据
data = data['areaTree'][0]['children'][3]['children']

# print(data)
# data = data['name']
my_list = []


for line in data:
    # for 循环，通过Key取出对应的Value
    name = line['name'] + '市'
    # 取得人数
    confirm = line['total']['confirm']
    # 封装进列表里
    my_list.append((name, confirm))
# for i in data:
#     # print(i)
#     name = data['children']
#     for line in name:
#         name = line['name'] + '市'
#         confirm = line['total']['confirm']
#         my_list.append((name, confirm))
    # num = i['total']['confirm']
    # my_list.append((name, num))


# print(my_list)
my_list.append(('济源市', 5))

map = Map()

map.add("河南省地图", my_list, "河南")

map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {'min': 1, "max": 90, "label": "1-90人", "color": "#00F5FF"},
            {'min': 91, "max": 200, "label": "91-200人", "color": "#00EE76"},
            {'min': 201, "max": 300, "label": "201-300人", "color": "#FFFF00"},
            {'min': 301, "label": "301+人", "color": "#FFC1C1"},
        ]
    )
)
map.render('河南.html')







