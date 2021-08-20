// given
a
binary
tree, determine
whether
this
tree is valid
BST or not?

10
6
5
1000000
3

min, max

INT_MIN = -1
INT_MAX = 65599


def checkBSTHelper(bst):
    return checkBST(bst, INT_MIN, INT_MAX)


def checkBST(bst, min, max):
    if bst == None
        return True

    // evaluate
    current
    node
    bst, check if between
    min and max
    if (bst.val <= min) | | (bst.val >= max)
        return false;

    return checkBST(bst.left, min, bst.val) & & checkBST(bst.right, bst.val, max);

    if bst.left_child == None and bst.right_child == None:
        return True
    if best.
        if bst.left_child.value <= bst.value and bst.value < bst.right_child.value:
