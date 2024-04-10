"""

"""

from pyspark import SparkConf, SparkContext
import os

os.environ["PYSPARK_PYTHON"] = "C:\Python\Python310\python.exe"
os.environ['HADOOP_HOME'] = "C:\IDEA\hadoop-3.0.0"

conf = SparkConf().setMaster('local[*]').setAppName('ALl_spark')
# SparkConf对象设置属性全局并行度为1:
conf.set("spark.default.parallelism", 1)
sc = SparkContext(conf=conf)

file_rdd = sc.textFile('C:/search_log.txt')

# print(file_rdd.collect())
"""需求1 热门搜索时间段Top3(小时精度)"""
# 按\t进行分割
# 取出时间,切片取出小时
# 把取得的时间都封装为二元元组
# 通过ByKey进行分组聚合
# 通过sortBy从大到小进行排序
# 通过take取得前三

# result1 = file_rdd.map(lambda x: x.split('\t')) \
#     .map(lambda x: x[0][:2]) \
#     .map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y) \
#     .sortBy(lambda element: element[1], ascending=False, numPartitions=1)
"""简略写法"""
result1 = file_rdd.map(lambda x: (x.split('\t')[0][:2], 1)).reduceByKey(lambda x, y: x + y) \
    .sortBy(lambda element: element[1], ascending=False, numPartitions=1).take(3)

print(f"需求1的结果是:{result1}")

"""需求2 热门搜索词Top3"""
result2 = file_rdd.map(lambda x: x.split('\t')).map(lambda x: x[2]) \
    .map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y) \
    .sortBy(lambda x: x[1], ascending=False, numPartitions=1).take(3)

print(f"需求2的结果是:{result2}")

"""需求3 统计hmcxy关键字在什么时候被搜索的最多"""
result3 = file_rdd.map(lambda x: x.split('\t')).filter(lambda x: x[2] == '黑马程序员') \
    .map(lambda x: x[0][:2]).map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y) \
    .sortBy(lambda x: x[1], ascending=False, numPartitions=1).take(3)

print(f"需求3的结果是:{result3[0][0]}")

"""需求4 转换为json数据,写入文件"""

file_rdd.map(lambda x: x.split('\t')) \
    .map(lambda x: {'time': x[0],
                    'user_id': x[1],
                    'key_world': x[2],
                    'rank_1': x[3],
                    'rank_2': x[4],
                    'url': x[5]
                    }
         ).saveAsTextFile('C:/json_data')
