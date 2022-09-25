import sys

t = int(sys.stdin.readline().rstrip())
arr=[]
for _ in range(t):
    arr.append(int(sys.stdin.readline()))
arr.sort()
# print(t)
# print(arr)
# print(arr)

for a in arr:
    print(a)