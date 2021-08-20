'''
Remove all duplicates from a given string
1.8
Below are the different methods to remove duplicates in a string.
'''

def deletedups(a):
    str1 = ''
    s = set()
    for i in a:
        if i not in s:
            s.add(i)
            str1 = str1 + i
    return str1

def deletedups2(a):
    hashtable = [0]*256
    out = ''
    for i in a:
        if hashtable[ord(i)] == 0:
            hashtable[ord(i)]  += 1
            out = out + i
    return out


a = 'Isdstgsgxvxffszxerwkfu'
deletedups2(a)
deletedups(a)




