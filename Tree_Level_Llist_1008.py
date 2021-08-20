import CdataS.Linkedlist as Llist
import CdataS.Tree as Tree


# myList = Llist.LinkedList()
# myList.add(5)
# myList.add(8)
# myList.add(12)
# print("size=" + str(myList.get_size()))
# myList.remove(8)
# print("size=" + str(myList.get_size()))
# print(myList.remove(12))
# print("size=" + str(myList.get_size()))
# print(myList.find(5))
#

def createLevelLinkedList(TreeNode, lists=[], level=None):
    if (TreeNode == None):
        return lists
    if len(lists) == level:
        list = Llist.LinkedList()
        lists.append(list)
    else:
        list = lists[level]

    list.add(TreeNode.value)
    createLevelLinkedList(TreeNode.left_child, lists, level + 1)
    createLevelLinkedList(TreeNode.right_child, lists, level + 1)


# def treelevel_linkedlist(aNode, lists={}, d=None):
#     if d == None:
#         return lists
#     if lists.get(d) == None:
#         if aNode.value != None:
#             lists[d] = Llist.LinkedList(Llist.LNode(aNode.value))
#     else:
#         if aNode.value != None:
#             lists[d].add(Llist.LNode(aNode.value))
#
#     lNode, rNode  = aNode.left_child, aNode.right_child
#     if  lNode != None:
#         l = d
#         lists = treelevel_linkedlist(lNode.left_child, lists, d - 1)
#         if rNode != None:
#             lists = treelevel_linkedlist(rNode.right_child, lists, d - 1)
#     return lists


bst = Tree.BST()
bst.insert(10)
bst.insert(8)
bst.insert(6)
bst.insert(9)
bst.insert(12)
bst.insert(23)
bst.insert(13)
bst.insert(28)
bst.preorder()

myList = createLevelLinkedList(bst.root, level=0)
