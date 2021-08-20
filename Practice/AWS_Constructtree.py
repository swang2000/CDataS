'''
Construct Tree from Preorder Traversal (Function Problem)
Show Topic Tags          Amazon
Given an array ‘pre[]’ that represents Preorder traversal of a binary tree where every node has either 0 or 2 children.
One more array ‘preLN[]’ is given which has only two possible values ‘L’ and ‘N’. The value ‘L’ in ‘preLN[]’ indicates
that the corresponding node in Binary Tree is a leaf node and value ‘N’ indicates that the corresponding node is
non-leaf node.

Your task is to complete the function constructTree(), that constructs the tree from the given two arrays and return
the root pointer to new binary tree formed.
For Example:

Input:  pre[] = {10, 30, 20, 5, 15},  preLN[] = {'N', 'N', 'L', 'L', 'L'}
Output: Root of following tree
          10
         /  \
        30   15
       /  \
      20   5
'''

import CdataS.BT.BianrySearchTree as tree

def constructree(pre, preln, index, n):
    idx = index[0]
    if idx == n:
        return None
    temp = tree.Node(pre[index[0]])
    index[0] += 1
    if preln[idx] == 'N':
        temp.left_child = constructree(pre, preln, index, n)
        temp.right_child = constructree(pre, preln, index, n)

    return temp


def contree(pre, preln):
    n = len(pre)
    index = [0]
    return constructree(pre, preln, index, n)


pre = [10, 30, 20, 5, 15]
preln = ['N', 'N', 'L', 'L', 'L']
ct = contree(pre, preln)



