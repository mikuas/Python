from EchartsFc import *

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

fc = Tools()

miku = Echarts()
timeline = Timeline()
timeline.width = '1200px'
timeline.height = '600px'

miku.readFileTimeBar(
    x_data=x_data,
    dicts=fc.getEchartsDict(4, 2000),
    data=fc.getNumberList(1000, 1000, 10000, True),
    echarts=Echarts(),
    title=fc.getYear(2024 - len(x_data), 2024),
    timeline=timeline,
    time=1000,
    position='top',
    HTML_Name='index.html',
    PT='1%',
    angle=45,
    play=True,
    For=True
)

