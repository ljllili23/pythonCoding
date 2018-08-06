# -*- coding: utf-8 -*-
"""
@author:LeeJiangLee
@contact:ljllili23@gmail.com

@time: 8/4/2018 2:59 PM

"""
from typing import List

from numpy import *
import operator


def classify(X, dataSets, label, k):
    X = array(X)
    X = X.astype(float)
    diffMat = tile(X, (dataSets.shape[0], 1)) - dataSets
    sqDiffMat = diffMat ** 2
    sqDistance = sqDiffMat.sum(1)
    distance = sqDistance ** 0.5
    sortedDistanceIndices = distance.argsort()  # return the indices that would sort an array
    resultDict={}
    for i in range(k):
        item = label[sortedDistanceIndices[i]]
        if not item in resultDict:
            resultDict[item]=1
        else:
            resultDict[item]+=1

    return max(resultDict,key=resultDict.get)


def file2Matrix(filename):
    label: List[str] = []
    dataset = zeros((0, 3), dtype=str)

    with open(filename, 'r',encoding='utf-8') as file:
        for line in file:
            line = line.strip().split('\t')
            dataset = row_stack((dataset, line[0:3]))
            if line[3]=='largeDoses':
                label.append(0)
            elif line[3]=='smallDoses':
                label.append(1)
            else:
                label.append(2)
    dataset = dataset.astype('float64')     # 从文本中读到的是字符串，要转化成浮点数！
    return dataset, label

def normalize (dataSet):
    minVals = amin(dataSet,axis=0)
    maxVals = amax(dataSet,axis=0)
    normailzedDataSet = zeros((0,3),dtype=float)
    for data in dataSet:
        data = (data-minVals)/(maxVals-minVals)
        normailzedDataSet = row_stack((normailzedDataSet,data))
    return normailzedDataSet