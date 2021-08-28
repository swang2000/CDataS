'''
1942. The Number of the Smallest Unoccupied Chair
Medium

281

15

Add to List

Share
There is a party where n friends numbered from 0 to n - 1 are attending. There is an infinite number of chairs in this party that are numbered from 0 to infinity. When a friend arrives at the party, they sit on the unoccupied chair with the smallest number.

For example, if chairs 0, 1, and 5 are occupied when a friend comes, they will sit on chair number 2.
When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another friend arrives at that same moment, they can sit in that chair.

You are given a 0-indexed 2D integer array times where times[i] = [arrivali, leavingi], indicating the arrival and leaving times of the ith friend respectively, and an integer targetFriend. All arrival times are distinct.

Return the chair number that the friend numbered targetFriend will sit on.
'''


class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        from heapq import heappush, heappop
        arrivals = []
        departures = []
        for i, (x, y) in enumerate(times):
            heappush(arrivals, (x, i))
            heappush(departures, (y, i))
        d = {}
        occupied = [0] * len(times)
        while True:
            if len(arrivals) > 0 and len(departures) > 0 and arrivals[0][0] < departures[0][0]:
                _, ind = heappop(arrivals)
                d[ind] = occupied.index(0)
                occupied[d[ind]] = 1
                if ind == targetFriend:
                    return d[ind]

            elif len(arrivals) > 0 and len(departures) > 0 and arrivals[0][0] >= departures[0][0]:
                _, ind = heappop(departures)
                occupied[d[ind]] = 0
