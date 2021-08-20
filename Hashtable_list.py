'''
Add a new element into hashtable
def insert(self, key, value):
    self.table[self.hash_func(key)].append(value)

def delE(self, key, value):
    list1 = self.table[self.hash_func(key)]
    for i in range(len(list1)):
        if list1[i] == value:
            list1.remove(value)


'''


class HashTable_list:

    def __init__(self, capacity =10):
        self.table = [[] for _ in range(capacity)]

    def hash_func(self, key):
        return key%10

    def insert(self, key, value):
        self.table[self.hash_func(key)].append(value)


hastable = HashTable_list()
hastable.insert(123, 'Dog')
hastable.insert(14, 'Zebra')
hastable.insert(26, 'Horse')
hastable.insert(84, 'Lion')
hastable.table

hastable.hash_func(16)

