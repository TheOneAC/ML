#!/usr/bin/python
from numpy import *

import kMeans

datMat = mat(kMeans.loadDataSet('testSet.txt'))
#myCentroid, clustAssing = kMeans.kMeans(datMat, 4)
#print myCentroid, clustAssing

#print kMeans.randCent(datMat, 10)
cenList, myNewAssments = kMeans.biKmeans(datMat, 3)
print cenList
