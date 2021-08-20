'''
URLify: Write a method to replace all spaces in a string with '%2e: You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: if implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr John Smith JJ, 13
Output: "Mr%2eJohn%2eSmith"
'''

def replacechars(a, k):
    b = list(a)
    for i in range(k):
        if b[i] == ' ':
            b[i]='%20'
    c = ''.join(b).rstrip()
    return c

a= "Mr John Smith  "
replacechars(a, 13)