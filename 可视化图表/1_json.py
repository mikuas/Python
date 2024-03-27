"""
json
json是一种轻量级的数据交互格式，可以按照json指定的格式取组织和封装数据
json本质上是一个带有特定格式的字符串

json数据格式可以是
{"name": "zhangsan", "age": 24}

也可以是
[{"name": "zhangsan", "age": 24}, {"name": "zhangsan", "age":}]
"""

"""
python数据和json数据的相互转化
"""

import json

data = [{"name": "zhangsan", "age": 24}, {"name": "lisi", "age": 24}]

# 通过dumps方法把python数据转化为了json数据,ensure_ascii=False,展示中文
data = json.dumps(data)

# 通过loads方法把json数据转换为了python数据
data = json.loads(data)















