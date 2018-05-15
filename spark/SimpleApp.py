#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/9 17:49
# @Author  : Frank
# @Site    : 
# @File    : SimpleApp.py
# @Software: PyCharm
"""
"""http://spark.apache.org/docs/latest/quick-start.html#self-contained-applications
"""
from pyspark.sql import SparkSession

logFile = "/opt/modules/spark-2.3.0-bin-hadoop2.7/README.md"  # Should be some file on your system
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
logData = spark.read.text(logFile).cache()

numAs = logData.filter(logData.value.contains('a')).count()
numBs = logData.filter(logData.value.contains('b')).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

spark.stop()

