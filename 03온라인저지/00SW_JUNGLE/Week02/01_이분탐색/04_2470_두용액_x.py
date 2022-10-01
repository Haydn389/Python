from itertools import combinations
import sys

n=int(sys.stdin.readline())

a=list(map(int,sys.stdin.readline().split()))

b=[abs(i) for i in a]
res=max(b)
ans1=0
ans2=0
for com in combinations(a,2):
    print(com)
    print(abs(com[0]+com[1]))
    print("res전",res)
    if abs(com[0]+com[1])<res:
        res=abs(com[0]+com[1])
        ans1,ans2=com[0],com[1]
    print("res후",res)
    print("-"*50)
        

print(ans1,ans2)