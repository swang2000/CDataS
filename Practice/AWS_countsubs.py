'''
Number of subsequences of the form a^i b^j c^k
4.4
Given a string, count number of subsequences of the form aibjck, i.e., it consists of i ’a’ characters, followed
by j ’b’ characters, followed by k ’c’ characters where i >= 1, j >=1 and k >= 1.

Note: Two subsequences are considered different if the set of array indexes picked for the 2 subsequences are different.

Expected Time Complexity : O(n)

Examples:

Input  : abbc
Output : 3
Subsequences are abc, abc and abbc

Input  : abcabc
Output : 7
Subsequences are abc, abc, abbc, aabc
abcc, abc and abc
Asked in : Amazon

Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.
We traverse given string. For every character encounter, we do following:

1) Initialize counts of different subsequences caused by different combination of ‘a’. Let this count be aCount.

2) Initialize counts of different subsequences caused by different combination of ‘b’. Let this count be bCount.

3) Initialize counts of different subsequences caused by different combination of ‘c’. Let this count be cCount.

4) Traverse all characters of given string. Do following for current character s[i]
    If current character is ‘a’, then there are following possibilities :
    a) Current character begins a new subsequence.
    b) Current character is part of aCount subsequences.
    c) Current character is not part of aCount subsequences.
    Therefore we do aCount = (1 + 2 * aCount);

    If current character is ‘b’, then there are following possibilities :
    a) Current character begins a new subsequence of b’s with aCount subsequences.
    b) Current character is part of bCount subsequences.
    c) Current character is not part of bCount subsequences.
    Therefore we do bCount = (aCount + 2 * bCount);

    If current character is ‘c’, then there are following possibilities :
    a) Current character begins a new subsequence of c’s with bCount subsequences.
    b) Current character is part of cCount subsequences.
    c) Current character is not part of cCount subsequences.
    Therefore we do cCount = (bCount + 2 * cCount);

5) Finally we return cCount;
'''

def countsubs(a):
    acounts = bcounts = ccounts = 0
    for i in range(len(a)):

        if a[i] == 'a':
            acounts = 1 + 2*acounts

        if a[i] == 'b':
            bcounts = acounts + 2*bcounts

        if a[i] == 'c':
            ccounts = bcounts + 2*ccounts

    return ccounts

a = 'abbcabc'
countsubs(a)
