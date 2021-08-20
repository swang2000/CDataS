'''
Palindrome Permutation: Given a string, write a function to check if it is a permutation of
a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
permutation is a rearrangement of letters. The palindrome does not need to be limited to just
dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations:"taco cat'; "atco cta'; etc.)
'''


def getcharnumber(char):
    z = ord('z')
    a = ord('a')
    c = ord(char)
    if c<=z and (c>=a):
        return c-a
    else:
        return -1


def freqtable(a):
    table =[0]*26
    b = a.lower()
    for i in b:
        num = getcharnumber(i)
        if num >= 0:
            table[num] += 1
    return table

def maxfreqone(table):
    odd = 0
    for i in table:
        if i%2 ==1:
            odd +=1
    if odd > 1:
        return False
    return True

def palindrone(a):
    table = freqtable(a)
    bool = maxfreqone(table)
    return bool

a = 'Tact Coa'
palindrone(a)


def palindromeperm(a):
    flag = True
    n = len(a)
    first = 0
    last = n-1
    while flag and (first <= last):
        if a[first] != a[last]:
            index = a[first+1:last].index(a[first]) + first +1 if a[first] in a[first+1:last] else -1
            if index >= 0:
                a[index], a[last] = a[last], a[index]
            else:
                flag = False
        first += 1
        last -= 1
    return flag

a = 'TactoCoa'
b = a.lower()
b = [x for x in b if x!=' ']
palindromeperm(b)














