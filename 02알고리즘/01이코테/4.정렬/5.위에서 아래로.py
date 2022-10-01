import sys
n = int(sys.stdin.readline())
a=[]
for _ in range(n):
    a.append(int(sys.stdin.readline()))

a.sort(reverse=True)

for i in a:
    print(i,end=" ")
