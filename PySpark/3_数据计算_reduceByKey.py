
"""
reduceByKey算子
功能: 针对KV型RDD(二元元组[元组里面的数据只有两个]),自动按照Key分组,然后根据你提供的聚合逻辑,完成组内数据(Value)的聚合操作
用法:
    rdd.reduceByKey(func)
    func: (V, V) -> V
    接受两个传入参数(类型要一致),返回一个返回值,类型和传入要求一致
    接受一个处理逻辑,对数据进行两两计算
"""

from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "C:\Python\Python310\python.exe"

conf = SparkConf().setMaster('local[*]').setAppName('two_spark')

sc = SparkContext(conf=conf)

rdd = sc.parallelize([('男', 99), ('男', 15), ('女', 12), ('女', 88)])

rdd2 = rdd.reduceByKey(lambda x, y: x + y)
# reduceByKey中接收的函数,只负责聚合,不理会分组
# 分组是自动by key来分组的
print(rdd2.collect())

sc.stop()







