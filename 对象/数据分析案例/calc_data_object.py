from record import Record
from read_file import FileReader, TextFileReader, JsonFileReader
from pyecharts.charts import Bar
from pyecharts.options import *
from typing import Union

text_file_reader = TextFileReader("C:/2011年1月销售数据.txt")

json_file_reader = JsonFileReader("C:/2011年2月销售数据JSON.txt")

jan_data: list[Record] = text_file_reader.file_read()
feb_data: list[Record] = json_file_reader.file_read()

all_data_list: list[Record] = jan_data + feb_data

money = {}

for record in all_data_list:
    # 通过if判断date在不在money的keys里
    if record.date in money.keys():
        # 当前日期有了，所以和老记录累加即可
        money[record.date] += record.money
        # 没有就进行赋值
    else:
        money[record.date] = record.money


def for_dict(_object: dict) -> Union[list, list]:
    x_list: list = []
    y_list: list = []

    for key in _object:
        x_list.append(key)
        y_list.append(_object[key])

    return x_list, y_list


bar = Bar()

x_object, y_object = for_dict(money)

bar.add_xaxis(x_object)
bar.add_yaxis('销售额', y_object, label_opts=LabelOpts(is_show=False))

bar.set_global_opts(
    title_opts=TitleOpts(title='每日销售额'),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {'min': 1, "max": 10000, "label": "1-10000人", "color": "#00F5FF"},
            {'min': 10001, "max": 30000, "label": "10001-30000人", "color": "#FFC1C1"},
            {'min': 30001, "max": 40000, "label": "3001-40000人", "color": "#FFFF00"},
            {'min': 40001, "label": "40001+人", "color": "#00EE76"}
        ]
    ))

bar.render("销售额.html")
