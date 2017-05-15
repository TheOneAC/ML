#!/usr/bin/python


def loadDataSet(filename):
	dataMat = []; labelMat = []
	fr = open(filename)
	for line in fr.readlines():
		lineArr = line.strip().split('\t')
		dataMat.append([float(lineArr[0]), float(lineArr[1])])
		labelMat.append(float(lineArr[2]))
	return dataMat, labelMat


def selectJrand(i, m):
	j = i
	while( j == i):
		j = int(random.uniform(0,m))
	return j

def clipAlpha(aj, H, L):
	if aj >H :
		aj = H
	if L > aj:
		aj = L
	return aj

def smpSimple(dataMAtIn, classLable, C, toler, maxIter):
	dataMatrix = mat(dataMAtIn)
	labelMat = mat(classLable).transpose()
	b = 0
	m, n = shape(dataMatrix)
	alphas  = mat(zeros((m,1)))
	iter = 0
	while(iter < maxIter):
		alphaPairsChanged = 0
		for i in range(m):
			fXi = float(multiply(alphas, labelMat).T * (dataMatrix * dataMatrix[i,:].T)) + b
			Ei = fXi - float(labelMat[i])
			if 

