from index.function import *

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
    '北京',
    '上海',
    '南昌',
    '深圳',
    '广东',
    '内蒙古',
    '新疆',
    '武汉',
    '河南',
    '河北'
]

title = []

date = 1154

for i in range(len(x_data)):
    title.append(date)
    date -= 1


print(title)

echarts = Echarts()
file = open('C:\data.txt', 'r', encoding='utf-8')
data = file.readlines()
timeline = Timeline()

echarts.readFileTimeBar(
    dicts=my_dict,
    line=10,
    data=data,
    num=len(x_data),
    echarts=echarts,
    x_data=x_data,
    timeline=timeline,
    time=1000,
    title=title,
    HTML_Name='Title.html',
    position='top',
    play=True,
    For=True
)



