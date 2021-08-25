'''
128. Longest Consecutive Sequence
Medium

6567

303

Add to List

Share
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        longest, cur_longest = 0, min(1, len(nums))
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                continue
            elif nums[i - 1] == nums[i] - 1:
                cur_longest += 1
            else:
                longest, cur_longest = max(longest, cur_longest), 1
        return max(longest, cur_longest)
