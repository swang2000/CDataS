'''
526. Beautiful Arrangement
Medium

1543

233

Add to List

Share
Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

perm[i] is divisible by i.
i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct.


'''

def beautifularrange(n):
    cand = list(range(1, n+1))
    temp =[]
    rlist =[]

    r =0
    def dfs(temp, candx, i=1):
        nonlocal r
        if i == n+1:
            rlist.append(temp[:])
            r = r+1

        for j, k in enumerate(candx):
            if not (k%i and i%k):
                temp.append(k)
                dfs(temp, candx[:j]+candx[j+1:], i+1)
                temp.pop()


    dfs(temp, cand)
    return r, rlist


beautifularrange(4)

