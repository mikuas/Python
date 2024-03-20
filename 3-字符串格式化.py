name = "Tom"
message = "我是 %s" % name
"""
%表示：我要占位
s表示：将变量变成字符串放入占位的地方
"""
print(message)

phone = 114514
flo = 11.45
message = "我是 %s , 我的电话是 %d , %.2f" % (name, phone, flo)
# 多个变量占位，要用括号括起来，并按照占位顺序填入 %m.nf，m控制宽度，n控制小数位数
print(message)

"""
快速格式化
"""

# f"内容{变量}"

name = "cxk"
eag = 24
fla = 11.45

print(f"我是{name}, 今年{eag}岁, 有{fla}个臭钱")
