# -*- coding: utf-8 -*-
"""
author:  LeeJiangLee
contact: ljllili23@gmail.com

20/9/2018 8:13 PM
"""
import numpy as np
import cv2
from os import listdir
import sys
from itertools import cycle

class MnistData:
    def __init__(self,dir):
        # self.labels = []
        self.mnistData = np.zeros((0,28*28+1),dtype=np.uint8)
        self.labelList = listdir(dir)
        # self.labels = []
        # self.picFile = np.zeros((len(labels),))
        str1 = '--init data array--'
        print(str1, end='\n')

        cycleList = cycle([1]*200+[2]*200+[3]*200+[4]*200)
        for label in self.labelList:
            for picFile in listdir(dir+'\\'+label):
                pic = cv2.imread(dir+'\\'+label+'\\'+picFile,cv2.IMREAD_GRAYSCALE)
                pic.shape = (28*28)
                # print(np.append(pic,label).shape)
                self.mnistData = np.row_stack((self.mnistData,np.append(pic, label)))
                # print(".",end='')
                str2 = 'Loading'+'.'*next(cycleList)
                sys.stdout.write('\r'+str2)
                sys.stdout.write("\033[K")
                # print(chr(27) + "[2J")
            sys.stdout.write('\n')
            print('--{0} class read complete--'.format(label))
                # self.labels.append(label)
        print('--finished!!--')