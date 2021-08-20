
class MyQueue:
    def __init__(self):
        self.newstack = []
        self.oldstack = []

    def push(self, val):
        self.newstack.append(val)


    def shiftstacks(self):
        while len(self.newstack) >0:
            self.oldstack.append(self.newstack.pop())

    def pop(self):
        if len(self.oldstack) == 0:
            self.shiftstacks()
        if len(self.oldstack)==0:
            return print('The Queue is empty')
        else:
            return self.oldstack.pop()


myQ = MyQueue()
myQ.push(3)
myQ.push(5)
myQ.push(4)
myQ.push(1)
myQ.newstack
myQ.pop()
myQ.pop()
myQ.pop()

