'''
Prime Number of Set Bits in Binary Representation
2
Given two integers ‘L’ and ‘R’, we need to write a program that finds the count of numbers having prime number of set
bits in their binary representation in the range [L, R].

Examples:

Input : 6 10
Output : 4
6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
9 -> 1001 (2 set bits , 2 is prime)
10->1010 (2 set bits , 2 is prime)

Input : 10 15
Output : 5
10 -> 1010(2 number of set bits)
11 -> 1011(3 number of set bits)
12 -> 1100(2 number of set bits)
13 -> 1101(3 number of set bits)
14 -> 1110(3 number of set bits)
15 -> 1111(4 number of set bits)
Hence total count is 5
'''

def isprime(a):
    return all( [a%i for i in range(2,a)])

isprime(7)

import numpy as np
def primesets(l, r):
    ans = 0
    for i in range(l, r+1):
        temp = bin(i)[2:]
        x = np.array([int(d) for d in temp])
        sumt = sum(x==1)
        ans += isprime(sumt)
    return ans

primesets(10, 15)
