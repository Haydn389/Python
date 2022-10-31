import sys
input=sys.stdin.readline

c,n=map(int,input().split())

hotel=[[0,0]]
for _ in range(n):
    hotel.append(list(map(int,input().split())))

# hotel.sort()
print(hotel)
k=16

d=[[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        if j<hotel[i][0]:
            d[i][j]=d[i-1][j]
        else:
            d[i][j]=max(d[i-1][j],d[i-1][j-hotel[i][0]]+hotel[i][1])

for p in d:
    print(*p)
# print(d[n][k])