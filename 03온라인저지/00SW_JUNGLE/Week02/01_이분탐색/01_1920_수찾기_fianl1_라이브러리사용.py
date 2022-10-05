from bisect import bisect_left, bisect_right
# a = [1, 2, 4, 4, 8]
# x = 4

# print(bisect_left(a, x)) # 2
# print(bisect_right(a, x)) #4
import sys
input=sys.stdin.readline

n= int(input())
a=list(map(int,input().split()))
a.sort() #[1,2,3,4,5]
m= int(input())
nums=list(map(int,input().split()))
for num in nums:
    if(bisect_right(a,num)-bisect_left(a,num)):
        print(1)
    else: print(0)