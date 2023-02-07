import sys
input = sys.stdin.readline

a=[]
for _ in range(9):
    a.append(int(input().strip()))

print(a)
print(a.index(57))