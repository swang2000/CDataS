'''
Kth smallest element in a row-wise and column-wise sorted 2D array | Set 1
3.9
Given an n x n matrix, where every row and column is sorted in non-decreasing order. Find the kth smallest element in
the given 2D array.

For example, consider the following 2D array.

        10, 20, 30, 40
        15, 25, 35, 45
        24, 29, 37, 48
        32, 33, 39, 50
The 3rd smallest element is 20 and 7th smallest element is 30

The idea is to use min heap. Following are detailed step.
1) Build a min heap of elements from first row. A heap entry also stores row number and column number.
2) Do following k times.
…a) Get minimum element (or root) from min heap.
…b) Find row number and column number of the minimum element.
…c) Replace root with the next element from same column and min-heapify the root.
3) Return the last extracted root.

'''


import numpy as np
# A structure to store an entry of heap.  The entry contains
# a value from 2D array, row and column numbers of the value
class HeapNode:
    def __init__(self, i, r, c):
        self.val =i  # value to be stored
        self.r =r    # Row number of value in 2D array
        self.c =c    # Column number of value in 2D array


class Minheap:
    def __init__(self):
        self.mheap =[]
        self.size = 0

    def append(self, v, i ,j):
        self.mheap.append(HeapNode(v, i, j))
        self.size += 1

    def swap(self, i, j):
        self.mheap[i], self.mheap[j] = self.mheap[j], self.mheap[i]


# A utility function to swap two HeapNode items.

 
# A utility function to minheapify the node harr[i] of a heap
# stored in harr[]
    def minHeapify(self, i):
        l = int(i*2 + 1)
        r = int(i*2 + 2)
        smallest = int(i)
        if l < self.size and (self.mheap[l].val < self.mheap[i].val):
            smallest = l
        if r < self.size and (self.mheap[r].val < self.mheap[smallest].val):
            smallest = r
        if (smallest != i):
            self.swap(i, smallest)
            self.minHeapify(smallest)

 
# A utility function to convert harr[] to a max heap
    def buildHeap(self):
        n = self.size
        i = (n - 1)//2
        while (i >= 0):
            self.minHeapify(i)
            i -= 1

 
# This function returns kth smallest element in a 2D array mat[][]
INT_MAX = 999999

def kthSmallest(a, k):
    n = len(a)
    # k must be greater than 0 and smaller than n*n
    if k <= 0 or (k > n*n):
       return INT_MAX
 
    # Create a min heap of elements from first row of 2D array
    mheap = Minheap()
    for i in range(n):
        mheap.append(a[0][i], 0, i)
    mheap.buildHeap()
    for j in range(k):

       # Get current heap root
       hr = mheap.mheap[0]
 
       # Get next value from column of root's value. If the
       # value stored at root was last value in its column,
       # then assign INFINITE as next value
       if hr.r< n-1:
           nextval = a[hr.r + 1, hr.c]
       else:
           nextval = INT_MAX
 
       # Update heap root with next value
       mheap.mheap[0] =  HeapNode(nextval, (hr.r) + 1, hr.c)
 
       # Heapify root
       mheap.minHeapify(0)
   # Return the value at last extracted root
    return mheap.mheap[0].val



a = np.array([[10, 20, 30, 40],
    [15, 25, 35, 45],
    [25, 29, 37, 48],
    [32, 33, 39, 50]])
kthSmallest(a, 6)