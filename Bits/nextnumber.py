'''
Next Number: Given a positive integer, print the next smallest and the next largest number that
have the same number of 1 bits in their binary representation.
'''

def nextbig(a):
    s = bin(a)[2:]
    num_ones = 0
    for i in s:
        if i=='1':
            num_ones += 1
    return int('1'*num_ones + '0'*(len(s) -num_ones), 2), int('1'*num_ones, 2)

a = 13948
nextbig(a)