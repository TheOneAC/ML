#!/usr/bin/python
from numpy import *
import operator
from os import listdir 

import knn

group, labels = knn.creatdataset()

#print( knn.classify0([0,0],group,labels, 3) )


'''
import matplotlib
import matplotlib.pyplot as plt 
fig = plt.figure()
ax = fig.add_subplot(111)
#ax.scatter(datingDatMat[:,1], datingDatMat[:,2])
#ax.scatter(datingDatMat[:,1], datingDatMat[:,2],15.0 *array(datinglabels), 15.0 *array(datinglabels))
ax.scatter(datingDatMat[:,0], datingDatMat[:,1],15.0 *array(datinglabels), 15.0 *array(datinglabels))
plt.show()
'''
knn.handwritingClassTest()