import sys
input=sys.stdin.readline
#bin(N).lstrip('0b') 내장 라이브러리 이용
def solution(N):
    a=[]
    # while N>0:
    #     a.append(N%2)
    #     N//=2
    a = bin(N).lstrip('0b')
    a=list(map(int,a))
    a.reverse()

    res=[]
    cnt=0
    while a:
        if a.pop()==0:
            cnt+=1
        else:
            res.append(cnt)
            cnt=0
    return max(res)

N=int(input())
print(solution(N))