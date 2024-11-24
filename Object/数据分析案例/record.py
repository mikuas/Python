

class Record:

    def __init__(self, date, orders_id, money, name):
        self.date = date                    # 订单日期
        self.orders_id = orders_id          # 订单编号
        self.money = int(money)             # 销售金额
        self.name = name                    # 省份名称

    def __str__(self):
        return f'{self.date},{self.orders_id},{self.money},{self.name}'


