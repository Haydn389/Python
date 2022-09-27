import sys
sys.setrecursionlimit(10**8) # 10^8 까지 늘림.
m=n=int(sys.stdin.readline())
# n,m=map(int,sys.stdin.readline().split())
# data=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
data=[[0, 10, 15, 20], [5, 0, 9, 10], [6, 13, 0, 12], [8, 8, 9, 0]]
print(data)
pos=[0]*m
flag=[False]*n
ans=1e9
def set(i):
    global ans
    if i==m:
        # for k in range(n-1):
        #     print(pos[k])
        print(pos)
        s=0
        for k in range(n):
            s+=data[pos[k%n]][pos[(k+1)%n]]
        print(s)
        if s<ans:ans=s
        
        # print(data[pos[0]][pos[1]])
        # print(data[pos[1]][pos[2]])
        # print(data[pos[2]][pos[3]])
        # print(data[pos[3]][pos[0]])
        # for i in pos:
        #     print(i,end=" ")
        #     data[i]
        # print()
    else:
        for j in range(n):
            if flag[j]==False:
                pos[i]=j
                flag[j]=True
                set(i+1)
                flag[j]=False

set(0)
print(ans)