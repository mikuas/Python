### DDL(Data Definition Language)-库管理
* 查看数据库 --> show databases;


* 使用数据库 --> use 数据库名称;


* 创建数据库 --> create database 数据库名称 [charset utf8];


* 删除数据库 --> drop database 数据库名称;


* 查看当前使用的数据库 --> select database();
---
### DDL-表管理
* 查看有哪些表 --> show tables; (需要先选择数据库)

* 创建表 --> create table 表名称(

    列名称 列类型,

    列名称 列类型,

    ......

)

---
#### 列表类型有

1. _int --> 整数_

2. _float --> 浮点数_

3. _varchar(长度) --> 文本，长度为数字，做最大长度限制(255)_

4. _date --> 日期类型_

5. _timestamp --> 时间戳类型_

* 删除表

       drop table  表名称;
       drop table if exists 表名称;
---
### DML(Data Manipulation Language)
1. 插入 --> INSERT
   * 基础语法：
    insert into 表 [(列1, 列2, ..., 列N)] values (值1, 值2, ..., 值N)[, (值1, 值2, ..., 值N)]
2. 删除 --> DELETE
   * 基础语法：
    delete from 表名称 [where 条件判断]
   
        条件判断：列 操作符 值
        
        操作符：= < > <= >= != 等等
3. 更新 --> UPDATE
    * 基础语法：
     update 表名 set 列 = 值 [where 条件判断]
   
        条件判断：列 操作符 值

        操作符：= < > <= >= != 等等
---
### DQL(Data Query Language)

##### 基础查询
* 基础语法：
    select 字段列表 | * from 表

* 基础数据查询-过滤:
    select 字段列表 | * from 表 where 条件判断
---
##### 分组聚合-group by
    分组聚合应用场景非常多，如：统计班级中，男生和女生的人数。
    这种需求就要：
    1.按性别分组
    2.统计每个组的人数
    这就称之为：分组聚合
* 基础语法：
    select 字段 | 聚合函数 from 表 [where 条件] group by 列
* 聚合函数有：
1. SUM(列) 求和
2. AVG(列) 求平均值
3. MIN(列) 求最小值
4. MAX(列) 求最大值
5. COUNT(列 | *) 求数量 

###### GROUP BY中出现了哪个列哪个列才能出现在SELECT中的非聚合中,一个SQL中是可以写多个聚合的

---
##### 排序分页-order by

* 基础语法：

    select 列 | 聚合函数 | * from 表

    where ...

    group by ...

    order by ... [ASC(升) | DESC(降)]
---

##### 结果分页限制-limit n[, m]
* 基础语法：

    select 列 | 聚合函数 | * from 表

    where ...

    group by ...

    order by ... [ASC(升) | DESC(降)]

    limit n[, m] (不加m表示取n条数据，加m表示从n之后开始取，取m行)

###### _执行顺序:    FROM -> WHERE -> GROUP BY 和聚合函数 -> SELECT -> ORDER BY -> LIMIT_

---
### python操纵mysql-pymysql
[python&mysql](python&mysql.py)
##### 获取链接对象
1. connection(主机,端口,账号,密码)即可得到链接对象
2. 链接对象.close()关闭和MySQL数据库的连接
##### 执行SQL查询
###### 通过连接对象调用cursor()方法,得到游标对象
1. 游标对象.execute()执行SQL语句
2. 游标对象.fetchall()得到全部的查询结果封装到元组内

#### 通过commit提交
自动提交：
    构建链接时传入(autocommit=True)

