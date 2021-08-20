'''
Given a 2D array, find the maximum sum subarray in it. For example, in the following 2D array, the maximum sum subarray
is highlighted with blue rectangle and sum of this subarray is 29.



Input:
First line of every test case consists of T test case. First line of every test case consists of 2 integers R and C ,
denoting number of rows and columns. Second line consists of R*C spaced integers denoting number of elements in array.

Output:
Single line output, print the Max sum forming a rectangle in a 2-D matrix

Example:
Input:
1
4 5
1 2 -1 -4 -20 -8 -3 4 2 1 3 8 10 1 3 -4 -1 1 7 -6
Ouptut:
29
'''

import numpy as np

def maxsum2D(a):
    m, n = a.shape
    ans =0
    for r1 in range(m):
        for c1 in range(n):
            for r2 in range(r1+1, m):
                for c2 in range(c1+1, n):
                   temp = a[r1:r2+1, c1:c2+1].sum()
                   if temp > ans:
                       ans = temp
    return ans


a = np.array([[1, 2, -1, -4, -20],
              [-8, -3, 4, 2, 1],
              [3, 8, 10, 1, 3],
              [-4, -1, 1, 7, -6]])

maxsum2D(a)




