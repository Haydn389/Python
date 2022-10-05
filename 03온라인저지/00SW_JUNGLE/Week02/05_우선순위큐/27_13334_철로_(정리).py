import sys
input = sys.stdin.readline
import heapq 

n=int(input())
#입력값을 오름차순으로 정렬하여 받기
a=[sorted(list(map(int,input().split()))) for _ in range(n)]
#end point 기준으로 오름차순 정렬 
a.sort(key=lambda x:x[1])
d=int(input())
# res=-1*(sys.maxsize) 
#최소값으로 초기화
res=0
h=[]
for s,e in a:
    #정렬된 start,end point를 기준으로 하나씩 꺼내어 기준에 충족될 시 heap에 넣는다.
    #lim은 현재 step에서 start가 존재할 수 있는 한계. 즉, 최솟값을 의미
    lim=e-d
    #start 가 limit 이상일때에만 힙에 추가
    if lim<=s:
        heapq.heappush(h,s) # 이때 힙에 들어가는 정보는 start 포인트 이다.
    #그 이유는 다음 while문에서 heap의 root node를 하나씩 꺼내어 현재step에서 lim보다 작은 start를 모두 꺼내기 위함
    while h and h[0] < lim:
        heapq.heappop(h)
    #모든 검토를 마친 뒤 이전까지의 최댓값res와 현재 step의 힙의 길이를비교해 큰 값을 넣는다.
    res=max(res,len(h))
print(res)
