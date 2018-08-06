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
largeDosesArray = np.zeros((0,3),dtype=float)
smallDosesArray = np.zeros((0,3),dtype=float)
didntLikeArray = np.zeros((0,3),dtype=float)

# row_stack 这种append的方式效率不高，可以用给定array大小的0矩阵，然后填值的方式来代替！

for item,data in zip(label,dataSet):
    if item==0:
        largeDosesArray = np.row_stack((largeDosesArray,data))
    elif item==1:
        smallDosesArray = np.row_stack((smallDosesArray,data))
    else:
        didntLikeArray = np.row_stack((didntLikeArray,data))
ax.scatter(largeDosesArray[:,0],largeDosesArray[:,1],largeDosesArray[:,2],s=100,c='green',marker='o',label='largeDoses')
ax.scatter(smallDosesArray[:,0],smallDosesArray[:,1],smallDosesArray[:,2],s=100,c='blue',marker='^',label='smallDoses')
ax.scatter(didntLikeArray[:,0],didntLikeArray[:,1],didntLikeArray[:,2],s=100,c='red',marker='x',label='didntLike')
ax.legend()
plt.show()

