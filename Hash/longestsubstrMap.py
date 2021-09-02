'''
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n < 2:
            return n
        i, m = -1, 0
        ht = {}
        for j in range(n):
            if s[j] in ht:
                i = max(ht[s[j]], i)

            ht[s[j]] = j
            m = max(m, j-i)
        return m

s = "dvdf"
a = Solution()
a.lengthOfLongestSubstring(s)
