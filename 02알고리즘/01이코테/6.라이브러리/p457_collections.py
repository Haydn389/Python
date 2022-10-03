#deque 라이브러리를 활용한 큐 자료구조 구현
#일반적인 리스트에서 가장 앞쪽에 원소를 추가하거나 제거할때의 시간복잡도는 O(N)
#deque에서는 위 경우에도 O(1)
#deque은 스택이나 큐의 기능을 모두 포함하기 때문에 스택 혹은 큐 대용으로 사용될 수 있음
#사용법
#1) 첫번째 원소 제거하기 : popleft()
#2) 마지막 원소 제거하기 : pop()
#3) 첫번째 인덱스에 원소x 삽입하기 : appendleft(x)
#4) 첫번째 인덱스에 원소x 삽입하기 : append(x)

#5)따라서 deque을 이용한 큐 구현시 사용되는 함수는 딱 2가지
#  - firstin : append(), first out : popleft()

from collections import deque
a=deque([2,3,4])
a.append(1)
a.popleft()

print(type(a))