#파이썬에서는 heapq 기능을 위해 heapq라이브러리를 제공,
#heapq은 다익스트라 최단경로 알고리즘을 포함해 다양한 알고리즘에서 우선순위 큐 기능을 구현할때 사용
#heqpq외에도 PriorityQueue 라이브러리를 사용할 수 있지만, 코테환경에서는 heapq 사용권장
#파이썬의 힙은 최소힙으로 구성되어있어, 단순히 원소를 힙에 전부 넣었다 빼는 것만으로도 시간복잡도 O(NlogN)에 오름차순 정렬이 완료
# 보통 최소힙 자료구조의 최상단원소는 항상 가장작은 원소이기 때문

import heapq

def heapsort(arr):
    h=[]
    res=[]

    for v in arr:
        heapq.heappush(h,v)
    
    for i in range(len(h)):
        res.append(heapq.heappop(h))
    return res

print(heapsort([1,3,5,7,9,2,4,6,8,0]))