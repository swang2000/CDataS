'''
1705. Maximum Number of Eaten Apples
Medium
Share
There is a special kind of apple tree that grows apples every day for n days. On the ith day, the tree grows apples[i] apples that will rot after days[i] days, that is on day i + days[i] the apples will be rotten and cannot be eaten. On some days, the apple tree does not grow any apples, which are denoted by apples[i] == 0 and days[i] == 0.

You decided to eat at most one apple a day (to keep the doctors away). Note that you can keep eating after the first n days.

Given two integer arrays days and apples of length n, return the maximum number of apples you can eat.
'''


class Solution(object):
    def eatenApples(self, apples, days):
        """
        :type apples: List[int]
        :type days: List[int]
        :rtype: int
        """
        import heapq
        rotten = []
        r = i = 0
        q = []
        while q or i < len(apples):
            if i < len(apples) and apples[i] > 0:
                heapq.heappush(q, [i + days[i], apples[i]])
            while q and (q[0][0] <= i or q[0][1] == 0):
                heapq.heappop(q)
            if q:
                q[0][1] -= 1
                r += 1
            i += 1

        return r
