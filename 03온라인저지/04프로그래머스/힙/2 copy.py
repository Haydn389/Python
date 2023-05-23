from heapq import heappush, heappop, heapify
from collections import deque
def solution(jobs):
    jobs=deque(jobs)
    now=0
    wait=0
    start=-1
    cnt=0
    h=[]
    
    while True:
        #현재작업의 시작시간~현재시간 사이에 요청들어온 작업모두 저장
        for j in jobs:
            if start<j[0]<=now:
                heappush(h,(j[1],j[0]))
        if h:
            cnt+=1
            cur=heappop(h)
            start=now
            now+=cur[0] #작업시간 만큼 추가
            wait+=(now-cur[1])
        else:
            now+=1
        if cnt==len(jobs):        
            break
        
    answer=wait//len(jobs)
    return answer