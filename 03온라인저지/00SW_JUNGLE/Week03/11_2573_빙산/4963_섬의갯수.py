import sys,copy
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

while True:                            
    m,n=map(int,input().split())
    if n==0 and m==0:
        break
    #그래프 데이터가 붙어있을 때
    # graph=[list(map(int,list(input().rstrip()))) for _ in range(n)]
    graph=[list(map(int,input().split())) for _ in range(n)]
    # print(graph)
    def dfs(x,y):
        if x<=-1 or x>=n or y<=-1 or y>=m or graph[x][y]!=1: #육지가 아니면 종료
            return
        graph[x][y]=0 #육지1을 다른 문자로 채우자! 꼭 0이 아니라 #,2,* 등도 가능
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        #대각선
        dfs(x+1,y+1)
        dfs(x+1,y-1)
        dfs(x-1,y+1)
        dfs(x-1,y-1)



    cnt=0
    for i in range(n):
        for j in range(m):
            #육지(1) 바다(0)
            if graph[i][j]==1: #육지의 수를 구하는것이기때문에 육지일때만 dfs수행
                cnt+=1 #count +=1
                dfs(i,j)    #dfs를 하는 목적은 한번 탐색할때 시작 노드를 기준으로 연결된 모든 노드를 1이아닌 값으로 수정 하기위함 ex)0같은 수로
                            #1이 아닌 다른 값을 갖는 노든는 다시 방문하지 않음
                            #쉽게 색칠한다고 생각하자
    print(cnt) 