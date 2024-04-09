from pyspark import SparkConf, SparkContext
import os

# 通过os模块给定python路径
os.environ['PYSPARK_PYTHON'] = "C:\Python\Python310\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName('test_spark')

sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])


# 通过map方法将全部的数据都乘以10
# def fuck(data):
#     return data * 10


rdd2 = rdd.map(lambda data: data * 10)  # 必须是一个能接收一个参数的,而且必须有返回值的函数
# (T) -> U
# (T) -> T

print(rdd2.collect())

# 链式调用
rdd2 = rdd2.map(lambda data: data + 5).map(lambda data: data + 10)

print(rdd2.collect())

sc.stop()



























