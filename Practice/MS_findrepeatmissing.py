'''
Find the repeating and the missing | Added 3 new methods
3.2
Given an unsorted array of size n. Array elements are in range from 1 to n. One number from set {1, 2, …n} is missing
and one number occurs twice in array. Find these two numbers.

Examples:

  arr[] = {3, 1, 3}
  Output: 2, 3   // 2 is missing and 3 occurs twice

  arr[] = {4, 3, 6, 2, 1, 1}
  Output: 1, 5  // 5 is missing and 1 occurs twice
'''

def findrepmis(a):
    n = len(a)
    b = [-1]*n
    for i in a:
        b[i-1] += 1
    return [i+1 for i, x in enumerate(b) if x==-1 or x>0]

a = [4, 3, 6, 2, 1, 1]
findrepmis(a)
