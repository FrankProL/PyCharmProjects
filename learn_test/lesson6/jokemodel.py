#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: jokemodel.py
@time: 2015/12/14 0014 下午 5:40
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship,backref
from sqlalchemy.dialects.mysql import LONGTEXT

#1.创建连接
engine = create_engine('mysql+mysqldb://root:root@127.0.0.1:3306/testdb?charset=utf8',echo=True)

#2.定义映射
Base = declarative_base()
class Joke(Base):
    __tablename__ = 'jokes'

    id = Column(Integer,primary_key=True)
    content = Column(LONGTEXT)



#3.映射实例化，创建数据库表
Base.metadata.create_all(engine)

#4.创建会话
Session = sessionmaker(engine)
session = Session()
