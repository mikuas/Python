"""
表达式：一个具有明确结果的代码语句 如 1 + 1， type("字符串")

格式化表达式
*f"{表达式}"
"""

# *"%s\%d\%f" % (表达式，表达式，表达式)


print("1 *1 的结果是：%d" % (1 * 1))
print(f"1 * 2 的结果是：{1 * 2}")
print("字符串在python中的类型名是：%s" % type("字符串"))

"""
股价计算小程序
"""

# 变量名
name = "Tomcat"
stock_price = 11.45
stock_code = 114514
stock_price_dally_growth_factor = 1.4
growth_days = 11

finally_stock_price = stock_price * stock_price_dally_growth_factor ** growth_days

print(f"公司：{name}, 股票代码：{stock_code}, 当前股价：{stock_price}")
print("每日增长系数：%.1f, 经过%d天的增长后，股价达到了：%.2f" % (stock_price_dally_growth_factor, growth_days, finally_stock_price))

