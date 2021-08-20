'''
Flip Bits
Show Topic Tags         Amazon
Given an array arr[] consisting of 0’s and 1’s. A flip operation is one in which you turn 1 into 0 and a 0 into 1.You
have to do atmost one “Flip” operation on a subarray. Then finally display maximum number of 1 you can have in the array.

Input:

First line of input consist of a single integer T denoting the total number of test case.First line of test case
contains an integer N.Second line of test case contains N space separated integers denoting the array arr[].

Output:
For each test case output a single integer representing  the maximum number of 1's you can have in the array after atmost one flip operation.


Constraints:

1<=T=100
1<=N<=10000
a[i]={0,1}


Example:

Input:

1
5
1 0 0 1 0

Output:

4

Explanation:

We can perform a flip operation in the range [1,2]

After flip operation array is : 1 1 1 1 0
'''


def maxonesflipbits(a):
    ones = 0
    maxzeros = 0
    counts =0
    for i in a:
        if i == 1:
            ones += 1
            maxzeros = max(counts, maxzeros)
            counts =0
        else:
            counts += 1
    return maxzeros + ones

a = [1,0,0,1,0,0,0,0,1,0,0,1]
maxonesflipbits(a)