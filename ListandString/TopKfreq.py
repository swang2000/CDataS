'''
347. Top K Frequent Elements
Medium
5842
291
Add to List

Share
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] =1
            else:
                freq[i] += 1
        r = sorted([(k, v) for k, v in freq.items()], key= lambda e:e[1], reverse = True)
        r = [k for k,v in r]
        return r[:k]

    def topKFrequent_heap(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import heapq
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] =1
            else:
                freq[i] += 1

        lfreq = [(-v, k) for k, v in freq.items()]
        heapq.heapify(lfreq)
        r = []
        for i in range(k):
            r.append(heapq.heappop(lfreq)[1])
        return r






a= [1,1,1,2,2,3]
k =2
s = Solution()
s.topKFrequent_heap(a, k)
