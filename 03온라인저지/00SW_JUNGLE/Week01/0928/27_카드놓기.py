from itertools import permutations
t=int(input())
k=int(input())
data=[]
for i in range(t):
    data.append(input())

print(data)

all=permutations(data,k)

ans=[]
for per in all:
    ans.append("".join(per))

    
