import sys
input=sys.stdin.readline

def solution(A):
    nums={} 
    for key in A:
        if key in nums:
            nums[key]+=1
        else:
            nums[key]=1
    print(nums)
    ans=0
    for k,v in nums.items():
        if k == v:
            ans=max(ans,k)
    return ans
A=list(map(int,input().split()))
print(solution(A))