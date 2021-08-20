'''
wo nodes of a BST are swapped, correct the BST
3.5
Two of the nodes of a Binary Search Tree (BST) are swapped. Fix (or correct) the BST.

Input Tree:
         10
        /  \
       5    8
      / \
     2   20

In the above tree, nodes 20 and 8 must be swapped to fix the tree.
Following is the output tree
         10
        /  \
       5    20
      / \
     2   8
'''

import CdataS.BT.BianrySearchTree as tree

def swapnodes(a, l):
    if a:
        swapnodes(a.left_child, l)

        if l[3] and l[3].value > a.value:
            if l[0] is None:
                l[0] = l[3]
                l[1] = a
            else:
                l[2] = a
        l[3] = a
        swapnodes(a.right_child, l)




def swap(a):
    l = [None]*4
    swapnodes(a,l)
    if l[2] and l[0]:
        l[0].value, l[2].value = l[2].value, l[0].value
    elif l[0] and l[1]:
        l[1].value, l[0].value = l[0].value, l[1].value


bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)

bst.root.left_child.left_child.value, bst.root.right_child.left_child.value = bst.root.right_child.left_child.value, bst.root.left_child.left_child.value

swap(bst.root)
bst.print



