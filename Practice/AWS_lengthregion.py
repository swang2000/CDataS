'''
Length of largest region of 1's
Show Topic Tags           Amazon    Microsoft
Consider a matrix with rows and columns (n,m), where each cell contains either a ‘0’ or a ‘1’ and any cell containing
a 1 is called a filled cell. Two cells are said to be connected if they are adjacent to each other horizontally,
vertically, or diagonally .If one or more filled cells are connected, they form a region. Your task is to  find the
length of the largest region.

Examples:

Input : M[][5] = { 0 0 1 1 0
                   1 0 1 1 0
                   0 1 0 0 0
                   0 0 0 0 1 }
Output : 6
Ex: in the following example, there are
2 regions one with length 1 and the other as 6.
so largest region : 6
'''

import numpy as np
def lenregion(a):
    b = a.copy()
    m, n = a.shape
    for i in range(1, m):
        for j in range(1, n):
            if a[i, j] == a[i-1, j] and (a[i, j] ==1):
                b[i, j] = b[i, j] + a[i-1, j]
            if a[i, j] == a[i, j-1] and (a[i, j] ==1):
                b[i, j] = b[i, j] + a[i, j-1]
            if a[i, j] == a[i-1, j-1] and (a[i, j] ==1):
                b[i, j] = b[i, j] + a[i-1, j-1]

    return b



a = np.array([[0, 0, 1, 1, 0],
               [1, 0, 1, 1, 0],
               [0, 1, 0, 0, 0],
               [0, 0, 0, 0, 1]])

lenregion(a)


