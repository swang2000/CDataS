'''
17. Letter Combinations of a Phone Number
Medium

7130

565

Add to List

Share
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


'''
def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    chars = {
        2 :['a', 'b', 'c'],
        3 :['d', 'e', 'f'],
        4 :['g', 'h', 'i'],
        5 :['j', 'k', 'l'],
        6 :['m', 'n', 'o'],
        7 :['p', 'q', 'r', 's'],
        8 :['t', 'u', 'v'],
        9 :['w', 'x', 'y', 'z']
    }
    n = len(digits)
    if n== 0:
        return []
    com = chars[int(digits[n - 1])]
    while n-2>=0:
        com = [j+i for i in com for j in chars[int(digits[n - 2])]]
        n = n-1
    return com

digits = '235'
letterCombinations(digits)
