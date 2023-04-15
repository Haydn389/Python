import sys
input=sys.stdin.readline

#idea 
def solution(A):
    a=[]
    for i,v in enumerate(A):
        a.append((i+v,1))
        a.append((i-v,-1))
    a.sort()
    res=0   #겹치는 수
    opens=0 #현재 열린 원의 갯수

    for i,v in enumerate(a):
        if v[1]==1:
            opens-=1
            # print(opens)
        else:#현재 열려있는 원의 개수만큼 누적!
            res+=opens
            # print("+",opens)
            opens+=1
            # print(opens,res)
    if res > 10000000: return -1
    return res

A=list(map(int,input().split()))
print(solution(A))