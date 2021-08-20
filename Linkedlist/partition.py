'''
Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 113 -> 2 -> 1 [partition = 5]
Output: 3 -> 1 -> 2 -> 113 -> 5 -> 5 -> 8
'''

import CdataS.Linkedlist.Linkedlist as Llist

def partition(a, k):
    pre = None
    current = a
    q = []
    while current:
        if current.data < k:
            pre = current
        else:
            q.append(current)
            pre.next_node = current.next_node
        current = current.next_node
    while len(q) > 0:
        pre.next_node = q.pop(0)
        pre = pre.next_node

llist = Llist.LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(2)
llist.append(4)
llist.append(5)

partition(llist.root, 3)
llist.printL()


