'''
49. Group Anagrams
Medium

6590

252

Add to List

Share
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
'''
import collections
def group_anagrams(s):
    r = {}
    for i in s:
        t = list(i)
        t.sort()
        j = ''.join(t)
        if j in r:
            r[j].append(i)
        else:
            r[j] =[i]
    return r


strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(strs).values())