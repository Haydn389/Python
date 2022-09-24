import itertools
t=int(input())
k=int(input())
data=[]
for i in range(t):
    data.append(input())
res=[]
for x in itertools.permutations(data,k):
    res.append("".join(list(x)))
print(len(set(res)))
