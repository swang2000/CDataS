'''
Print a Binary Tree in Vertical Order | Set 1
2.9
Given a binary tree, print it vertically. The following example illustrates vertical order traversal.

           1
        /    \
       2      3
      / \    / \
     4   5  6   7
             \   \
              8   9


The output of print this tree vertically will be:
4
2
1 5 6
3 8
7
9

'''

import CdataS.BT.BianrySearchTree as tree

def verticalorder(a, order=0, s=[]):
    if a != None:
        s.append([order, a.value])
        if a.left_child:
            verticalorder(a.left_child, order+1, s)
        if a.right_child:
            verticalorder(a.right_child, order-1, s)

bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
s= []
verticalorder(bst.root, order = 0, s=s)
b = sorted(s, key =lambda s_entry: s_entry[0], reverse = True)