'''
Rotten Oranges
Show Topic Tags          Accolite    Amazon    Microsoft
Given a matrix of dimension r*c where each cell in the matrix can have values 0, 1 or 2 which has the following meaning:

0: Empty cell
1: Cells have fresh oranges
2: Cells have rotten oranges
So we have to determine what is the minimum time required so that all the oranges become rotten. A rotten orange at
index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right) in unit
time. If it is impossible to rot every orange then simply return -1.

Input:
The first line of input contains an integer T denoting the number of test cases. Each test case contains two integers r
and c, where r is the number of rows and c is the number of columns in the array a[]. Next r line contains space
separated c elements each in the array a[].

Output:
Print an integer which denotes the minimum time taken to rot all the oranges.(-1 if it is impossible).

Constraints:
1<=T<=100
1<=r<=100
1<=c<=100
0<=a[i]<=2

Example:
Input:
2
3 5
2 1 0 2 1
1 0 1 2 1
1 0 0 2 1
3 5
2 1 0 2 1
0 0 1 2 1
1 0 0 2 1

Output:
2
-1
'''

import numpy as np


def isvalid(i, j, R, C):
    return i>=0 and (j >=0) and (i<R) and (j <C)

class Postion:

    def __init__(self, x, y):
        self.x = x
        self.y = y

def isdelim(pos):
    return pos.x==-1 and (pos.y ==-1)




def rotorange(a):
    r, c = a.shape
    rque = []
    for i in range(r):
        for j in range(c):
            if a[i, j] ==2:
                rque.append(Postion(i,j))
    ans = 0
    rque.append(Postion(-1, -1))
    while len(rque)>0:
        temp = rque.pop(0)
        flag = False
        while isdelim(temp) is False:
            x, y = temp.x, temp.y


            if isvalid(x-1, y, r, c) and (a[x-1, y] ==1):
                a[x - 1, y] = 2
                if flag is False:
                    ans += 1
                    flag = True
                rque.append(Postion(x-1, y))

            if isvalid(x+1, y, r, c) and (a[x+1, y] ==1):
                a[x + 1, y] = 2
                if flag is False:
                    ans += 1
                    flag = True
                rque.append(Postion(x+1, y))

            if isvalid(x, y-1, r, c) and (a[x, y-1] ==1):
                a[x, y-1] = 2
                if flag is False:
                    ans += 1
                    flag = True
                rque.append(Postion(x, y-1))

            if isvalid(x, y+1, r, c) and (a[x, y+1] ==1):
                a[x, y+1] = 2
                if flag is False:
                    ans += 1
                    flag = True
                rque.append(Postion(x, y+1))
            temp = rque.pop(0)
        if len(rque) > 0:
            rque.append(Postion(-1, -1))

    return ans


a = np.array([[2, 1, 0, 1, 1],
              [1, 0, 2, 1, 1],
              [1, 0, 0, 1, 1]])
rotorange(a)
















