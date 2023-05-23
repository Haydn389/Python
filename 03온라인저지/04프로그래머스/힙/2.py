from heapq import heappush,heappop

def solution(jobs):
    n=len(jobs)
    heap=[]
    answer=now=i=0
    start=-1
    
    while True:
        for j in jobs:
            if start<j[0]<=now:
                heappush(heap,((j[1],j[0])))#소요시간, 요청시간
        if heap:
            cur=heappop(heap)
            start=now#현재 작업의 시작시간 저장
            now+=cur[0]#현재시간을 소요시간 만큼 업데이트
            answer+=(now-cur[1])
            i+=1
            if i>=n:
                break
        else:
            now+=1
                
    answer = answer//n
    return answer