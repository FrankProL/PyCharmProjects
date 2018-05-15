#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/14 15:23
# @Author  : Frank
# @Site    : 
# @File    : basicSql.py
# @Software: PyCharm
"""
from pyspark.sql import SparkSession

spark=SparkSession.builder.appName("Python Spark SQL basic example").getOrCreate()

df=spark.read.json("examples/src/main/resources/people.json")
df.show()

df.printSchema()

# df.select("name",df['age']+1).show()
#
# df.select(df['name'],df['age']+1).show()
#
# df.filter(df['age']>21).show()
#
# df.groupBy("age").count().show()
#
# df.createOrReplaceTempView('people')
# sqlDF=spark.sql("select * from people")
# sqlDF.show()
#
# df.createGlobalTempView("people")
# spark.sql("select * from global_temp.people ").show()
# spark.newSession().sql("select * from global_temp.people").show()

from pyspark.sql import Row
sc=spark.sparkContext
lines=sc.textFile("examples/src/main/resources/people.txt")
parts=lines.map(lambda l:l.split(","))
people=parts.map(lambda p:Row(name=p[0],age=int(p[1])))

schemaPeople=spark.createDataFrame(people)
schemaPeople.createOrReplaceTempView("people")
teenagers=spark.sql("select name from people where age>=13")
teenNames=teenagers.rdd.map(lambda p:"Name: "+ p.name).collect()
for name in teenNames:
    print(name)


