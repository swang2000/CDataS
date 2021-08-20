import CdataS.BT.BianrySearchTree as tree

def findDist(root, n, dep):
    if root == None:
        return False
    elif root.value == n:
        return True
    elif findDist(root.left_child, n, dep):
        dep[0] += 1
        return True
    elif findDist(root.right_child, n, dep):
        dep[0] += 1
        return True
    return False

bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
l = [-1]
dep = [0]
findDist(bst.root, 8, dep)

