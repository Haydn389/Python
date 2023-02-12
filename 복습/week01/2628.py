import sys
input=sys.stdin.readline
a,b=map(int,input().split())
r=[0,b]
c=[0,a]
for _ in range(int(input())):
    n,m=map(int,input().split())
    if n:
        c.append(m)
    else:
        r.append(m)
r.sort()
c.sort()
# print(r,c)

max_r=max_c=0
for i in range(1,len(r)):
    res=r[i]-r[i-1]
    if max_r < res:
        max_r=res
for i in range(1,len(c)):
    res=c[i]-c[i-1]
    if max_c < res:
        max_c=res
print(max_r*max_c)
