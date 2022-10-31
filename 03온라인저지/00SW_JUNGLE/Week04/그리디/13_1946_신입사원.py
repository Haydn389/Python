import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    score=[]
    for _ in range(n):
        score.append(tuple(map(int,input().split())))
    score.sort()
    high_rank=score[0]
    cnt=1
    for s in score[1:]:
        if s[1]<high_rank[1]:
            high_rank=s
            cnt+=1
    print(cnt)
