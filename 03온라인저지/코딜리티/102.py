import sys
input=sys.stdin.readline

def solution(S):
    # a=S.split("A")
    # b=S.split("B")
    # print(a)
    # print(b)
    # stack=[]
    a=[]
    b=[]
    for i,p in enumerate(S):
        if p=='A':
            a.append(i)
        else:
            b.append(i)
    print(a)
    print(b)
    cnt=0
    a_sum=[]
    b_sum=[]
    for i in range(len(a)-1):
        if a[i+1]-a[i]>1:
            cnt+=1
            a_sum.append(a[i+1]-a[i]-1)
    print(a_sum)
    return cnt + a[0]

S=input().rstrip()
print(solution(S))