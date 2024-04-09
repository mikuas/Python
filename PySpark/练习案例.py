
"""
单词计数统计
"""
import pyspark
from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "C:\Python\Python310\python.exe"
conf = SparkConf().setMaster('local[*]').setAppName('word_spark')

sc = SparkContext(conf=conf)
# 取出全部单词
rdd = sc.textFile('C:/Users/Administrator/Desktop/Hello.txt').flatMap(lambda data: data.split(' '))

print(rdd.collect())
"""
# print(type(rdd.collect()))
hanser_num = rdd.collect().count('hanser')
miku_num = rdd.collect().count('miku')
spark_num = rdd.collect().count('spark')
python_num = rdd.collect().count('python')
pyspark_num = rdd.collect().count('pyspark')
print(f"hanser_num:{hanser_num}\nmiku_num:{miku_num}\nspark_num:{spark_num}\n"
      f"python_num:{python_num}\npyspark_num:{pyspark_num}")
"""
# 将所有单词都转换为二元元组,单词为Key,Value设置为1
"""
word_list = []
for word in rdd.collect():
    word_list.append((word, 1))
"""
# 返回每一个数据(data,1)的元组
rdd = (rdd.map(lambda word: (word, 1))
       # 通过reduceByeKey方法分组并求和
       .reduceByKey(lambda x, y: x + y))
# .reduceByKey(lambda x, y: x + y))
print(rdd.collect())

sc.stop()













