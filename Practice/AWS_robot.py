'''
Find whether path exist
Show Topic Tags           Adobe    Amazon
Given a N X N matrix (M) filled with 1 , 0 , 2 , 3 . Your task is to find whether there is a path possible from source
to destination, while traversing through blank cells only. You can traverse up, down, right and left.

A value of cell 1 means Source.
A value of cell 2 means Destination.
A value of cell 3 means Blank cell.
A value of cell 0 means Blank Wall.
Note : there is only single source and single destination.


Examples:

Input : M[3][3] = {{ 0 , 3 , 2 },
                   { 3 , 3 , 0 },
                   { 1 , 3 , 0 }};
Output : Yes

Input : M[4][4] = {{ 0 , 3 , 1 , 0 },
                   { 3 , 0 , 3 , 3 },
                   { 2 , 3 , 0 , 3 },
                   { 0 , 3 , 3 , 3 }};
Output : Yes
'''

import numpy as np
def isvalid(x, y, r, c):
    return x<r and (x >=0) and(y < c) and (y>= 0)


def robot(a, x, y, b):
    if x == ex and (y == ey):
        return True
    elif isvalid(x, y, m, n) and (a[x, y] ==3 or a[x, y] ==1) and (b[x, y] ==0):
        b[x, y] = 1
        if robot(a, x-1, y, b) or robot(a, x + 1, y, b) or robot(a, x, y - 1, b) or robot(a, x, y + 1, b):
            return True
    return False








a = np.array([[ 0 , 3 , 1 , 0 ],
              [ 3 , 0 , 0 , 3 ],
              [ 2 , 3 , 0 , 3 ],
              [ 0 , 3 , 3 , 3 ]])
m, n = a.shape
b = np.zeros((m,n))
sx, sy = np.where(a==1)
ex, ey = np.where(a==2)
robot(a,sx, sy, b )



