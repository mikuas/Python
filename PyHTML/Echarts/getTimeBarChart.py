from EchartsFc import *


result = []

for i in range(20):
    re = Echarts().getBarChart(
        Tools().getProvince('keys'),
        Tools().getRandomNumberList(
            len(Tools().getProvince('keys')),
            2000,
            10000
        ),
        Tools().getEchartsDict(4, 2000),
        '江西省',
        '江西省GDP',
    )
    result.append(re)


Echarts().getTimeBarChart(
    Timeline(),
    result,
    'GDP',
    html_name=[True, 'index.html'],
    play=True,
    auto=True,
)

