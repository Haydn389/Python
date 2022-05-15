from abc import abstractproperty
import sys
from itertools import combinations
n,m = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))   #int
array=[]
for i in range(len(data)):
    array.append((data[i],i+1))
print(array)

result=list(combinations(array,2))
cnt=0
for i in range(len(result)):
    if result[i][0][0]!=result[i][1][0]:
        cnt+=1

print(cnt)
# print(len(result))