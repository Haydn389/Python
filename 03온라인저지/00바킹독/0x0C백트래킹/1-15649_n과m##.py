import sys
input=sys.stdin.readline

n,m=map(int,input().split())
pos=[0]*m # m은 자리수, 트리의 깊이와 관련
visited=[False]*n #특정 수 사용여부저장 
cnt=0
def func(i): # 현재 i개까지 수를 택한 상황에서 pos[i](다음자리 수)를 정하는 함수
    if i==m: # m개를 모두 택했으면 출력
        # print(pos)
        for i in range(m):
            print(pos[i]+1,end=" ")
        print()
        return
    for j in range(n):# 0~n까지 수에 대해
        if not visited[j]:  # 아직 사용하지 않았으면
            pos[i]=j    # i번째 수를 j로 정함
            visited[j]=True # i를 사용되었다고 표시 
            func(i+1)   # 다음 수를 정하러 한단계 더 들어감
            visited[j]=False    # i번째 수를 i로정한 모든 경우에 대해 확인했으니 다시 False로 전환

func(0)
print(cnt)