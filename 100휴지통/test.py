import sys
from itertools import combinations
# a = ['1','2','3','4','5']
a=[1,2,3,4,5]
a=[str(k) for k in a]
# a=sys.stdin.readline().split()

permute=[]
for i in range(1,11):
    permute+=list(combinations(a,i))

print(permute)
# print(len(permute))

new=[int("".join(c)) for c in permute]
print(new)