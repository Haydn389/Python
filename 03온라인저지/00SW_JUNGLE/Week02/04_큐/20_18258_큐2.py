from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
queue = deque()

for _ in range(n):
    cmd=input().split()
    if cmd[0]=="push":
    # def push(x):
        queue.append(int(cmd[1]))

    if cmd[0]=="pop":
    # def pop():
        try:
            print(queue.popleft())
        except IndexError:
            print(-1)

    if cmd[0]=="size":
    # def size():
        print(len(queue))

    if cmd[0]=="empty":
    # def empty():
        if queue:   #비어있지 않으면
            print(0)
        else:       #비어있으면
            print(1)

    if cmd[0]=="front":
    # def front():
        try:
            print(queue[0])
        except IndexError:
            print(-1)
            
    if cmd[0]=="back":
    # def back():
        try:
            print(queue[-1])
        except IndexError:
            print(-1)
