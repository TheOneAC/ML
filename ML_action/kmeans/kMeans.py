#!/usr/bin/python


from numpy import *

def loadDataSet(filename):
	datMat = []
	fr = open(filename)
	for line in fr.readlines():
		curLine = line.strip().split('\t')
		fltLine = map(float, curLine)
		datMat.append(fltLine)
	return datMat


def distEclud(vecA, vecB):
	return sqrt(sum(power(vecA - vecB, 2)))


def randCent(datSet, k):
	n = shape(datSet)[1]
	centroids = mat(zeros((k, n)))
	for j in range(n):
		minJ = min(datSet[:,j])
		rangeJ = float(max(datSet[:,j])- minJ)
		centroids[:,j] = minJ + rangeJ * random.rand(k, 1)
	return centroids



def kMeans(datSet, k, distMeas = distEclud, createCent = randCent):
	m = shape(datSet)[0]
	clusterAssment = mat(zeros((m,2)))
	centroids = createCent(datSet, k)
	clusterChanged = True
	while clusterChanged:
		clusterChanged = False
		for i in range(m):
			minDist = inf
			minIndex = -1
			for j in range(k):
				distJI = distMeas(centroids[j,:], datSet[i,:])
				if distJI < minDist:
					minDist = distJI
					minIndex = j
			if clusterAssment[i,0] == minIndex:
				clusterChanged = True
			clusterAssment[i,:] = minIndex, minDist**2
		print centroids
		for cent in range(k):
			ptsInClus = datSet[nonzero(clusterAssment[:,0].A == cent)[0]]
			centroids[cent,:] = mean(ptsInClus, axis = 0)
	return centroids, clusterAssment


def biKmeans(datSet, k, distMeas = distEclud):
	m = shape(datSet)[0]
	clusterAssment = mat(zeros((m,2)))
	centroid0 = mean(datSet, axis = 0).tolist()[0]
	cenList = [centroid0]
	for j in range(m):
		clusterAssment[j,:] = distMeas(mat(centroid0), datSet[j,:])**2
	while(len(cenList) < k):
		lowestSSE = inf
		for i in range(len(cenList)):
			ptsInCurrCluster = datSet[nonzero(clusterAssment[:,0].A == i)[0],:]
			centroidMat, splitClustAss = kMeans(ptsInCurrCluster, 2, distMeas)
			sseSplit = sum(splitClustAss[:,1])
			sseNotSplit = sum(clusterAssment[nonzero(clusterAssment[:,0].A == i)[0],:])
			print "sseSplit, and sseNotSplit", sseSplit,sseNotSplit
			if(sseSplit + sseNotSplit) < lowestSSE:
				bestCentToSplit = i
				bestNewCents = centroidMat
				bestClustAss = splitClustAss.copy()
				lowestSSE = sseSplit + sseNotSplit
		bestClustAss[nonzero(bestClustAss[:,0].A == 1)[0],0] = len(cenList)
		bestClustAss[nonzero(bestClustAss[:,0].A == 0)[0],0] = bestCentToSplit
		print 'the bestCentToSplit is:', bestCentToSplit
		print 'the len of bestClustAss is:', len(bestClustAss)
		cenList[bestCentToSplit] = bestNewCents[0,:]
		cenList.append(bestNewCents[1,:])
		clusterAssment[nonzero(clusterAssment[:,0].A == bestCentToSplit)[0], :] = bestClustAss
	return mat(cenList), clusterAssment


