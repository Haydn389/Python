import sys
n=int(sys.stdin.readline())

cnt=1
sum=1
start=1
end=1

while end <n:
    if sum==n:
        cnt+=1
        end+=1
        sum+=end
    elif sum <n :
        end+=1
        sum+=end
    else:
        sum-=start
        start+=1


# for start in range(n):
#     while sum < n and end < n:
#         sum+=end+1
#         end+=1
#     if sum==n:
#         cnt+=1
#     sum-=start+1

print(cnt)