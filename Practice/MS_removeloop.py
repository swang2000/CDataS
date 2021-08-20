'''
Detect and Remove Loop in a Linked List
3.5
Write a function detectAndRemoveLoop() that checks whether a given Linked List contains loop and if loop is present
then removes the loop and returns true. And if the list doesn’t contain loop then returns false. Below diagram shows a
linked list with a loop. detectAndRemoveLoop() must change the below list to 1->2->3->4->5->NULL.

'''

import CdataS.Linkedlist.Linkedlist as Llist
# def rmloops(a):
#     s = set([a])
#     while a.next_node:
#         if a.next_node not in s:
#             s.add(a.next_node)
#             a = a.next_node
#         else:
#             a.next_node = None
#
#     return s



llist = Llist.LinkedList()
llist.append(5)
llist.append(4)
llist.append(2)
llist.append(3)
llist.append(8)
llist.append(6)
llist.append(9)
llist.root.next_node.next_node.next_node.next_node.next_node.next_node.next_node = llist.root.next_node.next_node
# s = rmloops(llist.root)


# Floyd cycle detection algorithm

# def rmloops1(a):
#     slowp = fastp = a
#     while slowp and fastp and fastp.next_node:
#         slowp = slowp.next_node
#         fastp = fastp.next_node.next_node
#
#         if slowp == fastp:
#             removepoint(a, slowp)
#             return False
#     return True
#
# def removepoint(a, slowp):
#     sp1 = a
#     while True:
#         sp2 = slowp
#         while sp2.next_node != slowp and sp1 != sp2.next_node:
#             sp2 = sp2.next_node
#         if sp1 == sp2.next_node:
#             sp2.next_node = None
#             break
#         sp1 = sp1.next_node
#
#
#
# rmloops1(llist.root)


# Floyd cycle detection algorithm improvement

def rmloops2(a):
    slowp = fastp = a
    # slowp catchs up with fastp. This means the loop exists
    while slowp and fastp and fastp.next_node:
        slowp = slowp.next_node
        fastp = fastp.next_node.next_node
        if slowp == fastp:
            break
    # count the node number in the loop
    k = 0
    temp = slowp.next_node
    while temp != slowp:
        k += 1
        temp = temp.next_node

    # repoint slow and fast pointers spaced by k nodes
    slowp = fastp = a
    for _ in range(k):
        fastp = fastp.next_node

    # find the merged nodes and delete the next_node
    while True:
        if slowp == fastp.next_node:
            fastp.next_node = None
            break
        slowp = slowp.next_node
        fastp = fastp.next_node
    return

rmloops2(llist.root)


