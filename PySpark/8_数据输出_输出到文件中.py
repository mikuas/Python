
from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "C:\Python\Python310\python.exe"
os.environ['HADOOP_HOME'] = "C:\IDEA\hadoop-3.0.0"

conf = SparkConf().setMaster('local[*]').setAppName('print_file_spark')

sc = SparkContext(conf=conf)

"""
saveAsTextFile算子
功能: 将RDD的数据写入文本文件中
支持 本地写出 hdfs等文件系统
"""

rdd = sc.parallelize([1, 2, 3, 4, 5], numSlices=1)

# 通过getNumPartitions获取rdd的分区数
num = rdd.getNumPartitions()

# 修改rdd分区为1个
#     方式1   SparkConf对象设置属性全局并行度为1:
#           conf.set("spark.default.parallelism", "1")
#     方式2   创建rdd的时候设置(parallelize方法传入numSlices参数为1)
#           rdd = sc.parallelize([1, 2, 3, 4, 5], numSlices=1)
# print(num)

rdd.saveAsTextFile('C:/save')








