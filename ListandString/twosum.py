'''
1. Two Sum
Easy

23722

791

Add to List

Share
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

'''

def twosum(a, t):
    complement ={}
    for i,v in enumerate(a):
        if v in complement:
            return complement[v], i
        else:
            complement[t-v]=i
    return -1

a = [1,5,3,7,12]
t=4
twosum(a,t)

