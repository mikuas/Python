from EchartsFc import *

Echarts().getBarChart(
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



