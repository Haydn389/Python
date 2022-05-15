import sys
n,m=map(int,sys.stdin.readline().split())
data=[[0]*m for _ in range(n)]
a = int(sys.stdin.readline())
for i in range(a):
    l,d,x,y = map(int,sys.stdin.readline().split())
    if(d==1):
        for j in range(l):
            data[(x-1)+j][y-1]=1            
    else: 
        for j in range(l):
            data[x-1][y+(j-1)]=1  


for i in range(n):
    for j in range(m):
        print(data[i][j],end=' ')
    print()