import sys
input = sys.stdin.readline
n = int(input())
a = sorted(list(map(int, input().split())))
pl = 0
pr = n-1
res = 1e10
res=sys.maxsize
# res = 2e+9+1 

while pl < pr:
    tot = a[pl]+a[pr]
    temp=abs(tot)
    if temp < res:
        res = temp
        ans = a[pl], a[pr]
    if tot == 0:
        break
    elif tot < 0:
        pl += 1
    else:
        pr -= 1
print(*ans)

