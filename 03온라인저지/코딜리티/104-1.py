import sys
input=sys.stdin.readline

def solution(S):
    a=[]
    idx_min={}
    idx_max={}
    for i in range(len(S)-1):
        a.append((i,S[i:i+2]))
    # print(a)
    for i in a:
        if i[1] in idx_min.keys():
            idx_max[i[1]]=i[0]
        else:
            idx_min[i[1]]=i[0]      
    ans=0
    for k,v in idx_max.items():
        ans=max(ans,v-idx_min[k])
    # print(idx_min)
    # print(idx_max)
    if ans==0:
        return -1
    return ans

A=input().rstrip()
print(solution(A))