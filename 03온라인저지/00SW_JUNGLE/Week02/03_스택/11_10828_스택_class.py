import sys
class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            return -1
            # print("Stack is empty!")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            return -1
            # print("Stack is empty!")

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return len(self) == 0  # 비어있으면 True, 아니면 False 반환


stack = Stack()
n = int(sys.stdin.readline())
for _ in range(n):
    m = sys.stdin.readline().split()

    if m[0] == "push":
        stack.push(m[1])

    elif m[0] == "pop":
        print(stack.pop())

    elif m[0] == "top":
        print(stack.top())

    elif m[0] == "size":
        print(len(stack))
    else:  # "empty":
        if stack.isEmpty():
            print(1)
        else:
            print(0)
