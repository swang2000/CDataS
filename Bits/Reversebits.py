'''
Reverse a 32 bit given number.
Input:
The first line of input consists number of the test cases. Each test case contains a single 32 bit integer.

Output:
Print the reverse of integer.

Constraints:
1<=T<=100
0<=x<=4294967295

Example:

Input:
2
1
5

Output:
2147483648
2684354560

Explanation:
In first cases
'''


def reversebits(n):
    nbit = bin(n)[:1:-1]
    deci = 0
    for i in range(len(nbit)):
        if nbit[i] == '1':
            deci += 2**(31-i)
    return deci


reversebits(13)



