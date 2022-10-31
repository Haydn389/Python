import sys
input=sys.stdin.readline

n=int(input())
a=[0]
tot=0
for _ in range(n):
    score=int(input())
    a.append(score)
    tot+=score
d=[0]*301

if n<=2:
    print(tot)
    exit(0)

d[1]=a[1]
d[2]=a[2]
d[3]=a[3]
for k in range(4,n+1):
    d[k]=min(d[k-2],d[k-3])+a[k]
# print(d)
print(tot-min(d[n-1],d[n-2]))
