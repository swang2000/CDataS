'''
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
'''

def uniquechar(a):
    if len(a) > 128:
        return False
    bool = [False]*128
    for item in a:
        i = ord(item)
        if bool[i] == True:
            return False
        bool[i] = True
    return True





a ='abcdfeghc'
uniquechar(a)
