from itertools import combinations
import sys
n=int(sys.stdin.readline().strip())

data=list(map(int,sys.stdin.readline().split()))

com=[]

com=list(combinations(data,2))
print(com)
sum=0
for c in com:
    i,j=c
    sum+=i*j

# for i in range(len(com)):
#     sum+=com[i][0]*com[i][1]

print(sum)