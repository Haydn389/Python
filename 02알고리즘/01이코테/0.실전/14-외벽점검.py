from itertools import permutations
import sys

#weak 길이만큼 순회하며 시작위치를 변경시기고
#각 경우마다 dist의 모든 조합을 가지고 확인
def solution(n, weak, dist):
    lim=len(weak)
    weak=weak + [n+w for w in weak] #[1, 5, 6, 10, 13, 17, 18, 22]
    answer=sys.maxsize
    for s in range(lim):#시작위치 변경 [1,5,6,10]
        end=s+lim #끝 위치 지정 (탈출조건)
        temp=0
        for permu in permutations(dist,len(dist)): # 1 2 3 4
            cnt=0
            idx=s
            for i in permu: # 1, 2, 3, 4
                cnt+=1
                next=weak[idx]+i #현재위치로부터 증가된 값 계산
                idx+=1 #위치이동
                while next >= weak[idx]: #증가된 값보다 작은동안 idx++
                    if idx>=end:
                        break
                    idx+=1                    
                if idx>=end:#탈출조건 확인
                    temp=1 # 모든 값을 순회했을 때 1 저장
                    break
            if temp!=0: # weak를 모두 한번씩 순회했을 때에만 업데이트
                answer= min(cnt,answer)

    if answer == sys.maxsize:
        return -1
    return answer   

n=20
weak=[3,6,10,12,16,17]
dist=[1,2,3]
print(solution(n, weak, dist))