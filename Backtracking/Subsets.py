'''
78. Subsets
Medium

6814

122

Add to List

Share
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''

def allsubsets(a):
    if len(a) >=1:
        r= [[]]
        #s = a[1:]
        def bfs(r,a):
            for i in a:
                newr = r[:]
                for j in newr:
                    temp = list(j)
                    temp.append(i)
                    r.append(temp)
        bfs(r,a)
    return r

def subsets(nums):
    res = []
    backtracking(res, 0, [], nums)
    return res

def backtracking(res, start, subset, nums):
    res.append(list(subset))
    for i in range(start, len(nums)):
        subset.append(nums[i])
        backtracking(res, i + 1, subset, nums)
        subset.pop()



a = [1,2,3, 4]
print(allsubsets(a))
print(subsets(a))


