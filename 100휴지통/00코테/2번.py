import sys

N,K=map(int,sys.stdin.readline().split())
# T= [[1,3],[3,4],[2,4],[2,4],[2,3],[1,2]]	
# T= [[1,2],[3,4],[2,4],[6,6],[3,4],[2,3]]
T= [[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]]

data=[[0]*K for _ in range(N)]
for i in range(len(T)):
    x,y=T[i][0],T[i][1]
    # print(x,y)

    for j in range(x-1,y):
        data[i][j]=1


for i in range(N):
    for j in range(K):
        print(data[i][j],end=" ")
    print()

cnt=0
for i in range(K):
    for j in range(N):
        if data[j][i]!=0:
            cnt+=1
            break

print(cnt)