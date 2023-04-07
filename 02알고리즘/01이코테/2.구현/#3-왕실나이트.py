import sys
input = sys.stdin.readline

move=input().rstrip()
s=['a','b','c','d','e','f','g','h']
dx=[-2,-1,1,2,2,1,-1,-2]
dy=[1,2,2,1,-1,-2,-2,-1]
x=s.index(move[0])+1
y=int(move[1])
ans=0
for i in range(8):
    nx=x+dx[i]
    ny=y+dy[i]
    if 1<=nx<=8 and 1<=ny<=8:
        ans+=1

print(ans)