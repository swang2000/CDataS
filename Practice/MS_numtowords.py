'''
Given number into words. For example, if “1234” is given as input, output should be “one thousand two hundred and thirty four”

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N.

Output:

Print the number into words (in small letter).

Constraints:

1 ≤ T ≤ 100
1 ≤ N ≤ 9999
'''



def numtowords(a):
    n = len(a)
    words = ['one', 'two', 'three', 'four', 'five',
             'six', 'seven', 'eight', 'nine']
    tys = ['twenty', 'thirty', 'forty','fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    out =''
    if n == 4:
        out = out + words[int(a[0])-1] + ' thousand '
    if n >= 3 and (int(a[-3]) > 0):
        out = out + words[int(a[-3])-1] + ' hundred and '
    if n >= 2 and (int(a[-2]) >1):
        out = out + tys[int(a[-2])-2] +' '
        out = out + words[int(a[-1]) - 1]
    elif n >= 2 and (int(a[-2]) ==1):
        out = out + teens[int(a[-1])]
    return out

a = '2513'
a = '8017'
numtowords(a)





