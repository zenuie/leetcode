class MyQueue:

    def __init__(self):
        # 建立一個queue
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop(0)

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0

test = MyQueue()
print(test)
print(test.push(1))
print(test.push(2))
print(test.peek())
print(test.pop())
print(test.empty())
