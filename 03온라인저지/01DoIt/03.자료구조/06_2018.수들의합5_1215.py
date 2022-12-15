import sys

n=int(sys.stdin.readline())

start=1
end=1
cnt=1
sum=1
while (end<n):
    if sum == n:
        # print("cnt++!!")
        cnt+=1
        end+=1
        sum+=end
    elif sum > n:
        sum-=start
        start+=1
    else:
        end+=1
        sum+=end
    # print('-----')
    # print(sum)
print(cnt)