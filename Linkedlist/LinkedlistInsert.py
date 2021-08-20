'''
Given a sorted linked list and a value to insert, write a function to insert the value in sorted way.

Initial Linked List [2,5,7,10,15]
Linked List after insertion of 9    [2,5,7,9,10,15]

'''
import CdataS.Linkedlist as Llist

def insert(alist, item):
    if alist == None:
        alist = Llist.LNode(item)
    preNode = None
    currentNode = alist
    while currentNode.data < item and currentNode:
        preNode = currentNode
        currentNode = currentNode.next_node
    if currentNode:
        itemNode = Llist.LNode(item)
        itemNode.next_node = currentNode
        preNode.next_node = itemNode
    else:
        preNode.next_node = Llist.LNode(item)
