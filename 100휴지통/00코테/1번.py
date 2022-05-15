import sys
N=int(sys.stdin.readline().strip())
mine=[ [1, 1], [1, 7], [2, 7], [3, 6], [4, 1], [4, 4], [4, 8], [8, 4], [8, 5], [9, 6] ]

array=[[0]*N for _ in range(N)]

l=len(mine)
dx=[0,1,1,1,0,-1,-1,-1]
dy=[1,1,0,-1,-1,-1,0,1]


for i in mine:
    x,y=i
    array[x-1][y-1]=-1

# for i in range(l):
#     a,b=mine[i][0],mine[i][1]
# for i in range(n):
#     for j in range(n):
#         print(array[i][j],end=" ")
#     print()

x=y=0
for i in range(N):
    for j in range(N):
        if array[i][j]==-1:
            continue
        else:
            for k in range(8):
                nx=i+dx[k]
                ny=j+dy[k]
                if (0<=nx<N and 0<=ny<N):
                    if array[nx][ny]==-1:
                        array[i][j]+=1
        
                
print()
for i in range(N):
    for j in range(N):
        print(array[i][j],end=" ")
    print()