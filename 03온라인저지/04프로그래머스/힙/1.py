from heapq import heappop,heappush,heapify,nsmallest,nlargest


def solution(scoville, K):
    heapify(scoville)
    cnt=0
    # print(len(scoville))
    # print(scoville)
    # print("*"*30)
    while(scoville[0]<K):
        cnt+=1
        a=heappop(scoville)
        b=heappop(scoville)
        heappush(scoville,a+b*2)
        if len(scoville)==1 and scoville[0]<K:
            cnt=-1
            break
        # print(cnt,scoville)
    answer = cnt
    return answer