'''
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list
'''
import CdataS.Linkedlist.Linkedlist as Llist

def ktothelast(a, k):
    if a == None:
        return -1
    else:
        n = ktothelast(a.next_node, k) + 1
        if n == k:
            print('The {}th element to the last: '.format(k), str(a.data))
        return n

llist = Llist.LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(2)
llist.append(4)
llist.append(5)
#llist.printL()
ktothelast(llist.root,2)

def kthtolast(a, k):
    p1 = a
    p2 = a
    for i in range(k):
        if p2.next_node == None:
            print('Out of boundary')
            return None
        p2 = p2.next_node

    while p2.next_node:
        p1 = p1.next_node
        p2 = p2.next_node
    print ('The {}th th element to the last: '.format(k), str(p1.data))

kthtolast(llist.root, 2)


