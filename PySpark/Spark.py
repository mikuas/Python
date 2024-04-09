"""
Apache Spark是用于大规模数据(large-scala data)处理的统一(unified)分析引擎
Spark是一款分布式的计算框架
"""

from pyspark import SparkConf, SparkContext
# 构建PySpark执行环境入口对象
conf = (SparkConf().setMaster("local[*]").      # 运行模式
        setAppName('test_spark_app'))           # 名称

# 基于SparkConf类对象创建SparkContext类对象
sc = SparkContext(conf=conf)

# 打印PySpark的运行版本
print(sc.version)

# 停止SparkContext对象的运行(停止PySpark程序)
# sc.stop()
"""
PySpark编程模型
通过SparkContext对象,完成数据输入
输入数据后的到RDD对象,对RDD对象进行迭代计算
最终通过RDD对象的成员方法,完成数据输出工作
"""

# RDD对象
# RDD全称为：弹性分布式数据集(Resilient Distributed Datasets)
# PySpark针对数据的处理,都是以RDD对象作为载体,即:
# 数据存储在RDD内
# 各类数据的计算方法,也都是RDD的成员方法
# RDD的数据计算方法,返回值依旧是RDD对象


# 通过parallelize方法将Python对象加载到Spark内,成为RDD对象
rdd1 = sc.parallelize([1, 2, 3, 4, 5])
rdd2 = sc.parallelize((1, 2, 3, 4, 5))
rdd3 = sc.parallelize({1, 2, 3, 4, 5})
rdd4 = sc.parallelize({'name': 'miku', 'age': 24})
rdd5 = sc.parallelize('Hello World')

# 如果要查看RDD里面有什么内容,需要用collect()方法
# print(rdd1.collect())
# print(rdd2.collect())
# print(rdd3.collect())
# print(rdd4.collect())
# print(rdd5.collect())
#
# sc.stop()

# 读取文件转RDD对象,textFile(文件路径)

rdd_file = sc.textFile("C:/Users/Administrator/Desktop/mysql.txt")

print(rdd_file.collect())

sc.stop()

