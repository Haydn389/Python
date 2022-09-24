import sys
n,m=map(int,sys.stdin.readline().split())
# n,m=4,2
#1부터 N까지 자연수 중에서 중복없이 M 개를 고른 (길이가 M인)수열

def put():
    global cnt
    for i in range(m):
        print(f"{pos[i]}",end=" ")
    print()
    cnt+=1

def set(i):
    for j in range(1,n+1):
        if not flag[j]:
            pos[i]=j
            
            if i==(m-1):
                put()
            else:
                flag[j]=True
                set(i+1)
                flag[j]=False
pos=[0]*m
flag=[False]*(n+1)
cnt=0
set(0)
print(cnt)

# pos=[0]*m
# flag=[False]*(n+1)
# cnt=0
# set(1)
# print(cnt)