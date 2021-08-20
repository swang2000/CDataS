'''
The code was created by Victor Wang to practice tree algorithm
1. Decision tree process
    a. choose a variable and split and conquer
    b. Choose a cost function - gini index, sse, entropy
    c. Interrogate every variable to select the variable with the most reduction in cost function
    d. Keep create the tree until we run out of variable or the node is pure or info gain is negligible
    e. prue the tree: use the number of leaf nodes as penalty to regularize or set the minimal size of data in a leaf
             or cut the branch with the least reduction in cost function

2. Programming design
    a. Build a tree - recursive (data - dictionary)
    b. Calculate the cost function
    c. Choose the best variable to split
    d. Count majority votes for the class

'''

import numpy as np
import math
import operator

def entropycal(dataset):
    lables = dataset[-1]
    classes = set(labels)
    entropy = 0
    p = []
    for mem in classes:
        p.append(labels[labels==mem]/len(labels))
    entropy = sum(-math.log(p, 2)*p)
    return entropy


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