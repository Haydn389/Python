#조합(cut만 잘 넣어주면됨, visited 필요x)
import sys
input = sys.stdin.readline

n,m =map(int,input().split())

pos=[0]*m
# visited=[False]*(n+1)

def solve(i,cut):
    if i==m:
        print(*pos)
        return
    for j in range(cut+1,n+1):
        # if not visited[j]:
            pos[i]=j
            # visited[j]=True
            solve(i+1,j)#다음스텝에 가기전 현재상태를 저장하여 j 이상인 수에 대해서만 탐색
            # visited[j]=False
solve(0,0)