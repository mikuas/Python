"""
filter
功能: 过滤想要的数据进行保留
语法:
    rdd.filter(func)
    # func: (T) -> bool     传入一个参数进来随意类型,返回值必须是True or False
        返回是True的数据被保留,False的数据被丢弃
"""

from pyspark import SparkConf, SparkContext
import os


os.environ['PYSPARK_PYTHON'] = "C:\Python\Python310\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("filter_spark")

sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])

even_num = rdd.filter(lambda element: element % 2 == 0)
odd_num = rdd.filter(lambda element: element % 2 != 0)

print(even_num.collect(), "\n", odd_num.collect())

sc.stop()
















