# -*- coding: utf-8 -*-
"""
author:  LeeJiangLee
contact: ljllili23@gmail.com

19/9/2018 7:32 PM
"""
import numpy as np
import math
from collections import defaultdict

class Node:
    def __init__(self, data=None, Axis=None):
        self.data = data
        self.splitAxis = Axis  # 表示在Axis维度上分割空间
        self.lchild = None
        self.rchild = None
        self.parent = None  # 增加父节点指针


class kdTree:
    def __init__(self):
        self.root = Node()

    def insert(self, dataSet, parent, Axis):
        if dataSet.shape[0] != 0:
            sortedIdxArray = np.argsort(dataSet, axis=Axis)
            midIdx = sortedIdxArray[dataSet.shape[0] / 2]
            newNode = Node(dataSet[midIdx], Axis)
            if parent == self.root:
                root = newNode
            else:
                if newNode.data[newNode.splitAxis] > parent.data[parent.splitAxis]:
                    parent.rchild = newNode
                    newNode.parent = parent
                else:
                    parent.lchild = newNode
                    newNode.parent = parent
        self.insert(dataSet[:, :midIdx], newNode, (Axis + 1) % dataSet.shape[1])
        self.insert(dataSet[:, midIdx:], newNode, (Axis + 1) % dataSet.shape[1])

    def buildKdTree(self, dataSet):
        kdT = kdTree()
        # dataDims = dataSet.shape[1]  # 计算出数据点的维度
        Axis = 0
        self.insert(dataSet, kdT.root, Axis)

    def search(self, data, node, parent):
        if node is None:
            return False, node, parent
        if node.data == data:
            return True, node, parent
        if node.data > data:
            return self.search(data, node.lchild, node)
        if node.data < data:
            return self.search(data, node.rchild, node)

    @staticmethod
    def distence(data, node):
        # dis = 0.0
        SqDis = 0.0
        for x1, x2 in zip(data, node.data):
            SqDis += math.pow(float(x1 - x2), 2.0)
        return math.sqrt(SqDis)

    def nn(self, data):
        # list = {}
        flag, nearestNode, parent = self.search(data, self.root, self.root)
        # if flag:
        dis = self.distence(data, nearestNode)
        while data[parent.splitAxis] - parent.data[parent.splitAxis] < dis:
            if nearestNode.data[parent.splitAxis] < parent.data[parent.splitAxis]:
                q = [parent.rchild]
                while q:
                    tmp = q[0]
                    q.pop(0)
                    if dis > self.distence(data, tmp.rchild):
                        nearestNode = tmp
                        dis = self.distence(data, tmp.rchild)
                    if not tmp.lchild:
                        q.append(tmp.lchild)
                    if not tmp.rchild:
                        q.append(tmp.rchild)
            else:
                q = [parent.lchild]
                while q:
                    tmp = q[0]
                    q.pop(0)
                    if dis > self.distence(data, tmp.rchild):
                        nearestNode = tmp
                        dis = self.distence(data, tmp.rchild)
                    if not tmp.lchild:
                        q.append(tmp.lchild)
                    if not tmp.rchild:
                        q.append(tmp.rchild)
            parent = parent.parent
        if nearestNode.parent.lchild == nearestNode:
            nearestNode.parent.lchild = None
        else:
            nearestNode.parent.rchild = None
        return nearestNode

    def knn(self,data,k):
        knnlist = defaultdict(int)
        while k :
            tmp = self.nn(data)
            knnlist[tmp] += 1
        return knnlist