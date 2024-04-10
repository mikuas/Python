"""
sortBy
功能: 对RDD数据进行排序,基于你指定的排序依据
语法: rdd.sortBy(func, ascending=False, numPartitions=1
 # func: (T) -> U: 告知按照rdd中哪个数据进行排序,比如 lambda x: x[1] 表示按照rdd中的第二列元素进行排序
 # ascending True升序 False 降序
 # numPartitions: 用多少分区排序(全局排序需要设置分区为1)
"""

from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "C:\Python\Python310\python.exe"
conf = SparkConf().setMaster('local[*]').setAppName('sortBy_spark')

sc = SparkContext(conf=conf)

rdd = sc.parallelize([('a', 5, 'Hello_World'), ('b', 12, 'Hello_Python'), ('c', 24, 'Hello_Spark')])

print(  # rdd.sortBy(lambda x: x[0], numPartitions=1).collect(), '\n',
    rdd.sortBy(lambda x: x[1], numPartitions=1).collect(), '\n',
    # rdd.sortBy(lambda x: x[2], numPartitions=1).collect()
)

rdd = sc.parallelize([('python', 6), ('hanser', 7), ('miku', 4), ('spark', 4), ('pyspark', 3)])

print(rdd.sortBy(lambda x: x[1], numPartitions=1).collect(), '\n',
      rdd.sortBy(lambda x: x[1], ascending=False, numPartitions=1).collect()
      )

print(rdd.sortBy(lambda x: x[0], numPartitions=1).collect(), '\n',
      rdd.sortBy(lambda x: x[0], ascending=False, numPartitions=1).collect()
      )
sc.stop()
