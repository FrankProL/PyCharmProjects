#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/2/18 18:42
# @Author  : Frank
# @Site    : 
# @File    : class_test.py
# @Software: PyCharm
"""

class A():
    def __init__(self,x,y):
        self.x=x
        self._y=y

    def __str__(self):
        return self.x+' '+self._y

aa=A('hello','world')
print aa

"""经典类、新式类
   只在python2中区分，python 3中默认全部都是新式类
   经典类 不继承任何类，或者祖先类不是Object
   新式类 继承自Object，或者祖先类是Object
   python 3中默认所有类都继承自Object，全是新式类
   python 2中也不推荐再使用经典类，即使不需要继承也建议写作为继承自Object
"""
def B(object):
    pass

"""经典类type为classobj，新式类type为function"""
print type(A)
print type(B)

"""定义类
        属性
            类属性
            实例属性
        方法
    python并没有真正的私有属性，用__定义的属性，只是被改名换姓而已，用_定义的属性，意义在于唤起用户的注意
"""
"""对于属性的访问，
   可以直接访问（不建议），
   可以定义get、set方法，
   可以通过属性装饰器（获取、更改、删除）
        @property
        @***.setter
        @***.deleter
   通过描述符访问
        代码重用
        描述符必须定义成类属性
"""
class Chinese(object):
    nation = 'china'
    def __init__(self,id,name):
        self._id = id
        self.__name = name
    def sya_hi(self,msg):
        print self.msg
    def getID(self):
        return self._id
    def setID(self,id):
        self._id=id
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name
    @name.deleter
    def name(self):
        del self.__name


print Chinese.__dict__
c1 = Chinese(2, 'zhangsan')
print c1.__dict__

print c1.getID()
c1.setID(4)
print c1.getID()

print c1.name
c1.name='lisi'
print c1.name
"""描述符 
   实现__set__ __get__ __del__ 三个方法的类
"""
class Property(object):
    def __init__(self,propname,datatype,default =None):
        self._name='_'+propname+'_'
        self._type=datatype
        self._default = default if default else self._type()

    def __get__(self, instance, owner):
        return getattr(instance,self._name,self._default)

    def __set__(self, instance, value):
        if not isinstance(value,self._type):
            raise TypeError('Type Error , must be %s type0' % self._type)
        setattr(instance,self._name,value)

    def __del__(self):
        pass

class Email(Property):
    def __init__(self,propname,default=None):
        super(Email,self).__init__(propname,str,default)

    def __set__(self, instance, value):
        if not isinstance(value,self._type):
            raise TypeError('Type Error , must be %s type0' % self._type)
        if not '@' in value :
            raise ValueError('Email address is not valid')
        setattr(instance,self._name,value)


class Chinese(object):


    ID = Property('id',int)
    Name = Property('name',str)
    Email = Email('email')

    def __init__(self,id,name,email):
        self.ID = id
        self.Name=name
        self.Email = email

    @staticmethod
    def getPeopleByParents(mather,father):
        print mather,father
        return Chinese(10,'dasheng','ab@def')

    @classmethod
    def getPeopleBySibling(cls,sibling):
        print sibling
        return cls(20,'bajie','de@ad')

    def __str__(self):
        return 'ID = {0} , Name = {1} ,Email = {2}'.format(self.ID,self.Name,self.Email)

    def __repr__(self):
        return 'ID={0}'.format(self.ID)

    def __add__(self,other):
        return self.ID + other.ID

    # def __lt__(self, other):
    #     return self.ID < other.ID

class JiLin(Chinese):
    pass


dasheng = JiLin.getPeopleByParents('mather','father')
bajie = JiLin.getPeopleBySibling('dasheng')

print dasheng
print bajie