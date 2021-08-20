
class MinStack:

    def __init__(self):
        self.min_val = []
        self.list = []

    def push(self, val):
        if (len(self.min_val) == 0) or (val < self.min_val[-1]):
            self.min_val.append(val)
        self.list.append(val)

    def pop(self):
        if self.list[-1] == self.min_val[-1]:
            self.min_val.pop()
        return self.list.pop()

    def getMin(self):
        return self.min_val[-1]


mins = MinStack()
mins.push(5)
mins.push(4)
mins.push(7)
mins.push(2)

mins.getMin()
mins.pop()
mins.getMin()


