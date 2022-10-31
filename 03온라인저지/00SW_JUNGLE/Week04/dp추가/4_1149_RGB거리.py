import sys
input=sys.stdin.readline
n=int(input())
house=[]
for _ in range(n):
    house.append(list(map(int,input().split())))

# print(house)

d=[[0]*3 for _ in range(n+1)]
d[1][0]=house[0][0]
d[1][1]=house[0][1]
d[1][2]=house[0][2]

for i in range(2,n+1):
    d[i][0]=min(d[i-1][1],d[i-1][2])+house[i-1][0]
    d[i][1]=min(d[i-1][0],d[i-1][2])+house[i-1][1]
    d[i][2]=min(d[i-1][0],d[i-1][1])+house[i-1][2]

print(min(d[n]))