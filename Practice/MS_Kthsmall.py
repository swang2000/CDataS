'''
K’th smallest element
Show Topic Tags         ABCO    Cisco    Microsoft    VMWare
Given an array and a number k where k is smaller than size of array, the task is to find the k’th smallest element in
the given array. It is given that all array elements are distinct.
'''

# def kthsmallest(a, k):
#     b = qsort(a)
#     return b[k]
#
# def qsort(a):
#     if len(a) ==1:
#         return list(a)
#     if len(a)> 1:
#         key = a[-1]
#         first = []
#         second = []
#         for i in a[:-1]:
#             if i < key:
#                 first.append(i)
#             else:
#                 second.append(i)
#         if len(first) ==0:
#             return [key] + qsort(second)
#         if len(second) ==0:
#             return qsort(first) +[key]
#         else:
#             return qsort(first) + [key] + qsort(second)
#
#
# a = [2, 6, 4, 8, 7, 3, 9, 10]
# qsort(a)



# a = [1,6,35,143,9,13,36,12]
# #qsort(a)[3]
#
#
# ##  Method2 - use minheap to realize
#
# def minheapify(a):
#     n = len(a)
#     i = n//2
#     while i >= 0:
#         if 2*i + 1 < n and (a[2*i +1] < a[i]):
#             a[i], a[2*i+1] = a[2*i+1], a[i]
#         if 2*i + 2 < n and (a[2*i +2] < a[i]):
#             a[i], a[2*i+2] = a[2*i+2], a[i]
#         i -= 1
#     return a
#
# def extractKthsmall(a, k):
#     for i in range(k):
#         mh = minheapify(a)
#         temp = mh.pop(0)
#     return temp
#
# a = [1,6,35,143,9,13,36,12]
# extractKthsmall(a, 2)


##  Method3 - use maxheap to realize

def maxheapify(a):
    n = len(a)
    i = n//2
    while i >= 0:
        if 2*i +1 < n and (a[2*i +1] > a[i]):
            a[i], a[2*i +1] = a[2*i +1], a[i]
        if 2*i +2 < n and (a[2*i +2] > a[i]):
            a[i], a[2*i +2] = a[2*i +2], a[i]
        i -= 1
    return a

def exkthsmall(a, k):
    b = maxheapify(a[:k])
    for i in range(k, len(a)):
        if b[0] > a[i]:
            b[0] = a[i]
            b = maxheapify(b)
    return b[0]

a = [1,6,35,143,9,13,36,12]
exkthsmall(a, 4)




