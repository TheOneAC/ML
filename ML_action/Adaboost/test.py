#!/usr/bin/python
from numpy import *

import adaboost

datMat, classLabels = adaboost.loadDataSet()

#D = matrix(ones((5,1))/5)
#adaboost.buildStump(datMat, classLabels, D)

classifierArr = adaboost.adaBoostTrainDS(datMat, classLabels,9)
adaboost.adaClassify([0,0],classifierArr)
