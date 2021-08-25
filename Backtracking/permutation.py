'''
46. Permutations
Given a collection of distinct numbers, return all possible permutations.
'''
def perm(a):
    result = []
    def dfs(temp, t):
        if len(t)==0:
            result.append(temp[:])
        for e in t:
            temp.append(e)
            s = t[:]
            s.remove(e)
            dfs(temp, s)
            temp.pop()
    dfs([], a)
    return result


a = [1,2,3]
perm(a)


