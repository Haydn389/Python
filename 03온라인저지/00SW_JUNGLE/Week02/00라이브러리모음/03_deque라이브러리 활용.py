from collections import deque

dq = deque()
print(dq)  # print결과 : deque([])

dq.append(5)
dq.append(6)
print(dq)  # print결과 : deque([5, 6])

dq.extend([7, 8, 9])
print(dq)  # print결과 : deque([3, 4, 5, 6, 7, 8, 9])

dq.extendleft([2, 1, 0])
print(dq)  # print결과 : deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

dq.remove(7)
dq.remove(8)
dq.remove(9)
print(dq)  # print결과 : deque([0, 1, 2, 3, 4, 5,6])

popValue = dq.pop()
print(popValue)  # print결과 : 6
print(dq)  # print결과 : deque([0, 1, 2, 3, 4, 5])

popValue = dq.popleft()
print(popValue)  # print결과 : 0
print(dq)  # print결과 : deque([1, 2, 3, 4, 5])


dq.append(7)
dq.append(8)
print(dq)  # print결과 : deque([1, 2, 3, 4, 5])
dq.rotate(1)
print(dq)  # print결과 : deque([5, 1, 2, 3, 4])
dq.rotate(-1)
print(dq)  # print결과 : deque([1, 2, 3, 4, 5])
dq.rotate(-1)
print(dq)  # print결과 : deque([2, 3, 4, 5, 1])