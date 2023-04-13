from collections import deque
answer = []
def solution(tickets):
    q=deque(tickets)
    while(q[0][0]!="ICN"):
        q.rotate(1)
    tickets=list(q)
    n=len(tickets)
    pos=[]
    def dfs(i):
        global answer
        if i==n:
            if len(answer)==0:
                answer=pos[:]
            else:
                if answer > pos:
                    answer=pos[:]
    
            return
        for j in range(n):
            if (not visited[j] and len(pos)==0) or (not visited[j] and pos[-1]==tickets[j][0]):
                if len(pos)==0:
                    pos.append(tickets[j][0])
                    pos.append(tickets[j][1])
                else:
                    pos.append(tickets[j][1])
                visited[j]=True
                dfs(i+1)
                visited[j]=False
                pos.pop()

    visited=[False]*n
    dfs(0)
    
    return answer