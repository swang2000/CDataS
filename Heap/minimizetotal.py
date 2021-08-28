'''
1962. Remove Stones to Minimize the Total
Medium

150

8

Add to List

Share
You are given a 0-indexed integer array piles, where piles[i] represents the number of stones in the ith pile, and an integer k. You should apply the following operation exactly k times:

Choose any piles[i] and remove floor(piles[i] / 2) stones from it.
Notice that you can apply the operation on the same pile more than once.

Return the minimum possible total number of stones remaining after applying the k operations.

floor(x) is the greatest integer that is smaller than or equal to x (i.e., rounds x down).
'''


class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        a = [-i for i in piles]
        heapq.heapify(a)
        for i in range(k):
            j = -heapq.heappop(a)
            heapq.heappush(a, -(j - j // 2))

        return -int(sum(a))
