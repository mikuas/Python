from Echarts.EchartsFc import *

x_data = [
    "北京市",
    "天津市",
    "上海市",
    "重庆市",
    "河北省",
    "山西省",
    "辽宁省",
    "吉林省",
    "黑龙江省",
    "江苏省",
    "浙江省",
    "安徽省",
    "福建省",
    "江西省",
    "山东省",
    "河南省",
    "湖北省",
    "湖南省",
    "广东省",
    "海南省",
    "四川省",
    "贵州省",
    "云南省",
    "陕西省",
    "甘肃省",
    "青海省",
    "台湾省",
]

main_title = []

for i in range(len(x_data)):
    main_title.append(f'全国各省{Tools().getYear(2024 - len(x_data) + 1, 2024, bools=True)[i]}GDP')

Echarts().readFileTimeBarCharts(
    x_data,
    Tools().getRandomNumberList(1000, 1000, 10000, True),
    Tools().getEchartsDict(4, 2000),
    Echarts(),
    Timeline(),
    Tools().getYear(2024 - len(x_data) + 1, 2024),
    main_title,
    '全国GDP',
    True,
    True,
)

