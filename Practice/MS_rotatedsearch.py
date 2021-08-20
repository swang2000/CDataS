'''
Search an element in a sorted and rotated array
3.2
An element in a sorted array can be found in O(log n) time via binary search. But suppose we rotate an ascending order
sorted array at some pivot unknown to you beforehand. So for instance, 1 2 3 4 5 might become 3 4 5 1 2. Devise a way to
find an element in the rotated array in O(log n) time.
'''

def fsearch(a, l, h, key):
    if l > h:
        return -1
    mid = (l + h)//2
    if a[mid] == key:
        return mid
    if a[l] <= a[mid]:
        if a[mid] >= key:
            return fsearch(a, l, mid-1, key)
        return fsearch(a, mid+1, h, key)
    if a[mid] <= key and (key <= a[h]):
        return fsearch(a, mid+1, h, key)
    return fsearch(a, l, mid-1, key)

a=[4,5,1,2,3]
fsearch(a, 0, 4, 5)








