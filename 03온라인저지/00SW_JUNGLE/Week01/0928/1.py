import sys
from itertools import permutations
# n=int(sys.stdin.readline().rstrip())
# m=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
n=4
m=[[123, 1, 1],
[356, 1, 0],
[327, 2, 0],
[489, 0, 1]]

# per = list(permutations(range(1,10),3))
# print(per)

cnt=0

for p in permutations(range(1,10),3):
    # p=(3,2,8)
    # tot=0
    for i in m:
        check=False
        strike=set()
        temp=0
        for j in range(3):
            if str(p[j])==str(i[0])[j]:
                temp+=1
                strike|=set(str(p[j]))
        if temp!=i[1]:
            break
        elif len((set(map(str,p))&set(str(i[0])))-strike)!=i[2]:
            break
        else:
            # tot+=1
            check=True
    # if tot==n:
    if check:
        cnt+=1

print(cnt)
