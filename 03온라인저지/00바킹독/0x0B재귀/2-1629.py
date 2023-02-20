import sys
input=sys.stdin.readline
a,b,c=map(int,input().split())

#시간초과 발생하는 코드
# def solve(a,b,c):
#     ans=1
#     while b>0:
#         ans*=a
#         b-=1
#     return ans%c

#재귀로 구현하기
def solve2(a,b,c):
    if b==1:
        return a%c
    temp=solve2(a,b//2,c)
    if b%2==0:
        return temp*temp%c
    else:
        return temp*temp*a%c

print(solve2(a,b,c))