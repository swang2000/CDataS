'''
Given a String of length N reverse each word in it. Words are separated by dots.
'''


def reversewords(a):
    out = a.split('.')
    n = len(out)
    s = ''
    for i in range(n):
        if s != '':
            s = s+('.')
        s = s+out[i][::-1]
    return s

a = 'i.like.this.program.very.much'
reversewords(a)
