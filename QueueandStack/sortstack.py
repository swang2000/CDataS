'''
Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.
'''

class Sortstack:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.temp = None


    def push(self,a, i=1):
        if i == 1:
            self.s1.append(a)
        elif i == 2:
            self.s2.append(a)

    def pop(self, i=1):
        if i == 1:
            return self.s1.pop(-1)
        elif i ==2:
            return self.s2.pop(-1)

    def peek(self, i=1):
        if i == 1:
            return self.s1[-1]
        if i == 2:
            return self.s2[-1]

    def sort(self):
        while len(self.s1) > 0:
            self.temp = self.pop(1)
            if len(self.s2) == 0:
                self.push(self.temp, 2)
            else:
                while self.temp > self.peek(2):
                    self.push(self.pop(2), 1)
                self.push(self.temp, 2)
        return self.s2

    def printS(self, i=1):
        if i == 1:
            for j in self.s1:
                print(str(j))
        if i == 2:
            for j in self.s2:
                print(str(j))

ss = Sortstack()
ss.push(8)
ss.push(3)
ss.push(5)
ss.push(4)
ss.push(6)
ss.push(7)
ss.push(9)
ss.sort()
ss.printS(2)



