#!/usr/bin/python

import bayes
import feedparser

'''
listOfPosts, listClasses = bayes.loadDataSet()
myVocabList = bayes.createVocabList(listOfPosts)
#print myVocabList
#print bayes.setOfWords2Vec(myVocabList, listOfPosts[0])
#print listOfPosts[0]
trainMat = []
for postinDoc in listOfPosts:
	trainMat.append(bayes.setOfWords2Vec(myVocabList, postinDoc))

p0V, p1V, pAb = bayes.trainNB0(trainMat, listClasses)
print pAb
print p0V
'''


ny = feedparser.parse('http://newyork.cragslit.org/stp/index.rss')
sf = feedparser.parse('http://sfbay..cragslit.org/stp/index.rss')
vocabList, pSF, pNY = bayes.localWords(ny, sf)
