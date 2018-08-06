# -*- coding: utf-8 -*-
"""
@author:LeeJiangLee
@contact:ljllili23@gmail.com

@time: 8/5/2018 3:36 PM

"""
import KNN
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

dataSet,label = KNN.file2Matrix('datingTestSet.txt')
dataSet = KNN.normalize(dataSet)
# print(dataSet)

fig = plt.figure(figsize=(15,15))
axLabels = ('Number of frequent flyer miles earned per year','Percentage of time spent playing video games','Liters of ice cream consumed per week')
# axLabels = np.tile(axLabels,len(label))

ax = fig.gca(projection='3d')  # 111 means the position of the subplot in the figure.
ax.set_xlabel(axLabels[0])
ax.set_ylabel(axLabels[1])
ax.set_zlabel(axLabels[2])

# ax.scatter(dataSet[:,0],dataSet[:,1],dataSet[:,2], s=100, c=np.array(label),alpha=.6,label=axLabels)     # 多维array 切片
largeDosesArray = np.zero((0,3),dtype=float)
smallDosesArray = np.zero((0,3),dtype=float)
didntLikeArray = np.zero((0,3),dtype=float)

# row_stack 这种append的方式效率不高，可以用给定array大小的0矩阵，然后填值的方式来代替！

for item,data in zip(label,dataSet):
    if item==0:
        largeDosesArray = np.row_stack()
    elif item==1:
        ax.scatter(data[0], data[1], data[2], s=100, c='yellow', marker='^', alpha=.6)
    else:
        ax.scatter(data[0], data[1], data[2], s=100, c='blue', marker='^', alpha=.6)

ax.legend()
plt.show()

