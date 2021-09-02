'''
Flip Bit to Win: You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to
find the length of the longest sequence of 1 s you could create.
EXAMPLE
Input: 1775   (11011101111)
Output: 8
'''


def longestones(a):
    n = len(bin(a)[2:])
    zeros = []
    for i in range(0, n):
        if (a & (1<<i) ==0):
            zeros.append(i)
    zeros.insert(0,0)
    zeros.append(n)
    temp = 0
    j = len(zeros)
    for i in range(j-1,1,-1):
        if (zeros[i] - zeros[i-2]) > temp:
            temp = zeros[i] - zeros[i-2]
    return temp

longestones(1775)

r = int('1110100101110111',2)
longestones(r)




