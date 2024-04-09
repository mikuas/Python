
"""
flatMap算子
功能: 对RDD执行map操作,然后进行解除嵌套操作
"""
# 解除嵌套
# 嵌套的list
fu_list = [[1, 2], [3, 4], [5, 6]]
# 解除了嵌套
fu_list = [1, 2, 3, 4, 5, 6]

from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "C:\Python\Python310\python.exe"

conf = SparkConf().setMaster('local[*]').setAppName('create_spark')
sc = SparkContext(conf=conf)

rdd = sc.parallelize(['create bottom top', 'div num element', 'flex justly center'])
# 将rdd内的数据一个个的提出出来
rdd2 = rdd.flatMap(lambda data: data.split(' '))

print(rdd2.collect())

sc.stop()










