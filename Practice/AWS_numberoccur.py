'''
Count number of occurrences (or frequency) in a sorted array
2.6
Given a sorted array arr[] and a number x, write a function that counts the occurrences of x in arr[]. Expected time
complexity is O(Logn)
'''

def binarysearch(a, x):
    n = len(a)
    if n ==0:
        return -1
    else:
        if a[n//2]== x:
            return n//2
        elif a[n//2] > x:
            binarysearch(a[:n//2], x)
        else:
            binarysearch(a[n//2+1:], x)

def countoccurs(a, x):
    num = 1
    t = binarysearch(a, x)
    f =b =t
    while a[f-1] ==x:
        num += 1
        f -= 1
    while a[b + 1] == x:
        num += 1
        b += 1
    return num

a = [1, 1, 2, 2, 2, 2, 3]
countoccurs(a, 2)

