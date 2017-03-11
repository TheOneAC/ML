#!/usr/bin/python

from numpy  import *
import operator

def creatdataset():
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group, labels

def classify0(inX, dataSet,labels, k):
	dataSetSize = dataSet.shape[0]
	#print(dataSetSize)
	diffMat = tile(inX, (dataSetSize,1)) - dataSet
	#print(diffMat)
	sqDiffMat = diffMat ** 2
	sqDistance = sqDiffMat.sum(axis = 1)
	#print(sqDistance)
	distance = sqDistance ** 0.5
	sortedDistanceIndices = distance.argsort()
	#print (sortedDistanceIndices)


	classCount = {}
	for i  in range(k):
		voteIlabel = labels[sortedDistanceIndices[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
	sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse = True)
	#print(sortedClassCount)
	return sortedClassCount[0][0]


def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())         
    returnMat = zeros((numberOfLines,3))        
    classLabelVector = []                         
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector


def autoNorm(dataSet):
	minVals = dataSet.min(0)
	maxVals = dataSet.max(0)
	ranges = maxVals - minVals
	normDataSet = zeros(shape(dataSet))
	m = dataSet.shape[0]
	normDataSet = dataSet - tile(minVals,(m,1))
	normDataSet = normDataSet/tile(ranges,(m,1))
	return normDataSet,ranges, minVals


def datingClassTest():
	hoRatio = 0.05
	datingDatMat, datinglabels = file2matrix('datingTestSet2.txt')
	normSet,ranges, minVals = autoNorm(datingDatMat)
	m = normSet.shape[0]
	numTestVecs = int(m* hoRatio)
	errorCount = 0
	for i in range(numTestVecs):
		classifierResult = classify0(normSet[i,:],normSet[numTestVecs:m,:],datinglabels[numTestVecs:m],3)
		print "the classifier came back with: %d , the real answer is: %d" % (classifierResult, datinglabels[i])
		if(classifierResult != datinglabels[i]): errorCount += 1.0
	print "the total error rate is %f " % (errorCount/float(numTestVecs))








def img2vector(filename):
    returnVect = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect


from os import listdir 

def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')           #load the training set
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]     #take off .txt
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)
    testFileList = listdir('testDigits')        #iterate through the test set
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]     #take off .txt
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr)
        if (classifierResult != classNumStr): errorCount += 1.0
    print "\nthe total number of errors is: %d" % errorCount
    print "\nthe total error rate is: %f" % (errorCount/float(mTest))