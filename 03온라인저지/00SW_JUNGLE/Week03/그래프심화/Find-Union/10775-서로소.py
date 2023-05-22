import sys
input=sys.stdin.readline

def find(par,x):
    if par[x]!=x:
        return find(par,par[x])
    return x
    #     par[x]=find(par,par[x])
    # return par[x]

def union(par,a,b):
    a=find(par,a)
    b=find(par,b)
    if a<b:
        par[b]=a
    else:
        par[a]=b

g=int(input())
p=int(input())
planes=[]
par=[0]*(g+1)
for i in range(1,g+1):
    par[i]=i
for _ in range(p):
    planes.append(int(input())) 
res=0
# print(par)
for i in planes:
    if i==find(par,i):
        res+=1
    # print(i,find(par,i))
    union(par,i-1,i)
    # print(par)
    # if find(par,i-1)!=find(par,i):#다른집합
    #     union(par,i-1,i)
    #     res+=1
print(res)
        