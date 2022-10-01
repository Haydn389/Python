import sys

n= int(sys.stdin.readline().strip())
m=n
pos=[None]*m
v1=[False]*n
v2=[False]*(2*n-1)
v3=[False]*(2*n-1)

cnt=0
def set(i):
    global cnt
    if i==m:
        # print(*pos)
        cnt+=1
        return
    # else:
    for j in range(n):
        if not v1[j] and not v2[i+j] and not v3[i-j+(n-1)]:
            pos[i]=j
            v1[j]=v2[i+j]=v3[i-j+(n-1)]=True
            set(i+1)
            v1[j]=v2[i+j]=v3[i-j+(n-1)]=False

set(0)
print(cnt)