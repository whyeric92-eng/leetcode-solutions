class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min_stack or value <self.min_stack[-1]:
            self.min_stack.append(value)
        else:
            self.min_stack.append(self.min_stack[-1])
#最巧妙的地方就是如果当前value不是最小值的话，直接append当前最小值即可

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()