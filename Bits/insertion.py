'''
Insertion: You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method
to insert M into N such that M starts at bit j and ends at bit i. You can assume that the bits j through
i have enough space to fit all of M. That is, if M = 18811, you can assume that there are at least 5
bits between j and i. You would not, for example, have j = 3 and i = 2, because M could not fully
fit between bit 3 and bit 2.
EXAMPLE
Input: N 10000000000 ,M 11001, i 2, j 6
Output: N = 10000110010
'''

def insertion(n, m, i, j):
    length = len(bin(m)[2:])
    mask = ~((2**length -1) << i)
    n_mask = n & mask
    return n_mask | (m << (j-length+1))


n = int('10001110100', 2)
m = int('10101', 2)
r = insertion(n,m, 2, 6)
bin(r)[2:]