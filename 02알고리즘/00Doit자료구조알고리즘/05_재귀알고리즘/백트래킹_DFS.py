import sys
n, m = map(int, sys.stdin.readline().split())

pos=[0]*m
flag=[False]*n
cnt=0

def set(i):
    global cnt
    if i ==m:
        print(pos)
        cnt+=1
    else:
        for j in range(n):
            if flag[j]==False:
                pos[i]=j
                flag[j]=True
                set(i+1)
                flag[j]=False

set(0)