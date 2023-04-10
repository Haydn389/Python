from itertools import combinations
import sys

input=sys.stdin.readline

n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
homes=[]
stores=[]
for i in range(n):
    for j in range(n): 
        if a[i][j]==1:
            homes.append([i,j,[]])
        if a[i][j]==2:
            stores.append((i,j))
res={}
for home in homes:
    for store in stores:
        dist=abs(store[0]-home[0])+abs(store[1]-home[1])
        home[2].append([(store[0],store[1]),dist])

        
print(n,m)
print(a)
temp=0
for home in homes:
    home[2].sort(key=lambda x:x[1])
    temp+=home[2][0][1]
for x in homes:
    print(x)
# ans=list(res)
ans=stores
print("ans",ans)
if len(ans)<m:
    print(temp)
else:
    answer=sys.maxsize
    for i in combinations(ans,m):
        com_store=list(i)
        # print(">>>com_store",com_store)
        temp=0
        for home in homes:
            for k in home[2]:
                if k[0] in com_store:
                    temp+=k[1]
                    break
        # print(temp)
        answer=min(answer,temp)
        
    print(answer)