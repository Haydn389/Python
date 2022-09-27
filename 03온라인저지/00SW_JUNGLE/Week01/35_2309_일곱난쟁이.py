from itertools import combinations

a=[]
for i in range(9):
    a.append(int(input()))

result=list(combinations(a,7))
for i in result:
    if sum(i)==100:
        for x in sorted(i):print(x)
        break
