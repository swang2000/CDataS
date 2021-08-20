'''
Backtracking | Set 7 (Sudoku)
3.8
Given a partially filled 9×9 2D array ‘grid[9][9]’, the goal is to assign digits (from 1 to 9) to the empty cells so
that every row, column, and subgrid of size 3×3 contains exactly one instance of the digits from 1 to 9.



Recommended: Please solve it on “PRACTICE ” first, before moving on to the solution.
Naive Algorithm
'''

import numpy as np
def findmissing(a,b,c):
    allnumber = set([1,2,3,4,5,6,7,8,9])
    missing = allnumber - set(a) - set(b) - set(c)
    return list(missing)




def isempty(a, l):
    for i in range(9):
        for j in range(9):
            if a[i, j] == 0:
                l[0], l[1] = i, j
                return l
    return False

def boxempty(a, l):
    for i in range(3):
        for j in [x for x in [0, 1, 2] if x != i]:
            for k in range(3):
                for p in range(3):
                    if a[i*3+k, j*3+p] == 0:
                        l[0], l[1] = i*3+k, j*3+p
                        return l
    return False



def sudoku(a):

    l = [0, 0]
    if not isempty(a, l):
        return True
    x = list(a[(l[0] // 3) * 3:(l[0] // 3) * 3 + 3, (l[1] // 3) * 3:(l[1] // 3) * 3 + 3].flat)
    pot = findmissing(x, a[l[0], :], a[:, l[1]])

    for k in pot:
        a[l[0], l[1]] = k

        if sudoku(a):
            return True
        a[l[0], l[1]] = 0

    return False




# a =   np.array([[2, 3, 0, 4, 1, 5, 0, 6, 8],
#                 [0, 8, 0, 2, 3, 6, 5, 1, 9],
#                 [1, 6, 0, 9, 8, 7, 2, 3, 4],
#                 [3, 1, 7, 0, 9, 4, 0, 2, 5],
#                 [4, 5, 8, 1, 2, 0, 6, 9, 7],
#                 [9, 2, 6, 0, 5, 8, 3, 0, 1],
#                 [0, 0, 0, 5, 0, 0, 1, 0, 2],
#                 [0, 0, 0, 8, 4, 2, 9, 0, 3],
#                 [5, 9, 2, 3, 7, 1, 4, 8, 6]])
#
# sudoku(a)


def filldiag(a):
    for i in range(3):
        x = np.arange(1,10)
        np.random.shuffle(x)
        x = x.reshape((3,3))
        a[i*3+0:i*3+3, i*3+0:i*3+3] = x


def skgenerator(a):
    l = [0, 0]
    if not boxempty(a, l):
        return True
    x = list(a[(l[0] // 3) * 3:(l[0] // 3) * 3 + 3, (l[1] // 3) * 3:(l[1] // 3) * 3 + 3].flat)
    pot = findmissing(x, a[l[0], :], a[:, l[1]])
    if len(pot) == 0:
        return False
    for k in pot:
        a[l[0], l[1]] = k
        if skgenerator(a):
            return True
        a[l[0], l[1]] = 0

    return False


a = np.zeros((9,9))
filldiag(a)
skgenerator(a)








