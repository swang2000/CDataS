import CdataS.BT.BianrySearchTree as tree
def distofnode(a, x):
    if a != None:
        if a.value == x:
            return 0
        else:
            ld = distofnode(a.left_child, x)
            rd = distofnode(a.right_child, x)
            if ld != None:
                return ld + 1
            elif rd != None:
                return rd + 1





bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
bst.insert(2.7)
distofnode(bst.root, 2.7)


'''
Given preorder traversal of a binary search tree, construct the BST.

For example, if the given traversal is {10, 5, 1, 7, 40, 50}, then the output should be root of following tree.

     10
   /   \
  5     40
 /  \      \
1    7      50

Solution:
1. Identify the root;
2. Code a list of index whose values are less than the root, and another list whose values are bigger than the root;
3. Split into two lists and recursively construct nodes

'''



import CdataS.BT.BianrySearchTree as tree

def pretoBST(a, temp=None):
    if len(a) == 0:
        return
    temp = a.pop(0)
    node = tree.Node(temp)
    if len(a) >0:
        if a[0] < temp:
            node.left_child = pretoBST(a,temp)
        else:
            node.right_child = pretoBST(a, temp)
    return node

L1 =pretoBST([10, 5, 1, 7, 40, 50])
L1.preorder()
