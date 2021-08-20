'''
Number of Groups
Show Topic Tags         Amazon
Given an array Arr[] of N distinct integers. Write a program to find the count of groups of 2 or 3 integers that can be
formed by choosing integers from the given array such that sum of integers in each of the group is divisible by three.

Input:
First line of input contains a single integer T which denotes the number of test case. Then T test case follows. First
line of each test case contains a single integer N which denotes number of elements in the array. Second line of each
test case contains N space separated integers.

Output:
For each test case, print the count of all the groups of 2 or 3 integers formed from the given array such that sum of
elements in the group is divisible by 3.

Constraints:
1<=T<=100
1<=N<=105
1<=Arr[i]<=105

Example:
Input:
2
6
1 5 7 2 9 14
4
3 6 9 12
Output:
13
10
'''


def numberGrps(a):
    n = len(a)
    s = 0
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j])%3 == 0:
                s += 1
            for k in range(j+1, n):
                if (a[i] + a[j] + a[k])%3 ==0:
                    s+=1
    return s

a = [1, 5, 7, 2, 9, 14]

numberGrps(a)
