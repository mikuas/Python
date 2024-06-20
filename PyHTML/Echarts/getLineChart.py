from EchartsFc import *

Echarts().getLineChart(
    Tools().getProvince(['江西省']),
    Tools().getRandomNumberList(
        len(Tools().getProvince(['江西省'])),
        1000
    ),
    '江西省GDP',
    False
)
