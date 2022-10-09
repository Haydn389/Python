#https://ku-hug.tistory.com/132#--%C-%A---%C-%A---%C-%A--%C-%A---%C-%A---%C-%A---%C-%A---%C-%A---
import sys
sys.setrecursionlimit(10**9)
nums = []
while True:                            
    try:
        nums.append(int(sys.stdin.readline()))
    except:
        break
        
def postorder(s, e):
    if s > e:
        return
    mid = e + 1  # 오른쪽 노드가 없을 경우를 고려
    #mid를 end + 1로 초기화하는 이유
    #만약 모든 원소가 루트 노드보다 작은 경우 for문 안의 if문 안으로 들어갈 수 없으며 mid는 그대로 end+1이되고
    # 1) post(start + 1, mid - 1) : start + 1, end 가 삽입, 즉 루트 노드를 제외한 트리 전체가 삽입된다
    # 2) post(mid, end) : end + 1, end 가 삽입되어 if start > end: return에 의해 바로 리턴됨 이는 오른쪽 노드가 없음을 의미
    for i in range(s+1, e+1):
        if nums[s] < nums[i]:
            mid = i
            break

    postorder(s+1, mid-1)               # 왼쪽 확인
    postorder(mid, e)                   # 오른쪽 확인
    print(nums[s])

postorder(0, len(nums)-1)