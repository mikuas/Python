from EchartsFc import *

province = []

for i in range(len(Tools().getProvince(['江西省']))):
    province.append((Tools().getProvince(['江西省'])[i], Tools().getRandom(2000, 10000)))

print(province)

Echarts().getMap(
    province,
    '江西省GDP',
    Tools().getEchartsDict(4, 2000),
    '江西',
)
