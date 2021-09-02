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

        longest = 1 if s else 0
        if s:
            sub = [s[0]]
        for v in s:
            if v not in sub:
                sub.append(v)
                longest = max(longest, len(sub))
            else:
                if len(sub) > 1:
                    idx = sub.index(v)
                    sub = sub[idx + 1:]
                    sub.append(v)
        return longest

s = "dvdf"
a = Solution()
a.lengthOfLongestSubstring(s)
