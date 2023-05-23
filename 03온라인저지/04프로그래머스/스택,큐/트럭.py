from collections import deque
def solution(bridge_length, weight, truck_weights):
    wait=deque(truck_weights)
    bridge=deque([ 0 for _ in range(bridge_length)])
    answer = 0
    tot=0
    while bridge:
        answer+=1
        out=bridge.popleft()
        tot-=out
        if wait:
            if tot+wait[0]<=weight:
                cur=wait.popleft()
                bridge.append(cur)
                tot+=cur
            else:
                bridge.append(0)

    return answer