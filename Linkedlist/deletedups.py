'''
Remove Dups: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
'''

import CdataS.Linkedlist.Linkedlist as Llist


def deletedups(a):
    s = set([a.data])
    temp = a
    while temp.next_node:
        if temp.next_node.data in s:
            temp.next_node = temp.next_node.next_node
        else:
            s.add(temp.next_node.data)
        temp = temp.next_node


llist = Llist.LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(2)
llist.append(4)
llist.append(5)
llist.printL()
deletedups(llist.root)
llist.printL()


# how about no temporary buffer available?

def deletedups2(a):
    p1 = a
    while p1.next_node:
        current = p1.next_node
        pre = p1
        while current:
            if p1.data == current.data:
                pre.next_node = current.next_node
            pre = current
            current = current.next_node
        p1 = p1.next_node


llist = Llist.LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(2)
llist.append(4)
llist.append(5)
llist.printL()
deletedups2(llist.root)
llist.printL()





