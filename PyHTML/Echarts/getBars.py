from PyHTML.Tools import *

Echarts().getBars(
    Tools().getProvince(['江西省']),
    [Tools().getRandomNumberList(
        len(Tools().getProvince(['江西省'])),
        2000,
        10000
    ), Tools().getRandomNumberList(
        len(Tools().getProvince(['江西省'])),
        2000,
        10000
    )],
    ['商品A', '商品B'],
    'GDP',
    Tools().getEchartsDict(4, 2000)
)




