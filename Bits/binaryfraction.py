'''
Binary to String: Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double,
print the binary representation. If the number cannot be represented accurately in binary with at
most 32 characters, print "ERROR:'
'''


def binaryfrac(a):
    if a > 1 and a < 0:
        print('Error')
        return
    out = '.'
    while a > 0:
        r = a * 2
        if r >= 1:
            out = out + '1'
            a = r - 1
        else:
            out = out + '0'
            a = r
        if len(out) > 32:
            print('Error')
            return
    return out

binaryfrac(0.72)
binaryfrac(5/16)
