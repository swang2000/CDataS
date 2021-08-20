'''
Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
'''

class Queuebystacks:

    def __init__(self):
        self.snew = []
        self.sold = []

    def push(self, a):
        self.snew.append(a)

    def pop(self):
        if len(self.sold) == 0:
            while len(self.snew) >0:
                self.sold.append(self.snew.pop(-1))
            return self.sold.pop(-1)
        else:
            return self.sold.pop(-1)



qs = Queuebystacks()
qs.push(3)
qs.push(5)
qs.push(6)
qs.push(9)
qs.push(4)
qs.push(2)
qs.pop()
qs.pop()


