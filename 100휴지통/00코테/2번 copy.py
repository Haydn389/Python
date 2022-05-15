import sys

N,K=map(int,sys.stdin.readline().split())
# T= [[1,3],[3,4],[2,4],[2,4],[2,3],[1,2]]	
T= [[1,2],[3,3],[2,3],[5,6],[3,3],[2,3]]

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
check=[0]*K
cnt=0
for i in range(K):
    for j in range(N):
        if data[j][i]!=0:
            check[i]=1
            break

# print(check)
res=[0]*K
pos=0
for c in check:
    if c==0:
        pos+=1
    else:
        res[pos]+=1

print(max(res))
# check2=list(map(str,check))
# print(check2)




# cnt=0
# for i in range(K):
#     for j in range(N):
#         if data[j][i]!=0:
#             cnt+=1
#             break

