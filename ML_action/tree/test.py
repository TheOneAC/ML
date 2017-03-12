#!/usr/bin/python
import trees

myDat,labels = trees.createDataSet()

myTree = trees.createTree(myDat, labels)

trees.storeTree(myTree,'classifierStorage.txt')

print(trees.grabTree('classifierStorage.txt'))
