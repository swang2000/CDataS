'''
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push () and SetOfStacks. pop() should behave identically to a single stack
(that is, pop ( ) should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt (int index) which performs a pop operation on a specific substack.
pg99
'''

class SetofStacks:

    def __init__(self,k):
        self.slists =[]
        self.size = k



    def push(self, a):
        if len(self.slists) == 0 or (len(self.slists[-1]) == self.size):
            self.slists.append([a])
        else:
            self.slists[-1].append(a)



    def pop(self):
        return self.slists[-1].pop(-1)


    def popat(self, i):
        return self.slists[i-1].pop(-1)



ss = SetofStacks(3)
ss.push(2)
ss.push(3)
ss.push(1)
ss.push(8)
ss.push(2)
ss.push(9)
ss.push(12)
ss.push(53)
ss.push(6)
ss.pop()
ss.popat(1)






