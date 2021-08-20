'''
Given an array of words, print the count of all anagrams together in sorted order (increasing order of counts).
For example, if the given array is {“cat”, “dog”, “tac”, “god”, “act”}, then grouped anagrams are “(dog, god)
(cat, tac, act)”. So the output will be 2 3.
'''

def countanagrams(a):
    s = []
    count = [1]
    n = len(a)
    s.append(set([x for x in a[0]]))
    for i in range(1, n):
        m = len(s)
        temp = set([x for x in a[i]])
        for j in range(m):
            if s[j] != temp:
                s.append(temp)
                count.append(1)
            else:
                count[j] += 1
                break
    return count

a = ['cat', 'dog', 'tac', 'god', 'act']
countanagrams(a)


