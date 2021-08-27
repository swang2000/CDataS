'''
1947. Maximum Compatibility Score Sum
Medium

277

7

Add to List

Share
There is a survey that consists of n questions where each question's answer is either 0 (no) or 1 (yes).

The survey was given to m students numbered from 0 to m - 1 and m mentors numbered from 0 to m - 1. The answers of the students are represented by a 2D integer array students where students[i] is an integer array that contains the answers of the ith student (0-indexed). The answers of the mentors are represented by a 2D integer array mentors where mentors[j] is an integer array that contains the answers of the jth mentor (0-indexed).

Each student will be assigned to one mentor, and each mentor will have one student assigned to them. The compatibility score of a student-mentor pair is the number of answers that are the same for both the student and the mentor.

For example, if the student's answers were [1, 0, 1] and the mentor's answers were [0, 0, 1], then their compatibility score is 2 because only the second and the third answers are the same.
You are tasked with finding the optimal student-mentor pairings to maximize the sum of the compatibility scores.

Given students and mentors, return the maximum compatibility score sum that can be achieved.
'''
class Solution(object):
    import numpy as np
    def maxCompatibilitySum(self, students, mentors):
        """
        :type students: List[List[int]]
        :type mentors: List[List[int]]
        :rtype: int
        """
        self.m = len(mentors)
        self.score = self.temp = 0
        #import numpy as np
        self.students = self.np.array(students)
        self.mentors = self.np.array(mentors)
        self.dfs(list(), list(range(self.m)))
        return self.score

    def dfs(self, mlist, mleft):
        #import numpy as np
        if len(mleft )==0:
            self.temp = self.m*len(self.mentors[0]) - self.np.count_nonzero(self.students -self.mentors[mlist ,:])
            if self.temp > self.score:
                self.score = self.temp
            return
        for i in mleft:
            nm = mleft[:]
            nm.remove(i)
            mlist.append(i)
            self.dfs(mlist, nm)
            mlist.pop()


students = [[1,1,0],[1,0,1],[0,0,1]]
mentors = [[1,0,0],[0,0,1],[1,1,0]]

a = Solution()
a.maxCompatibilitySum(students, mentors)