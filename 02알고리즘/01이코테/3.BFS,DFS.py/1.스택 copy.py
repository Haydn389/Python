from collections import deque

queue=deque()

queue.append(5)
queue.append(5)
queue.append(5)
queue.append(5)
queue.popleft()
queue.append(5)
queue.append(5)
queue.popleft()

print(queue)
queue.reverse()