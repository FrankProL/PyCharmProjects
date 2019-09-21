#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/8/1 16:32
# @Author  : Frank
# @Site    : 
# @File    : strCompare.py
# @Software: PyCharm
"""
import re

def version_compare(versionA,versionB):
    alist = re.split("(\D+)",versionA)
    blist = re.split("(\D+)",versionB)

    for i,num in enumerate(alist):
        if num.isdigit() and alist[i].isdigit():
            anum=int(num)
            bnum=int(blist[i])
            if anum>bnum:
                print ("versionA>versionB")
                break
            if anum<bnum:
                print ("versionA<versionB")
                break
        if i==len(alist)-2:
            if num>blist[i]:
                print ("versionA>versionB")
                break
            if num<blist[i]:
                print ("versionA<versionB")
                break
        if i==len(alist)-1:
            print ("versionA=versionB")

if __name__ == '__main__':
    versionA = "1.2.3a"
    versionB = "1.2.3b"
    version_compare(versionA,versionB)
    version_compare("1.11.2a","1.2.2a")