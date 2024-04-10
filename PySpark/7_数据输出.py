
from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "C:\Python\Python310\python.exe"
conf = SparkConf().setMaster('local[*]').setAppName('print_spark')

sc = SparkContext(conf=conf)

"""
collect算子
功能: 将RDD各个分区的数据,统一收集到Driver中,形成一个List对象
用法: rdd.collect()   返回值是一个list
"""

rdd = sc.parallelize([1, 2, 3, 4, 5])

print(rdd.collect(), '\n', type(rdd.collect()))

"""
reduce算子
功能: 对RDD数据收集按照你传入的逻辑进行[聚合]
语法: rdd.reduce(func)
    # func: (T, T) -> T
    # 2参数传入 1个返回值,返回值和参数要求类型一致
"""

reduce_rdd = sc.parallelize(['hanser', 'miku'])

print(reduce_rdd.reduce(lambda x, y: x + y), '\n', type(reduce_rdd.reduce(lambda x, y: x + y)))

"""
take算子
功能: 取RDD的前N个元素,组合成list返回
"""

take_rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).take(5)

print(take_rdd, '\n', type(take_rdd))

"""
count算子
功能: 计算RDD有多少条数据,返回值是一个数字
"""

count_rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).count()

print(count_rdd, '\n', type(count_rdd))






