'''
Connect nodes at same level
3.2
Write a function to connect all the adjacent nodes at the same level in a binary tree. Structure of the given Binary Tree node is like following.

struct node{
  int data;
  struct node* left;
  struct node* right;
  struct node* nextRight;
}
Initially, all the nextRight pointers point to garbage values. Your function should set these pointers to point next right for each node.

Example

Input Tree
       A
      / \
     B   C
    / \   \
   D   E   F


Output Tree
       A--->NULL
      / \
     B-->C-->NULL
    / \   \
   D-->E-->F-->NULL
'''


class dNode:

    def __init__(self, a):
        self.data = a
        self.left = None
        self.right = None
        self.nextright = None

    def add(self, a):
        if a < self.data:
            if self.left:
                self.left.add(a)
            else:
                self.left = dNode(a)
        else:
            if self.right:
                self.right.add(a)
            else:
                self.right = dNode(a)




class dTree:

    def __init__(self):
        self.root = None

    def add(self, a):
        if self.root == None:
            self.root = dNode(a)
        else:
            self.root.add(a)

def buildconnect(a):
    q = [a]
    while True:
        n = len(q)
        if n <= 0:
            return
        while n >0:
            curr = q.pop(0)
            if n == 1:
                curr.nextright = None
            else:
                curr.nextright = q[0]

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            n -= 1



bt = dTree()
bt.add(5)
bt.add(3)
bt.add(2)
bt.add(2.5)
bt.add(4)
bt.add(8)
bt.add(6)


buildconnect(bt.root)
