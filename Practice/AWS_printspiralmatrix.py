'''
Print a given matrix in spiral form
3
Given a 2D array, print it in spiral form. See the following examples.

Input:
        1    2   3   4
        5    6   7   8
        9   10  11  12
        13  14  15  16
Output:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10


Input:
        1   2   3   4  5   6
        7   8   9  10  11  12
        13  14  15 16  17  18
Output:
1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11
'''

import numpy as np
def printspiralmatrix(a):
    rs, cs = 0, 0
    re, ce = a.shape


    while (rs < (re-1) and (cs < (ce-1))):
        for i in range (ce):
            print(a[rs, i], end = ' ')
        rs += 1
        for i in range(rs, re):
            print(a[i, ce-1], end =' ')
        ce -= 1
        if rs < (re):
            for i in range(ce-1, cs, -1):
                print(a[re-1, i], end = ' ')
            re -= 1
        if cs < (ce):
            for i in range(re, rs-1, -1):
                print(a[i, cs], end = ' ')
            cs += 1


a = np.array([[1,    2,   3,   4],
        [5,    6,   7,   8],
        [9,   10,  11,  12],
        [13,  14,  15,  16]])
printspiralmatrix(a)




