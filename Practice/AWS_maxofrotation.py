'''
Maximum sum of i*arr[i] among all rotations of a given array
3.1
Given an array arr[] of n integers, find the maximum that maximizes sum of value of i*arr[i] where i varies from 0
to n-1.
'''

import numpy as np
def maxofrotation(a):
    n = len(a)
    w = list(range(n))
    max = sum(np.multiply(a, w))
    for i in range(1, n):
        s= w[:-1]
        s.insert(0, w[-1])
        w = s
        temp = sum(np.multiply(a, w))
        if temp > max:
            max = temp
    return max

a = [8, 3, 1, 2]
maxofrotation(a)


