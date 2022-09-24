#N_Queen 풀기
import sys

n,m=map(int,sys.stdin.readline().split())
# n,m=4,3
pos=[0]*m
flag_1=[0]*n
flag_2=[0]*n
flag_3=[0]*n
cnt=0

def put():
    for i in range(m):
        print(f"{pos[i]}",end=" ")
    print()

def N_Queen(i):
    global cnt
    for j in range(n):
        if (not flag_1[j] and not flag_2[j] and not flag_3[j]):
            pos[i]=j
            if i==(m-1):
                put()
                cnt+=1
            else:
                flag_1[j]=True
                N_Queen(i+1)
                flag_2[j]=False

N_Queen(0)
print(cnt)