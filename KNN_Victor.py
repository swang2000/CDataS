
## Create main functions for KNN from scratch
from numpy import *
import os

def KNN(InX, dataset, labels, k):
    tm, tn = dataset.shape
    dataToClassify = tile(InX, (tm, 1))
    distV = sqrt(sum(power(dataToClassify - dataset),2), axis=1)
    classcount = {}
    labelIndex = distV.argsort()
    for i in range(k):
        classcount[labels[labelIndex[i]]] = classcount.get(labels[labelIndex[i]], 0) + 1
    classlabel = sorted(classcount.items(), key = operator.itemgetter(1),  reverse = True)
    return classlabel[0][0]



def autoNorm(dataset):
    mins = dataset.min(0)
    ranges = dataset.max(0) - dataset.min(0)
    m = dataset.shape[0]
    minsM = tile(mins, (m, 1))
    rangesM = tile(ranges, (m,1))
    normM = (dataset - minsM)/rangesM
    return normM



