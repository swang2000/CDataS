'''
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
'''

def asc_count(s1):
    table = [0]*128
    for item in s1:
        i = ord(item)
        table[i] += 1
    return table


def checkpermu(s1, s2):
    if len(s1) != len(s2):
        return False
    return asc_count(s1) == asc_count(s2)

s1 = 'abxysx'
s2 = 'xaysby'
checkpermu(s1, s2)


# solution II

def checkpermu2(s1, s2):
    return sorted(s1) == sorted(s2)

s1 = 'abxysx'
s2 = 'xaysxb'
checkpermu2(s1, s2)




