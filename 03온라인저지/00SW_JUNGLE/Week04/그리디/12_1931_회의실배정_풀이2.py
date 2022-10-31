import sys
input=sys.stdin.readline
n=int(input())
m=[]
for _ in range(n):
    m.append(tuple(map(int,input().split())))
m.sort(key=lambda x:(x[1],x[0]))
# sort 기준1 끝시간, 기준2 시작시간 
# ex) lambda x:(x[1],x[0])  --> [(0,1),(1,1),(1,2),(2,3)]
# ex) lambda x:(x[1])       --> [(1,1),(0,1),(1,2),(2,3)]

# print(m)
res=[m[0]]

for i in range(1,len(m)):
    if res[-1][1]<=m[i][0]:
        res.append(m[i])

print(len(res))

# 4
# 1 1
# 0 1
# 1 2
# 2 3