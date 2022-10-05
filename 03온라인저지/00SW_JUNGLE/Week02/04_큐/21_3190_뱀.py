from collections import deque


def direction_change(d, c):
    if c == "L":
        d = (d-1) % 4
    else:
        d = (d+1) % 4
    return d


n = int(input())  # n = board 크기
k = int(input())  # k = 사과의 수

board = [[0]*n for _ in range(n)]  # 보드 초기화

for _ in range(k):  # 사과 그리기
    a, b = map(int, input().split())
    board[a-1][b-1] = 1

L = int(input())  # L= 방향전환 횟수
times = {}  # 시간에 다른 방향전환 정보 저장 dictionary

for _ in range(L):  # 방향전환 정보를 dictionary에 저장
    X, C = input().split()
    times[int(X)] = C
#===========입력===========#
# print(n,k)
# for i in board:
#     print(i)
# print(times)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

direction = 1  # 뱀의 현재 이동방향
time = 1  # 게임진행시간 저장하기 위한 변수
y, x = 0, 0  # 뱀위 현재 머리위치
# 뱀의 꼬리위치를 큐로 저장,
# 이동한 칸에 사과가 없다면 뱀의 마지막 부분인 꼬리를 제거
# 큐를 이용하면 가장 먼저 삽입된 끝부분을 지우기 쉬움
snake = deque([[y, x]])  # 현재 뱀의 머리위치를 큐에 넣는다.
board[y][x] = 2  # 뱀이 존재하는 곳은 보드에 2로 표시

while True:
    y, x = y+dy[direction], x+dx[direction]  # 몸길이를 늘려 머리를 다음칸에 위치시킴
    if 0 <= y < n and 0 <= x < n and board[y][x] != 2:  # 벽에 닿는지 혹은 자기몸에 닿는지 검사
        if not board[y][x] == 1:  # 사과가 없으면
            del_y, del_x = snake.popleft()  # 원래있던 좌표를 담아서
            board[del_y][del_x] = 0  # 지워준다
        board[y][x] = 2  # 새롭게 이동한 곳에 2로 표시
        snake.append([y, x])  # 머리 위치를 큐에 넣는다.
        if time in times.keys():
            direction = direction_change(direction, times[time])  # 특정시간에 해당하는 방향 전달
        time += 1
    else:
        break
print(time)
