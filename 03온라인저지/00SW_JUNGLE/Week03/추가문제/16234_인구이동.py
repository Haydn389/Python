import sys
from collections import deque
input=sys.stdin.readline
n,l,r=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def check(a):#멈춰야하는지 확인 : 차이가 범위내에 들어오는 게 하나라도 있으면 True, 없으면(종료해야하면) False
    global n 
    for i in range(n):
        for j in range(n):
            for k in range(4):
                nx=i+dx[k]
                ny=j+dy[k]
                if 0<=nx<n and 0<=ny<n:
                    if l <= abs(a[i][j]-a[nx][ny]) <= r:
                        return True
    return False

def bfs(x,y):
    global a,flag
    open=[]
    temp=0
    tot=0
    visited[x][y]=1
    q=deque([(x,y)])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and l<=abs(a[x][y]-a[nx][ny])<=r:
                flag=False
                if not open:
                # if temp==0:
                    open.append((x,y))
                    tot+=a[x][y]
                open.append((nx,ny))
                tot+=a[nx][ny]
                q.append((nx,ny))
                visited[nx][ny]=2
                temp+=1
    print("===open",len(open),sorted(open))

    if open:
        avg=tot//len(open)
        for x,y in open:
            a[x][y]=avg
        # for p in visited:
        #     print(p)
        # print("-"*30)

for p in a:
    print(p)
print("*"*30)

#한번 다 돌고 나면
# if open:
#     print(tot//len(open))
# for x,y in open:
#     a[x][y]=

cnt=0
flag=True
while True:
    visited=[[0]*n for _ in range(n)]
    # open=[]
    
    print(">>>>>자~ 드가자",cnt)
    flag=True
    for p in a:
        print(p)
    print("^"*30)
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                print(">>>>>>",i,j)
                bfs(i,j)
    for p in visited:
        print(p)
    print("-"*30)
    # if len(open)==0:
    if flag==True:
        print(cnt)
        break
    # if len(open)==n*n:
    #     print(cnt+1)
    #     break

    cnt+=1

# print(cnt)

# opne이 비어있으면 return 0
# 그외에는반복
# open이 n*n이면 stop
