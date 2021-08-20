'''
The program was developed by Victor Wang
1. K_mean process
    a. randomly choose the data points rows/K
    b. Calculate the centroid using Euclidean distance
    c. Calculate Euclidean distance between every points to centroids
    d. Rank the K Euclidean distances from the shortest to longest
    e. Switch to class membership according to the shortest distance
    f. Rpeat b - e until no points switch the class membership

2. Design the program
    a. Randomly start the process
    b. While loops - centroids, class memberships
    c. Euclidean distance calculation function
    d. Given the class memberships, calculate the centroids for the matrix
'''


import numpy as np
import math

def euclical(v, dataset):
    m = dataset.shape[0]
    vM = np.tile(v, (m,1))
    return np.sqrt(sum((dataset - vM)**2))




def CentCal(members, dataset):
    k = len(set(members))
    centroids = np.zeros((k, dataset.shape[1]))
    i = 0
    for m in set(members):
        centroids[i, :] = dataset[members == m].mean(0)
        i +=1
    return centroids



def Kmeans(dataset, k):
    m, n = dataset.shape
    initCM = np.random.randint(1, k + 1, m)
    centroids = CentCal(initCM, dataset)
    classmembers = np.mat(np.zeros((m,2)))
    classmembers[:,0] = initCM
    classchanged = True
    while classchanged:
        classchanged = False
        for i in range(k):
            x = euclical(centroids[i,:], dataset[classmembers[:,0] == i]).argsort() + 1
            if classmembers[classmembers[:,0] == i] != x:
                classchanged = True
                classmembers[classmembers[:, 0] == i] = x
        centroids = CentCal(classmembers, dataset)
    return classmembers, centroids




