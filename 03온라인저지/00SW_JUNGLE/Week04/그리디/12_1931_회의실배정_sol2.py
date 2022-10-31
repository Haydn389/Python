import sys
input=sys.stdin.readline
n=int(input())
m=[]
for _ in range(n):
    m.append(tuple(map(int,input().split())))
m.sort(key=lambda x:(x[1],x[0]))
res=[m[0]]
for i in range(1,len(m)):
    if res[-1][1]<=m[i][0]:
        res.append(m[i])
print(len(res))
