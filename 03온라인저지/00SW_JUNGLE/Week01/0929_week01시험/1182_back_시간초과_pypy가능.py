import sys
# n, m = map(int, sys.stdin.readline().split())
# a = list(map(int, sys.stdin.readline().split()))
n=5
m=0
a=[-7,-3,-2,5,8]

cnt = 0
pos=[0]*m
flag=[False]*n

def back(i,depth,cut):
    global tot,cnt
    if i == depth:
        if tot==m:
            cnt+=1
        return
    for j in range(n):
        if flag[j]==False and cut<=j:
            tot+=a[j]
            flag[j]=True
            back(i+1,depth,j)
            flag[j]=False
            tot-=a[j]

# tot=0
# back(0,3,0)
for depth in range(1,n+1):
    tot=0
    back(0,depth,0)

print(cnt)
