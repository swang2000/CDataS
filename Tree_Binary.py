import Linkedlist




class Node:
    def __init__(self, v):
        self.value = v
        self.left_child = None
        self.right_child = None

    def get(self):
        return self.value

    def set(self, v):
        self.value = v

    def get_children(self):
        children = []
        if (self.left_child != None):
            children.append(self.left_child)
        if (self.right_child != None):
            children.append(self.right_child)

    def insert(self, val):
        if self.value <= val:
            if (self.right_child):
                return self.right_child.insert(val)
            else:
                self.right_child = Node(val)
                return True
        else:
            if (self.left_child):
                return self.left_child.insert(val)
            else:
                self.left_child = Node(val)
                return True

    def find(self, val):
        if self.value == val:
            return True
        elif self.value > val:
            if self.left_child:
                self.left_child.find(val)
            else:
                return False
        else:
            if self.right_child:
                self.right_child.find(val)
            else:
                return False

    def preorder(self):
        print(str(self.value))
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()

    def postorder(self):
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()
        print(str(self.value))

    def inorder(self):
        if self.left_child:
            self.left_child.inorder()
        print(str(self.value))
        if self.right_child:
            self.right_child.inorder()


class BST:
    def __init__(self):
        self.root = None

    def setRoot(self, val):
        self.root = Node(val)

    def insert(self, val):
        if self.root:
            self.root.insert(val)
        else:
            self.root = Node(val)

    def find(self, val):
        if self.root:
            self.root.find(val)
        else:
            return False

    def preorder(self):
        print('Preorder Print')
        if self.root:
            self.root.preorder()
        else:
            print('Tree is empty')

    def postorder(self):
        print('Postorder Print')
        if self.root:
            self.root.postorder()
        else:
            print('Tree is empty')

    def inorder(self):
        print('Inorder Print')
        if self.root:
            self.root.inorder()
        else:
            print('Tree is empty')



    def treelevel_linkedlist(self, lists={}, d=None):
        if d == None:
            d = depth(self)
        if lists.get(d) == None:
            lists[d] = LinkedList(self.value)
        else:
            lists[d].add(self.val)
            if d == 1:
                return lists
        if self.left_child != None:
            lists = treelevel_linkedlist(self.left_child, lists, d - 1)
        if self.right_child != None:
            lists = treelevel_linkedlist(self.right_child, lists, d - 1)
        return lists


bst = BST()
bst.insert(10)
bst.insert(12)
bst.insert(8)
bst.insert(23)
bst.insert(13)
bst.insert(28)
bst.insert(6)
bst.insert(8)
bst.preorder()
# Delete the root node
bst.delete(10)
bst.preorder()
# Delete the node which has both left and right child
bst.delete(23)
bst.preorder()
# Delete the node which has only right child
bst.delete(12)
bst.preorder()

