from Echarts.EchartsFc import *

main_title = []

for i in range(len(Tools().getProvince('keys'))):
    main_title.append(f'中国{Tools().getYear(2024 - len(Tools().getProvince('keys')) + 1, 2024, bools=True)[i]}各省GDP')

Echarts().readFileTimeBarCharts(
    Tools().getProvince('keys'),
    Tools().getRandomNumberList(500, 100, 10000, True),
    Tools().getEchartsDict(5, 2000),
    # [],
    Echarts(),
    Timeline(),
    Tools().getYear(2024 - len(Tools().getProvince('keys')), 2024, bools=True),
    main_title,
    '全国各省GDP',
    True,
    True,
    True,
    'green',
    '1500px',
    '800px',
    True,
    False,
    2000,
    'top',
    '4%',
    45,
)



