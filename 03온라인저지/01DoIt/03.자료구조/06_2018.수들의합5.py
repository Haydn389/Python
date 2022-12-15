import sys

n=int(sys.stdin.readline())

# print(n)

cnt=0
tot=0

for i in range(1,n+1):
    for j in range(1,n+1):
        if tot>n:
            break
        tot+=j
    if tot==n:
        cnt+=1
    tot-=i        

print(cnt)
