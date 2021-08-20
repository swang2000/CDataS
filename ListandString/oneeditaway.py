'''
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -) true
pales, pale -) true
pale, bale -) true
pale, bae -) false
'''

def oneeditaway(s1, s2):
    l1 = list(s1)
    l2 = list(s2)
    mismatch = 0
    if  len(l2) < len(l1):
        l1, l2 = l2, l1
        while len(l1)>0:
            temp = l1.pop(0)
            if temp != l2.pop(0):
                if temp != l2.pop(0):
                    return False
        return True
    if len(l2) == len(l1):
        while len(l1)>0:
            if l1.pop(0) != l2.pop(0):
                mismatch += 1
        if mismatch >1:
            return False
        else:
            return True


s1= 'paxes'
s2 = 'paley'
oneeditaway(s1, s2)




