'''
Delete Middle Node: Implement an algorithm to delete a node in the middle (Le., any node but
the fi rst and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
EXAMPLE
Input: the node c from the linked list a - >b- >c - >d - >e- >f
Result: nothing is returned, but the new linked list looks like a->b->d->e->f
'''

import CdataS.Linkedlist.Linkedlist as Llist
def delmiddle(a):
    fast = a
    slow = a
    pre = None
    while fast.next_node and fast.next_node.next_node:
        pre = slow
        slow = slow.next_node
        fast = fast.next_node.next_node
    pre.next_node = slow.next_node

llist = Llist.LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
# llist.append(2)
llist.append(4)
llist.append(5)

delmiddle(llist.root)
llist.printL()


