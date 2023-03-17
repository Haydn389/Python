from collections import deque

class Stack:
    def __init__(self):
        self.q=deque()

    def push(self,item):
        self.q.append(item)
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self):
        pass