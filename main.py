from function import *

my_dict = {
    0: {
        'min': 0,
        'max': 4000,
        'label': '0-4000',
        'color': 'orange'
    },
    1: {
        'min': 4001,
        'max': 6000,
        'label': '4001-6000',
        'color': 'red'
    },
    2: {
        'min': 6001,
        'max': 8000,
        'label': '6001-8000',
        'color': 'green'
    },
    3: {
        'min': 8001,
        'label': '8001+',
        'color': 'blue'
    }
}

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
title = []

date = 1154

for i in range(len(x_data)):
    title.append(date)
    date -= 1


print(title)

echarts = Echarts()
file = open('C:/data.txt', 'r', encoding='utf-8')
data = file.readlines()
timeline = Timeline()
timeline.width = '1200px'
timeline.height = '600px'

echarts.readFileTimeBar(
    x_data=x_data,
    dicts=my_dict,
    line=len(x_data),
    data=data,
    num=len(x_data),
    echarts=echarts,
    title=title,
    timeline=timeline,
    time=1000,
    position='top',
    HTML_Name='Bar.html',
    PT='1%',
    angle=45,
    play=True,
    For=True
)



