'''
Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2) .Thatis,617 + 295.
Output: 2 - > 1 - > 9. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).Thatis,617 + 295.
Output: 9 - > 1 - > 2. That is, 912.
'''

import CdataS.Linkedlist.Linkedlist as Llist

def sumlists(a, b, c = None):
    over = 0
    while a and b:
        temp = (a.data+b.data+over)%10
        if c == None:
            c  = Llist.LinkedList()
        c.append(temp)
        over = (a.data + b.data + over) // 10
        a = a.next_node
        b = b.next_node
    return c

l1 = Llist.LinkedList()
l2 = Llist.LinkedList()

l1.append(7)
l1.append(1)
l1.append(6)

l2.append(5)
l2.append(9)
l2.append(2)

c = sumlists(l1.root, l2.root)
c.printL()

# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.

def sumlistsR(a,b, c= []):
    if a and b:
        if a.next_node == None and b.next_node == None:
            temp = (a.data + b.data)%10
            over =  (a.data + b.data)//10
        else:
            over, c = sumlistsR(a.next_node, b.next_node, c)
            temp = (a.data + b.data + over)%10
            over = (a.data + b.data + over) //10
        c.append(temp)
        return over, c


def stacktoLL(over, c):
    out = Llist.LinkedList()
    if over >0:
        out.append(over)
    while len(c) >0:
        out.append(c.pop(-1))
    return out

over, c = sumlistsR(l1.root, l2.root)
d = stacktoLL(over, c)
d.printL()