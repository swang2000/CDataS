'''
398. Random Pick Index
Medium

737

895

Add to List

Share
Given an integer array nums with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the array nums.
int pick(int target) Picks a random index i from nums where nums[i] == target. If there are multiple valid i's, then each index should have an equal probability of returning.


Example 1:

Input
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
Output
[null, 4, 0, 2]

'''


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dict = {}
        for i, k in enumerate(nums):
            if k in self.dict:
                self.dict[k].append(i)
            else:
                self.dict[k] = [i]

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        import random
        return random.sample(self.dict[target], 1)
