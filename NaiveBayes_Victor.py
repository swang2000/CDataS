'''
The code was created by Victor Wang to practice NB algorithm
1. Naive bayes p(c|X) = p(X|c)*p(c) / p(X) = p(x1|c)*p(x2|c)...p(c)/p(x1)*p(x2)...
    a. Calculate the prior probability = the average class probability
    b. Calculate the conditional probability for each word and joint probability
    c. Calculate the posterior probability or ratio

2. Programming design
    a. Calculate the class probability - prior, conditional, and marginal probabilities for each doc
    b. function to calculate conditional
    c. function to calculate marginal


'''

import numpy as np
import math
import operator

def classNB0(dataset, classcategory):
    m, n = dataset.shape
    p1 = sum(classcategory)/m
    p1num = np.ones(n)
    p0num = np.ones(n)
    p1denom = 2
    p0denom =2
    for i in range(m):
        if classcategory == 1:
            p1num += dataset[i]
            p1denom += sum(dataset[i])
        else:
            p0num += dataset[i]
            p0denom += sum(dataset[i])
    p0vec = np.log(p0num/p0denom)
    p1vec = np.log(p1num/p1denom)
    return p0vec, p1vec, p1



def splitdata(dataset, axis, value):
    reducedmat = []
    for row in dataset:
        if row[axis] == value:
            rlist = row[:axis]
            rlist.extend(row[(axis+1):])
            reducedmat.append(rlist)
    return reducedmat

def bestvartosplit(dataset):
    labels = dataset[:, -1]
    m, n = dataset.shape
    baseentro = entropycal(dataset)
    minivar =0
    minientro = 0
    for c in range(n-1):
        unival = set(dataset[:,c])
        p =[]
        entro = []
        for mem in unival:
            redm = splitdata(dataset, c, mem)
            p.append(len(redm)/m)
            newentro = entropycal(redm, labels)
            entro.append(newentro)
        if c ==0:
            minientro = sum(p*newentro)
        elif sum(p*newentro) < minientro:
            minientro = sum(p*newentro)
            minivar = c
    return c, minientro

def maxcount(dataset):
    labels = dataset[:, -1]
    counts = {}
    for val in set(labels):
        counts[val] = counts.get(val, 0) + len(labels[labels==val])
    countsordered = sorted(counts.items(), key = operator.itemgetter(1), reverse = True)
    return countsordered[0][0]

def createtree(dataset):
    numofeats = dataset.shape[1] - 1
    labels = dataset[:, -1]
    if labels.count(labels[0]) == len(labels):
        return labels
    if dataset.shape[0] ==0:
        return dataset
    bestindex = bestvartosplit(dataset)
    bestfeat = labels[bestindex]
    mytree = {bestfeat:{}}
    univals = set(dataset[:, bestindex])
    for val in univals:
        mytree[bestfeat] = createtree(splitdata(dataset, bestindex, val))
    return mytree




def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    # change to discrete values
    return dataSet, labels

myDat, labels = createDataSet()
splitdata(myDat,1,1)