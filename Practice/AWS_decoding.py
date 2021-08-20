'''
Count Possible Decodings of a given Digit Sequence
3.4
Let 1 represent ‘A’, 2 represents ‘B’, etc. Given a digit sequence, count the number of possible decodings of the given
digit sequence.

Examples:

Input:  digits[] = "121"
Output: 3
// The possible decodings are "ABA", "AU", "LA"

Input: digits[] = "1234"
Output: 3
// The possible decodings are "ABCD", "LCD", "AWD"

This problem is recursive and can be broken in sub-problems. We start from end of the given digit sequence.
We initialize the total count of decodings as 0. We recur for two subproblems.
1) If the last digit is non-zero, recur for remaining (n-1) digits and add the result to total count.
2) If the last two digits form a valid character (or smaller than 27), recur for remaining (n-2) digits and add
the result to total count.
'''


def decodingways(a):
    n = len(a)
    w = [0]*(n+1)
    w[0] =w[1] = 1
    for i in range(2,n+1):
        if int(a[i-1]) >0:
            w[i] = w[i-1]
        if int(a[i-2:i]) <= 26:
            w[i] += w[i-2]
    return w

a = '1212'
decodingways(a)


