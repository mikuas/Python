### Apache Spark是用于大规模数据(large-scala data)处理的统一(unified)分析引擎
* ### Spark是一款分布式的计算框架
---
#### PySpark编程模型
* #### 通过SparkContext对象,完成数据输入
* #### 输入数据后的到RDD对象,对RDD对象进行迭代计算
* #### 最终通过RDD对象的成员方法,完成数据输出工作
---
### RDD对象
* #### RDD全称为：弹性分布式数据集(Resilient Distributed Datasets)
* #### PySpark针对数据的处理,都是以RDD对象作为载体,即:
* #### 数据存储在RDD内
* #### 各类数据的计算方法,也都是RDD的成员方法
* #### RDD的数据计算方法,返回值依旧是RDD对象
---
### Python数据容器转RDD对象
* PySpark支持通过SparkContext对象的parallelize成员方法,将:
    * list
    * tuple
    * set
    * dict
    * str
* 转换为PySpark的RDD对象(
  * 字符串会被拆分为一个个的字符,存入RDD对象
  * 字典仅有Key会被存入RDD对象)
---

#### 如果要查看RDD里面有什么内容,需要用collect()方法

---

### 读取文件转RDD对象,textFile(文件路径)

---
### [map方法(算子)](1_数据计算_map.py)
* map算子(功能:map算子,是将RDD的数据一条条处理(处理逻辑 基于map算子中接收的处理函数),返回新的RDD)
* 接受一个处理函数,可以用lambda表达式快速编写
* 对RDD内的元素逐个处理,并返回一个新的RDD
### 链式调用
* 对于返回值是新的RDD的算子,可以通过链式调用的方式多次调用算子
---
### [flatMap算子](2_数据计算_flatMap.py)
* 功能: 对RDD执行map操作,然后进行解除嵌套操作(计算逻辑和map一样,可以比map多出解除一层嵌套的功能)
---
### [reduceByKey算子](3_数据计算_reduceByKey.py)
* 功能: 针对KV型RDD(二元元组[元组里面的数据只有两个]),自动按照Key分组,然后根据你提供的聚合逻辑,完成组内数据(Value)的聚合操作
* 用法:
  rdd.reduceByKey(func)

  func: (V, V) -> V

  接受两个传入参数(类型要一致),返回一个返回值,类型和传入要求一致

  接受一个处理逻辑,对数据进行两两计算
---
### [filter算子](4_数据计算_filter.py)
* 功能: 过滤想要的数据进行保留
* 语法:
  rdd.filter(func)

    func: (T) -> bool     传入一个参数进来随意类型,返回值必须是True or False

    返回是True的数据被保留,False的数据被丢弃
---
### [distinct算子](5_数据计算_distinct.py)
* 功能: 对RDD数据进行去重,返回新的RDD
* 语法: rdd.distinct()  无需传参
---
### [sortBy算子](6_数据计算_sortBy.py)
* 功能: 对RDD数据进行排序,基于你指定的排序依据
* 语法: rdd.sortBy(func, ascending=False, numPartitions=1

  func: (T) -> U: 告知按照rdd中哪个数据进行排序,比如 lambda x: x[1] 表示按照rdd中的第二列元素进行排序

  ascending True升序 False 降序

  numPartitions: 用多少分区排序(全局排序需要设置分区为1)
---
### [数据输出](7_数据输出.py)
#### collect算子
* 功能: 将RDD各个分区的数据,统一收集到Driver中,形成一个List对象
* 用法: rdd.collect()   返回值是一个list
---
#### reduce算子
* 功能: 对RDD数据收集按照你传入的逻辑进行[聚合]
* 语法: rdd.reduce(func)

  func: (T, T) -> T

   2参数传入 1个返回值,返回值和参数要求类型一致
---
#### take算子
* 功能: 取RDD的前N个元素,组合成list返回
---
#### count算子
* 功能: 计算RDD有多少条数据,返回值是一个数字
---
#### saveAsTextFile算子
* 功能: 将RDD的数据写入文本文件中
* 支持 本地写出 hdfs等文件系统

    修改rdd分区为1个

    方式1   SparkConf对象设置属性全局并行度为1:

        conf.set("spark.default.parallelism", "1")

    方式2   创建rdd的时候设置(parallelize方法传入numSlices参数为1)

        rdd = sc.parallelize([1, 2, 3, 4, 5], numSlices=1)