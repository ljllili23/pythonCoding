# -*- coding: utf-8 -*-
"""
author:  LeeJiangLee
contact: ljllili23@gmail.com

20/9/2018 7:50 PM
"""
import dataTreating
import kdTree
import numpy as np

trainSetDir = "C:\\Users\\User\\Downloads\\Compressed\\trainingSet"
Data = dataTreating.MnistData(trainSetDir)
kdTreeInstance = kdTree.kdTree()
kdTreeInstance.buildKdTree(Data.mnistData)