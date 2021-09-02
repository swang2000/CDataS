'''
342. Power of Four
Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4x.
'''


class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n in [1, 4]:
            return True
        elif n % 4 == 0:
            while n > 2:
                n = n >> 2
            return True if n == 1 else False
        return False



a = Solution()
a.isPowerOfFour(20)