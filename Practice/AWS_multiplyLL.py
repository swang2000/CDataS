'''
Multiply two numbers represented by Linked Lists
1.9
Given two numbers represented by linked lists, write a function that returns the multiplication
of these two linked lists.

Examples:

Input : 9->4->6
        8->4
Output : 79464

Input : 3->2->1
        1->2
Output : 3852
'''

import CdataS.Linkedlist.Linkedlist as Llist
def llTonumber(a, n=0):
    if a == None:
        return n
    else:
        n = 10*n + a.data
        return llTonumber(a.next_node, n)

a = Llist.LinkedList()
b = Llist.LinkedList()
a.append(4)
a.append(3)
a.append(2)
b.append(8)
b.append(7)
llTonumber(a.root)*llTonumber(b.root)


