#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/5 10:10
# @Author  : Frank
# @Site    : 
# @File    : kNN.py
# @Software: PyCharm
"""
import numpy as np
import operator

def createDataSet():
    group = np.array([[1.0,1.1],[1.0,1.1],[0,0],[0,0.1]])
    labels=['A','A','B','B']
    return group ,labels

def classify0(inX,dataSet,labels,k):
    dataSetSize=dataSet.shape[0]
    diffMat=np.tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat=diffMat**2
    sqDistances=sqDiffMat.sum(axis=1)
    distinces=sqDistances**0.5
    sortedDistIndicies=distinces.argsort()
    classCount={}
    for i in range(k):
        voteIlabel=labels[sortedDistIndicies[i]]

if __name__ == '__main__':
    a,b=createDataSet()
    print (a)
    print (b)