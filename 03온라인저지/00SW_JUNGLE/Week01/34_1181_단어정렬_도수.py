import sys

num=int(sys.stdin.readline())
a={}
for i in range(1,51):
    a[i]=[]

for _ in range(num):
    l=sys.stdin.readline().rstrip()
    if l not in a[len(l)]:
        a[len(l)].append(l)

for i in range(1,51):
    if len(a[i])>0:
        for j in sorted(a[i]):
            print(j)
