

class SetStacks:

    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.lists = []
        list = []
        self.lists.append(list)

    def push(self, val):
        if len(self.lists[len(self.lists)-1]) < self.capacity:
            self.lists[len(self.lists)-1].append(val)
        else:
            list = []
            list.append(val)
            self.lists.append(list)


    def pop(self):
        d = self.lists[len(self.lists) - 1].pop()
        if len(self.lists[len(self.lists) - 1]) ==0:
            del self.lists[-1]
        return d



sets = SetStacks()
sets.push(5)
sets.push(3)
sets.push(6)
sets.push(7)
sets.push(1)
sets.push(11)
sets.lists
sets.pop()
sets.lists

sets.pop()
sets.lists
