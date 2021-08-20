'''
Palindrome: Implement a function to check if a linked list is a palindrome.
'''

import CdataS.Linkedlist.Linkedlist as Llist

def palindomeLL1(a):
    s = a
    f = a
    stack = [s.data]
    while f.next_node and f.next_node.next_node:
        s = s.next_node
        stack.append(s.data)
        f = f.next_node.next_node
    if f.next_node == None:
        stack.pop(-1)
    while s.next_node:
        s = s.next_node
        if stack.pop(-1) != s.data:
            return False
    return True


l1 = Llist.LinkedList()
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
l1.append(5)
l1.append(4)
l1.append(3)
l1.append(8)
#palindomeLL1(l1.root)



# Solution 2  reading forward and backword are the same

def palindromeLL2(a):
    forward = []
    backward =[]
    while a:
        forward.append(a.data)
        a = a.next_node
    s = forward.copy()
    while len(s) > 0:
        backward.append(s.pop(-1))
    return forward == backward

palindromeLL2(l1.root)

