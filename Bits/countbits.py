'''
338. Counting Bits
iven an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
'''

def countbits(a):
    r = []
    for i in range(a+1):
        chr = list(bin(i)[2:])
        r.append(chr.count('1'))
    return r

countbits(3)