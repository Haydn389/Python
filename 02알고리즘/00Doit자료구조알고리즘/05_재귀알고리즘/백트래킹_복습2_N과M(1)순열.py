# 백트래킹 연습(순열)
# nPm : 서로 다른 n개중에 r개를 선택하는 경우의 수를 의미합니다. (순서 상관 있음)
import sys
n, m = map(int, sys.stdin.readline().split())

pos=[0]*m
flag=[False]*n
cnt=0
def set(i):
    global cnt
    if i==m:
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
print(cnt)