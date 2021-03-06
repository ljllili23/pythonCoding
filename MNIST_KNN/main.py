# -*- coding: utf-8 -*-
"""
author:  LeeJiangLee
contact: ljllili23@gmail.com

20/9/2018 7:50 PM
"""
import dataTreating
import kdTree
import numpy as np
import cv2
import os
trainSetDir = "C:\\Users\\User\\Downloads\\Compressed\\trainingSet"
testSetDir = "C:\\Users\\User\\Downloads\\Compressed\\testSet"
trainData = dataTreating.MnistData(trainSetDir)
kdTreeInstance = kdTree.kdTree()
kdTreeInstance.buildKdTree(trainData.mnistData)
for filename in os.listdir(testSetDir):
    testData = cv2.imread(testSetDir+'\\'+filename, cv2.IMREAD_GRAYSCALE)
    #cv2.imshow('testData',testData)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    testData.shape = (28*28)
    # print(testData.dtype,testData.shape)
    print(validationLabel = kdTreeInstance.knn(testData,3))

kdTreeInstance.knn()
