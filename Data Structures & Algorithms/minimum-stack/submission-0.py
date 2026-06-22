class MinStack:

    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        self.s.append(val)

    def pop(self) -> None:
        return self.s.pop(len(self.s)-1)

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return min(self.s)
