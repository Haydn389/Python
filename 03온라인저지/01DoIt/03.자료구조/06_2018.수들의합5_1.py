import sys
n=int(sys.stdin.readline())
# a=[i for i in range(1,n+1)]
# print(a)

cnt=0
sum=0
end=0

for start in range(n):
    while sum < n and end < n:
        print(sum,end=" ")
        sum+=end+1
        end+=1
    if sum==n:
        cnt+=1
    sum-=start+1
    print()

print(cnt)