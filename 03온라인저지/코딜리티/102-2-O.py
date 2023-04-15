import sys
input=sys.stdin.readline

def solution(s):
    n=len(s)
    idx_a=idx_b=None
    cnt_a=cnt_b=0
    for i in range(n):
        if s[i]=='A':
            idx_a=i 
            break
        cnt_a+=1
    for i in range(n-1,0,-1):
        if s[i]=='B':
            idx_b=i
            break
        cnt_b+=1
    if idx_a>idx_b:
        return min(cnt_a,cnt_b)
    cnt_ab=0
    while (idx_a<idx_b):
        if s[idx_a:idx_a+2]=='AB':
            cnt_ab+=1
        idx_a+=1       
    tot_a=list(s).count('A')
    tot_b=n-tot_a
    return min(tot_a,tot_b,cnt_a+cnt_b+cnt_ab-1)


S=input().rstrip()
print(solution(S))