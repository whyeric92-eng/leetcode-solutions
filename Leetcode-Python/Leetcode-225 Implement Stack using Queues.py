import queue

class MyStack:

    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def push(self, x: int) -> None:
        self.q1.put(x)

    def pop(self) -> int:
        while self.q1.qsize() != 1:
            self.q2.put(self.q1.get())
        temp = self.q1.get()
        self.q1, self.q2 = self.q2, self.q1  # 交换引用，而不是让两个变量指向同一对象
        return temp

    def top(self) -> int:
        while self.q1.qsize() != 1:
            self.q2.put(self.q1.get())
        temp = self.q1.get()
        self.q2.put(temp)
        self.q1, self.q2 = self.q2, self.q1
        return temp

    def empty(self) -> bool:
        return self.q1.empty()