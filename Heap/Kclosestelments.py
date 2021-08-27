'''
658. Find K Closest Elements
Medium

3083

357

Add to List

Share
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
'''
import heapq


class Solution(object):
    # def findClosestElements(self, arr, k, x):
    #     """
    #     :type arr: List[int]
    #     :type k: int
    #     :type x: int
    #     :rtype: List[int]
    #     """
    #     arr = sorted(arr, key=lambda i:abs(i-x))
    #     return sorted(arr[:k])

    import heapq

    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        heap = arr[:k]
        heapq.heapify(heap)
        for v in arr[k:]:
            cur_diff = abs(v-x)
            top_diff = abs(heap[0] - x)
            if cur_diff == top_diff:
                if v > heap[0]:
                    continue
                else:
                    heapq.heapreplace(heap, v)
            elif cur_diff < top_diff:
                heapq.heapreplace(heap, v)
            else:
                continue
        return sorted(heap)


s = [0,0,1,2,3,3,4,7,7,8]
k = 3
x = 5
a= Solution()
a.findClosestElements(s,k, x)