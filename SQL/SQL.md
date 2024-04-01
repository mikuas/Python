### DDL(Data Definition Language)-库管理
* 查看数据库 --> show databases;


* 使用数据库 --> use 数据库名称;


* 创建数据库 --> create database 数据库名称 [charset utf8];


* 删除数据库 --> drop database 数据库名称;


* 查看当前使用的数据库 --> select database();

### DDL-表管理
* 查看有哪些表 --> show tables; (需要先选择数据库)

* 创建表 --> create table 表名称(

    列名称 列类型,

    列名称 列类型,

    ......

)

#### 列表类型有

1. _int --> 整数_

2. _float --> 浮点数_

3. _varchar(长度) --> 文本，长度为数字，做最大长度限制(255)_

4. _date --> 日期类型_

5. _timestamp --> 时间戳类型_

* 删除表

       drop table  表名称;
       drop table if exists 表名称;

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

### DQL(Data Query Language)

##### 基础查询
* 基础语法：
    select 字段列表 | * from 表

* 基础数据查询-过滤:
    select 字段列表 | * from 表 where 条件判断

##### 分组聚合
*
