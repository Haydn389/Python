import sys
# n, m = map(int, sys.stdin.readline().split())
# a = list(map(int, sys.stdin.readline().split()))
n=5
m=0
a=[-7,-3,-2,5,8]

cnt = 0
pos=[0]*m
flag=[False]*n
tot=0
# def back(i,end,cut):
def back(depth,start):
    global cnt,tot
    # if i == end:
    if tot == m and depth>=1:
        cnt+=1
        return
    for j in range(start,n):
        if flag[j]==False:
            tot+=a[j]
            flag[j]=True
            back(depth+1,j)
            flag[j]=False
            tot-=a[j]

# tot=0
# back(0,3,0)

back(0,0)
# for end in range(1,n+1):
#     tot=0
#     back(0,end,0)

print(cnt)
