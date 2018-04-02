#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/2 15:11
# @Author  : Frank
# @Site    : 
# @File    : decorator.py
# @Software: PyCharm
"""
"""装饰器模式
   https://yq.aliyun.com/articles/70737?utm_campaign=wenzhang&utm_medium=article&utm_source=QQ-qun&utm_content=m_11966
   动态地给一个对象添加一些额外的职责。在增加功能方面，装饰器模式比生成子类更为灵活。
   装饰器模式就是代理模式的一个特殊应用，两者的共同点是都具有相同的接口，不同点是侧重对主题类的过程的控制，而装饰模式则侧重对类功能的加强或减弱。
"""

class Beverage():
    name = ""
    price = 0.0
    type = "BEVERAGE"

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name


class coke(Beverage):
    def __init__(self):
        self.name = "coke"
        self.price = 4.0


class milk(Beverage):
    def __init__(self):
        self.name = "milk"
        self.price = 5.0


class drinkDecorator():
    def getName(self):
        pass

    def getPrice(self):
        pass


class iceDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + '+ice'

    def getPrice(self):
        return self.beverage.getPrice() + 0.3


class sugarDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.berverage = beverage

    def getName(self):
        return self.berverage.getName() + '+sugar'
    def getPrice(self):
        return self.berverage.getPrice() + 0.5

if __name__ == '__main__':
    coke_cola = coke()
    print "Name:%s"%coke_cola.getName()
    print "Price:%s"%coke_cola.getPrice()
    ice_coke = iceDecorator(coke_cola)
    print "Name:%s"%ice_coke.getName()
    print "Price:%s"%ice_coke.getPrice()
