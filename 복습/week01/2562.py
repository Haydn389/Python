import sys
input = sys.stdin.readline

a=[]
for _ in range(9):
    a.append(int(input()))

max_val=max(a)
print(max_val)
print(a.index(max_val)+1)