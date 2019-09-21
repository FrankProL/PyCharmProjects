#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/7/23 10:54
# @Author  : Frank
# @Site    : 
# @File    : magic.py
# @Software: PyCharm
"""
# https://mp.weixin.qq.com/s/vPqePyQtb3A-gKBal4O5lw

class Money:
    currency_rates={'$':1,'&':0.5}

    def __init__(self,symbol,amount):
        self.symbol=symbol
        self.amount=amount

    def __repr__(self):
        return '%s%f' %(self.symbol,self.amount)

    def convert(self,other):
        new_amount=(other.amount/self.currency_rates[other.symbol] * self.currency_rates[self.symbol])
        return Money(self.symbol,new_amount)
    def __add__(self, other):
        new_amount=self.amount+self.convert(other).amount
        return Money(self.symbol,new_amount)
if __name__ == '__main__':
    soda_cost=Money('$',5)
    pizza_cost=Money('&',8)

    print(soda_cost)
    print(pizza_cost)

    print(soda_cost + pizza_cost)
    print(pizza_cost + soda_cost)