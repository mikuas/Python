from pyspark import SparkConf, SparkContext
import os
import json

os.environ['PYSPARK_PYTHON'] = "C:\Python\Python310\python.exe"
conf = SparkConf().setMaster('local[*]').setAppName('data_spark')

sc = SparkContext(conf=conf)
"""需求1 城市销售额排名"""
# 读取文件得到rdd对象，得到一个json字符串
rdd = sc.textFile('C:/orders.txt').flatMap(lambda element: element.split("|"))
# 将一个个json字符串转为字典
dict_rdd = rdd.map(lambda line: json.loads(line))
# 取出城市和销售额，封装到二元元组里(城市,销售额)
city_money = dict_rdd.map(lambda data: (data['areaName'], int(data['money'])))
# 按城市分组,按销售额聚合
city_result_rdd = city_money.reduceByKey(lambda a, b: a + b)
# 按销售额进行排序
result1 = city_result_rdd.sortBy(lambda x: x[1], ascending=False, numPartitions=1)
# print(dict_rdd.collect(), '\n', type(dict_rdd.collect()))
print(  # city_money.count(),
    # city_result_rdd.collect(),
    f"需求1的结果是:{result1.collect()}")

"""需求2 全部城市有哪些商品在售卖"""
# 通过map取得城市信息,售卖商品
two_tuple = dict_rdd.map(lambda x: (x['areaName'], x['category']))
# 通过distinct去重
rdd = two_tuple.distinct()
# 通过reduceByKey把相同的相加
result2 = rdd.reduceByKey(lambda x, y: x + ',' + y)

print(f"需求2的结果是:{result2.collect()}")
print(dict_rdd.map(lambda x: x['category']).distinct().collect())

"""需求3 北京市有哪些商品在售卖"""

result3 = result2.filter(lambda x: x[0] == '北京')

print(f'需求3的结果是:{result3.collect()}')




