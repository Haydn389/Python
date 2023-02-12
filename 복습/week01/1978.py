import sys,math
input = sys.stdin.readline

def solve(num):
    # print((num))
    for i in range(2,int(math.sqrt(num))+1):
        if num % i ==0: return 0
    return 1        

n=int(input())
a=list(map(int,input().split()))
cnt=0
for x in a:
    if x ==1:continue
    cnt+=solve(x)
print(cnt)