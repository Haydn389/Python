import sys
input=sys.stdin.readline

#max_count를 마지막에 한 번만 수행하기!
def solution(N, A):
    cnt=[0]*N
    m1=0 # 해당 루프에서의 최댓값
    m2=0 #전체 최대값
    for v in A:
        if v<N+1:
            if cnt[v-1]<m2:
                cnt[v-1]=m2+1
            else:
                cnt[v-1]+=1
            if m1<cnt[v-1]:
                m1=cnt[v-1]
            # print(f"v:{v},cnt,{cnt}")
        else:
            m2=m1
            # print(f"v:{v},cnt,{cnt}")

    cnt=[m2 if i<m2 else i for i in cnt ]    #업데이트 안된 원소에 대해 고려
    return cnt

N=int(input())
A=list(map(int,input().split()))
print(solution(N, A))