'''
Count subtress that sum up to a given value x
2
Given a binary tree containing n nodes. The problem is to count subtress having total node’s data sum equal to a given value x.

Examples:

Input :
             5
           /   \
        -10     3
        /  \   /  \
       9    8 -4   7

       x = 7

Output : 2
There are 2 subtrees with sum 7.

1st one is leaf node:
7.

2nd one is:

      -10
     /   \
    9     8
'''

import CdataS.BT.BianrySearchTree as tree
def treesum(a):
    sum = 0
    if a != None:
        if a.left_child:
            sum += treesum(a.left_child)
        sum += a.value
        if a.right_child:
            sum += treesum(a.right_child)
    return sum

def findsum(a, k):
    if a == None:
        return 0
    if a != None:
        if treesum(a) == k:
            return findsum(a.left_child, k) + findsum(a.right_child,k) + 1
        else:
            return findsum(a.left_child, k) + findsum(a.right_child, k)


bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4.5)
bst.insert(8)
bst.insert(6)
findsum(bst.root, 4.5)



