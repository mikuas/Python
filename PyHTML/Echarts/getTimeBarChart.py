from PyHTML.Tools import *


result = []

for i in range(4):
    re = Echarts().getBarChart(
        Tools().getProvince(['江西省']),
        Tools().getRandomNumberList(
            len(Tools().getProvince(['江西省'])),
            2000,
            10000
        ),
        Tools().getEchartsDict(4, 2000),
        '江西省',
        '江西省GDP'
    )
    result.append(re)


Echarts().getTimeBarChart(
    Timeline(),
    result,
    'GDP',
    html_name=[True, 'index.html'],
    play=True,
    auto=True
)

