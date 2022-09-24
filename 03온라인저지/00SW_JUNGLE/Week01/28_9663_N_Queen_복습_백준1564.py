#nPr 구현하기
import sys

n,m=map(int,sys.stdin.readline().split())
# n,m=4,3
pos=[0]*m
flag_1=[False]*n
cnt=0

def put():
    for i in range(m):
        print(f"{pos[i]+1}",end=" ")
    print()

def N_Queen(i):
    global cnt
    for j in range(n):
        if (not flag_1[j]):
            pos[i]=j
            if i==(m-1):
                put()
                cnt+=1
            else:
                flag_1[j]=True
                N_Queen(i+1)
                flag_1[j]=False

N_Queen(0)
print(cnt)