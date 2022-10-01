import sys

n=int(sys.stdin.readline())

cnt=0
sum=0
end=0

for start in range(n):
    while sum < n and end < n:
        sum+=end+1
        end+=1

    if sum==n:
        cnt+=1
    sum-=start+1

print(cnt)