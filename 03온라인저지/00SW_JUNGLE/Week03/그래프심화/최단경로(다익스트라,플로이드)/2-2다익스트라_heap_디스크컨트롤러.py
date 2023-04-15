import heapq
def solution(jobs):
    answer,now,i=0,0,0
    start=-1
    heap=[]

    while i<len(jobs):
        for j in jobs:
            #현재시점 now에서 작업할 수 있는 작업의 조건은 이전 작업의 시작시간 < X<=현재시간
            if start < j[0] <=now:
                heapq.heappush(heap,(j[1],j[0]))
        if heap:
            cur = heapq.heappop(heap)
            start =now
            now+=cur[0]
            answer+=(now-cur[1])
            i+=1
        else:
            now +=1
    return int(answer/len(jobs))


print(solution([[0, 3], [1, 9], [2, 6]]))