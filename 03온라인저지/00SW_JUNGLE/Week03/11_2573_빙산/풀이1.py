# https://lazypazy.tistory.com/101
import sys 
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

# 상하좌우로 얼음 살필 좌표
dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m = map(int,input().rstrip().split())
# 얼음과 물의 정보를 입력받는다.
ice = [list(map(int, input().rstrip().split())) for i in range(n)]
# 한번 녹은 빙산을 잠시 저장해줄 리스트
new = [[0 for i in range(m)] for i in range(n)]


# 빙산이 둘 이상으로 나누어졌는지 탐색하는 함수
def dfs(x,y):
    if x <= -1 or y <= -1 or x >= n or y >= m: 
        return False
    if ice[x][y] >0: # 바닷물이 아닌 빙산이라면
        ice[x][y] = 0 # 방문 처리
        # 상하좌우로 DFS 돌린다.
        dfs(x,y-1) 
        dfs(x,y+1)
        dfs(x+1,y)
        dfs(x-1,y)
        return True
    return False
    
year = 0 # 연도 카운트

while True:
    no = 0 # 둘 이상으로 쪼개지지 않고 전부 녹는 경우를 체크하기 위한 변수
    for i in range(n): 
        for j in range(m):
            if ice[i][j] > 0: # 얼음이라면
                cnt = 0
                for k in range(4):
                	# 상하좌우 네군데가 얼음인지 바닷물인지 체크
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if nx <= -1 or ny <= -1 or nx >= n or ny >= m: # 벗어나는 경우 컨티뉴
                        continue

                    if ice[nx][ny] == 0: # 바닷물이라면 카운트 올려줌
                        cnt += 1
                # 이제 현재 빙산을 녹여준다.
                # if 문 사용한 이유는 음수가 되지 않게 하기 위해서
                if ice[i][j] - cnt >= 0:
                    new[i][j] = ice[i][j] - cnt
                else:
                    new[i][j] = 0
            else: # 바닷물이라면
                no += 1 # no 카운트를 올려주고
    # 전부 바닷물이라면 0 출력 후 종료
    if no == n*m: 
        print(0)
        break
	# 둘로 쪼개졌는지 체크하기 위해 DFS 함수를 호출한다.
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                result += 1
    if result >= 2: # 둘 이상 쪼개졌다면 year 출력하고 종료
        print(year)
        break
    year += 1

	# 빙산 정보 업데이트
    ice = new
    new = [[0 for i in range(m)] for i in range(n)]