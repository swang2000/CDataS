'''
How to determine if a binary tree is height-balanced?
2.7
A tree where no leaf is much farther away from the root than any other leaf. Different balancing schemes allow different definitions of “much farther” and different amounts of work to keep them balanced.
An empty tree is height-balanced. A non-empty binary tree T is balanced if:
1) Left subtree of T is balanced
2) Right subtree of T is balanced
3) The difference between heights of left subtree and right subtree is not more than 1.

'''

import CdataS.BT.BianrySearchTree as tree

def heightBT(a):
    if a == None:
        return 0
    else:
        return max((heightBT(a.left_child) + 1),  (heightBT(a.right_child) + 1))

def balancedBT(a):
    if a == None:
        return True
    elif a.left_child is None and a.right_child:
        return balancedBT(a.right_child)
    elif a.left_child and a.right_child is None:
        return balancedBT(a.left_child)
    elif a.left_child and a.right_child:
        if abs(heightBT(a.left_child) - heightBT(a.right_child)) > 1:
            return False
        else:
            return True


bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
# bst.insert(2.3)
balancedBT(bst.root)

