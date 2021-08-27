'''
1405. Longest Happy String
Medium

679

119

Add to List

Share
A string is called happy if it does not have any of the strings 'aaa', 'bbb' or 'ccc' as a substring.

Given three integers a, b and c, return any string s, which satisfies following conditions:

s is happy and longest possible.
s contains at most a occurrences of the letter 'a', at most b occurrences of the letter 'b' and at most c occurrences of the letter 'c'.
s will only contain 'a', 'b' and 'c' letters.
If there is no such string s return the empty string "".
'''


class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        from heapq import heappush, heappop
        heap = []
        if a != 0:
            heappush(heap, (-a, 'a'))
        if b != 0:
            heappush(heap, (-b, 'b'))
        if c != 0:
            heappush(heap, (-c, 'c'))
        s = []

        while heap:
            first, char1 = heappop(heap)
            if len(s) >= 2 and s[-1] == s[-2] == char1:
                if not heap:
                    return ''.join(s)
                else:
                    second, char2 = heappop(heap)
                    s.append(char2)
                    second += 1
                    if second != 0:
                        heappush(heap, (second, char2))
                heappush(heap, (first, char1))
                continue
            s.append(char1)
            first += 1
            if first < 0:
                heappush(heap, (first, char1))
        return ''.join(s)


a = Solution()
a.longestDiverseString(1,1,7)