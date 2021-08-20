'''
Design a tiny URL or URL shortener
Show Topic Tags          Hike    Microsoft
Design a system that takes big URLs like “http://www.geeksforgeeks.org/count-sum-of-digits-in-numbers-from-1-to-n/” and
converts them into a short 6 character URL. It is given that URLs are stored in database and every URL has an associated
integer id.  So your program should take an integer id and generate a 6 character long URL.

A URL character can be one of the following
1) A lower case alphabet [‘a’ to ‘z’], total 26 characters
2) An upper case alphabet [‘A’ to ‘Z’], total 26 characters
3) A digit [‘0′ to ‘9’], total 10 characters

There are total 26 + 26 + 10 = 62 possible characters.

So the task is to convert an integer (database id) to a base 62 number where digits of 62 base are
"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

Input:

The first line of input contains an integer T denoting the number of test cases.

And the second line consists of a long integer.


'''

def getdigits(c):
    dic = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return dic.index(c)

def decTO62(a):
    dic = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    s = []
    m = a
    while m >0:
        s.append(m%62)
        m = m //62
    n = len(s)
    out = ''
    for i in range(n-1, -1, -1):
        out += dic[s[i]]
    return out

def sixtytwoTo10(a):
    n = len(a)
    out = 0
    for i in range(n):
        digit = getdigits(a[i])
        out = out + digit * 62**(n-i-1)
    return out




a =  12345
s = decTO62(a)
sixtytwoTo10(s)





