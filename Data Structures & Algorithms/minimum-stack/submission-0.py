class MinStack:

    def __init__(self):
        self.minimum = []
        self.ordering = []
    def push(self, val: int) -> None:
        self.ordering.append(val)
        if (len(self.minimum)==0):
            self.minimum.append(val)
        else:
            self.minimum.append(min(val,self.minimum[-1]))

    def pop(self) -> None:
        self.ordering.pop()
        self.minimum.pop()


    def top(self) -> int:
        return self.ordering[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
