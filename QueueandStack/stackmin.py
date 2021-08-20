'''
Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.
'''

class Stack_min:

    def __init__(self):
        self.contain = []
        self.smin = []
        self.size = 0

    def add(self,k):
        self.contain.append(k)
        if len(self.smin) == 0 or k < self.smin[-1]:
            self.smin.append(k)

    def pop(self):
        if self.contain[-1] == self.smin[-1]:
            self.smin.pop(-1)
        return self.contain.pop(-1)

    def getmin(self):
        return self.smin[-1]



smin = Stack_min()
smin.add(5)
smin.add(3)
smin.add(8)
smin.add(7)
smin.add(4)
smin.add(2)
smin.add(9)

smin.getmin()
smin.pop()
smin.getmin()
smin.pop()
smin.getmin()
smin.pop()
smin.getmin()





