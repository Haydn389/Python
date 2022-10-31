import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    score=[]
    for _ in range(n):
        score.append(tuple(map(int,input().split())))
    a=sorted(score,key=lambda x:x[0])[0]
    b=sorted(score,key=lambda x:x[1])[0]

    print(a,b)
    cnt=0
    for s in score:
        if (s[0]>a[0] and s[1]>a[1]) or (s[0]>b[0] and s[1]>b[1]):
            cnt+=1 

    print(n-cnt)
# 1
# 6
# 6 4
# 4 1
# 5 2
# 1 6
# 2 3
# 3 5
#내 코드 : 4
#정답 : 3