class MyStack:

    def __init__(self):
        self.s = []
        self.curlen = 0
        

    def push(self, x: int) -> None:
        self.s.append(x)
        self.curlen+=1

    def pop(self) -> int:
        val = self.s[self.curlen-1]
        del self.s[self.curlen-1]
        self.curlen-=1
        return val

    def top(self) -> int:
        return self.s[self.curlen-1]

    def empty(self) -> bool:
        if self.curlen==0:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()