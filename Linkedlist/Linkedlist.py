'''
delete a node from a linkedlist

 def deleteN(self, v):
        this_node= self.root
        prev_node = None
        while (this_node):
            if this_node.data == v:
                if prev_node is None:
                    self.root = this_node.next_node
                else:
                    prev_node = this_node.next_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False

 def append(self, v):
    this_node = self.root
    while this_node.next_node:
        this_node = this_node.next_node
    this_node.next_node = LNode(v)


'''




class LNode:
    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d




class LinkedList:
    def __init__(self, r=None):
        self.root = LNode(None, r)
        self.size = 0

    def setRoot(self, r):
        self.root = r

    def get_size(self):
        return self.size

    def add(self, d):
        new_node = LNode(d, self.root)
        self.root = new_node
        self.size += 1

    def remove(self, d):
        this_node = self.root
        prev_node = None

        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True  # data removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False  # data not found

    def find(self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None

    def append(self, d):
        if self.root.data == None:
            self.root = LNode(d)
            self.size = 1
        else:
            n = self.root
            while (n.next_node):
                n = n.next_node
            n.next_node = LNode(d)
            self.size += 1
        return self

    def printL(self):
        if self.root == None:
            print('The Linkedlist is empty')
        n = self.root
        while n:
            print(str(n.data))
            n = n.next_node




