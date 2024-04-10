"""
distinct
功能: 对RDD数据进行去重,返回新的RDD
语法: rdd.distinct()  无需传参
"""

from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "C:\Python\Python310\python.exe"

conf = SparkConf().setMaster('local[*]').setAppName('distinct_spark')

cs = SparkContext(conf=conf)

rdd = cs.parallelize([1, 2, 3, 4, 5, 5, 4, 3, 2, 1])

rdd = rdd.distinct()
print(rdd.collect())

cs.stop()















