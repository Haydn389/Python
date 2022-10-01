import sys
n=int(sys.stdin.readline())
w=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

visited=[]
ans = float('inf')
 
def bf(start,next, cost):
    global ans,visited
    if len(visited)==n:
        if w[next][start] !=0:
            ans = min(ans, cost+w[next][start])
        return
    
    for i in range(n):
        #경로가 존재하고, 방문한적 없고, 비용이 현재보다 작을때
        if w[next][i]!=0 and i not in visited and cost<ans:
            visited.append(i)
            bf(start, i, cost+w[next][i])
            visited.pop()
        
for i in range(n):
    visited.append(i)
    bf(i, i, 0)
    visited.pop()
    
print(ans)