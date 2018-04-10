#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: 03.sqlalchemydemo.py
@time: 2015/12/14 0014 下午 2:59
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship,backref

#1.创建连接
engine = create_engine('mysql+mysqldb://root:root@127.0.0.1:3306/testdb?charset=utf8',echo=True)

#2.定义映射
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True)
    name = Column(String(40))
    orders = relationship('Order')

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer,primary_key=True)
    name = Column(String(40))
    orders = relationship('Order')

class Order(Base):
     __tablename__ = 'orders'

     id = Column(Integer,primary_key=True)
     otime = Column(DateTime)
     uid = Column(Integer,ForeignKey('users.id'))
     pid = Column(Integer,ForeignKey('products.id'))

#3.映射实例化，创建数据库表
Base.metadata.create_all(engine)

#4.创建会话
Session = sessionmaker(engine)
session = Session()

#5、对象实例持久化
dasheng=session.query(User).filter(User.name=='dasheng').one()
p1= session.query(Product).filter(Product.name=='p1').one()

o1=Order(uid=dasheng.id,pid=p1.id)
session.add(o1)
orders=dasheng.orders
for order in orders:
    print order.id
