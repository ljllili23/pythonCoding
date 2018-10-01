# -*- coding: utf-8 -*-
"""
author:  LeeJiangLee
contact: ljllili23@gmail.com

19/9/2018 7:32 PM
"""
import numpy as np
import math
from collections import defaultdict
import sys

sys.setrecursionlimit(1000)


class Node:
    def __init__(self, data=None, Axis=None):
        self.data = data  # data contain label; data.shape = (2,28*28)
        self.splitAxis = Axis  # 表示在Axis维度上分割空间
        self.lchild = None
        self.rchild = None
        self.parent = None  # 增加父节点指针


class kdTree:
    def __init__(self):
        self.root = Node()

    def insert(self, dataSet, parent, Axis):
        dataSetSize = dataSet.shape[0]
        # print(dataSetSize)
        if dataSetSize >= 1:
            # if dataSetSize == 1:

            dataSet = dataSet[dataSet[:, Axis].argsort()]
            newNode = Node(dataSet[int(dataSetSize / 2)], Axis)
            if parent is None:  # 这里有改动 之前是self.root
                self.root = newNode
            else:
                if newNode.data[newNode.splitAxis] > parent.data[newNode.splitAxis]:
                    parent.rchild = newNode
                    newNode.parent = parent
                else:
                    parent.lchild = newNode
                    newNode.parent = parent
            self.insert(dataSet[int(dataSetSize / 2) + 1:, :], newNode, (Axis + 1) % dataSet.shape[1] - 1)
            self.insert(dataSet[:int(dataSetSize / 2), :], newNode, (Axis + 1) % dataSet.shape[1] - 1)

    def buildKdTree(self, dataSet):
        # kdT = kdTree()
        # dataDims = dataSet.shape[1]  # 计算出数据点的维度
        Axis = 0
        self.insert(dataSet, None, Axis)

    def search(self, data, node, parent):
        # print(data)
        # print(node.data)
        if node is None:
            return parent, parent.parent
        if data[node.splitAxis] <= node.data[node.splitAxis]:
            return self.search(data, node.lchild, node)
        else:
            return self.search(data, node.rchild, node)

    @staticmethod
    def distence(data, node):
        # dis = 0.0
        SqDis = 0.0
        for x1, x2 in zip(data, node.data[:-1]):
            SqDis += math.pow(float(x1 - x2), 2.0)
        return math.sqrt(SqDis)

    def nn(self, data):
        # list = {}
        nearestNode, parent = self.search(data, self.root, self.root)
        # if flag:
        dis = self.distence(data, nearestNode)
        while (parent is not None) and (data[nearestNode.splitAxis] - parent.data[nearestNode.splitAxis] < dis):
            # print(nearestNode.data)
            # print(parent.data)
            if nearestNode.data[nearestNode.splitAxis] <= parent.data[nearestNode.splitAxis] \
                    and parent.rchild is not None:
                # print(parent.rchild.data)
                q = []
                q.append(parent.rchild)
                while q:
                    tmp = q[0]
                    q.pop(0)
                    if dis > self.distence(data, tmp):
                        nearestNode = tmp
                        dis = self.distence(data, tmp)
                    if not tmp.lchild:
                        q.append(tmp.lchild)
                    if not tmp.rchild:
                        q.append(tmp.rchild)
            elif parent.lchild is not None:
                # print(type(parent.lchild))
                #print(parent.lchild.data.dtype)
                q = []
                q.append(parent.lchild)
                # print(q[0].data.dtype)
                while q:
                    tmp = q[0]

                    # q.pop(0)
                    # print(tmp.data.dtype)
                    if dis > self.distence(data, tmp):
                        nearestNode = tmp
                        dis = self.distence(data, tmp)
                    if tmp.lchild is not None:
                        q.append(tmp.lchild)
                    if tmp.rchild is not None:
                        q.append(tmp.rchild)
                    q.pop(0)
            parent = parent.parent
        print(nearestNode.data)
        if nearestNode.parent.lchild is not None:
             nearestNode.parent.lchild = None
        else:
            nearestNode.parent.rchild = None
        # print(nearestNode.data)
        return nearestNode

    def knn(self, data, k):
        knnDict = defaultdict(int)
        # print(data.dtype)
        while k:
            tmp = self.nn(data)
            knnDict[tmp.data[-1]] += 1
        return max(knnDict, key=knnDict.get)
