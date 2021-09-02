'''
1. Python bits functions for converting bits to int and vice versa
2. The most common used tricks about bits - getbit, setbit, clearbit, updatebit
3. Bit oprators - &(both ones),|(both zeros), ^(XOR, 1 and 0), ~(Negation), <<(left shift = *2**i), >>(right shift = /2**i)
AND | 0 1     OR | 0 1     XOR | 0 1    NOT | 0 1
----+-----    ---+----     ----+----    ----+----
 0  | 0 0      0 | 0 1       0 | 0 1        | 1 0
 1  | 0 1      1 | 1 1       1 | 1 0
'''

# int('1001010111001', 2)
# bin(4793)[2:]

def getbit(a, i):
    return(a & (1<<i) !=0)

getbit(9, 3)

def setbit(a, i):
    return (a | (1 <<i))

def clearbit(a, i):
    return (a & ~(1<<i))

def update(a, i, value):
    return (a & ~(1 << i) | (value<<i))


r = update(4793, 3, 0)
bin(4793)[2:]
bin(r)[2:]

def tobinary(i):
    s = []
    while i >0:
        s.insert(0, str(i%2))
        i = i // 2
    return ''.join(s)

def toint(s):
    n = len(s)
    r  = 0
    s = s[::-1]
    for i in range(n):
        if s[i]=='1':
            r += 2**i
    return r

tobinary(46)
toint(bin(46)[2:])