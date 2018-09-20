# -*- coding: utf-8 -*-
"""
author:  LeeJiangLee
contact: ljllili23@gmail.com

20/9/2018 8:13 PM
"""
import numpy as np
import cv2
from os import listdir
class MnistData:
    def __init__(self,dir):
        # self.labels = []
        self.mnistData = np.zeros()
        self.labels = listdir(dir)
        # self.picFile = np.zeros((len(labels),))
        for label in self.labels:
            for picFile in  listdir(dir+'/'+label):
                with cv2.imread(picFile,cv2.IMREAD_GRAYSCALE()) as pic:
                    pic