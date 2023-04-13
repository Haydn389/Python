from collections import deque
def check(x,y,rectangle):
    for x1,y1,x2,y2 in rectangle:
        if x1*2<x<x2*2 and y1*2<y<y2*2:
            return False
    return True
def solution(rectangle, characterX, characterY, itemX, itemY):
    n=m=0
    for x1,y1,x2,y2 in rectangle:
        n=max(n,y2)
        m=max(m,x2)
    map=[[0]*((m+1)*2) for _ in range((n+1)*2)]
    for x1,y1,x2,y2 in rectangle:
        for i in range((x2-x1)*2+1):
            map[2*y1][2*x1+i]=map[2*y2][2*x1+i]=1
        for j in range((y2-y1)*2+1):
            map[2*y1+j][2*x1]=map[2*y1+j][2*x2]=1
    answer = 0
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    def bfs(x0,y0,rectangle):
        q=deque([(x0,y0)])
        map[y0][x0]=1
        while q:
            x,y=q.popleft()  
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if ((nx,ny)!=(x0,y0)) and 0<=nx<=2*m and 0<=ny<=2*n and map[ny][nx]==1 and check(nx,ny,rectangle):
                    q.append((nx,ny))
                    map[ny][nx]=map[y][x]+1
    bfs(characterX*2,characterY*2,rectangle)
    answer=(map[2*itemY][2*itemX]-1)//2
    return answer