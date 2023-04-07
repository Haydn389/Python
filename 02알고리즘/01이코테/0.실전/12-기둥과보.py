def check_col(y,x,n):
    if y==0 or col[y-1][x]==1:
        return True
    if  beam[y][x]==1 or (x>0 and beam[y][x-1]):
        return True
    return False
def check_beam(y,x,n):
    if col[y-1][x]==1 or (x+1<=n and col[y-1][x+1])==1:
        return True
    elif 0<=x-1 and x+1<=n:
        if beam[y][x-1]==1 and beam[y][x+1]==1:
            return True
    return False

    
def can_delete(y,x,n):
    for i in range(x-1,x+2):
        for j in range(y,y+2):
            # print("i,j")
            if col[j][i] and check_col(j,i,n)==False:
                return False
            if beam[j][i] and check_beam(j,i,n)==False:
                return False
    return True
    
col=[[]]
beam=[[]]
def solution(n, build_frame):
    global col, beam
    col=[[0]*(n+1) for _ in range(n+1)]
    beam=[[0]*(n+1) for _ in range(n+1)]
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    for i in build_frame:
        x,y,a,b=map(int,i)
        if a==0:#기둥
            nx=x
            ny=y+1
            if b:#설치
                # print(f"{x},{y} 에 기둥설치!")
                if check_col(y,x,n):
                    # print(f"{x},{y} 설치성공!")
                    col[y][x]=1 #기둥 있음 표시

            else:#삭제
                col[y][x]=0
                if can_delete(y,x,n)==False:#삭제할 수 없으면
                    col[y][x]=1
        else: #보
            nx=x+1
            ny=y
            if b:#설치
                if check_beam(y,x,n):
                    beam[y][x]=1
            else: #삭제
                beam[y][x]=0
                if can_delete(y,x,n)==False:#삭제할 수 없으면
                    beam[y][x]=1
                    
        # for j in range(n-1,-1,-1):
        #     print(col[j])            
        # print("-"*30)
        # for j in range(n-1,-1,-1):
        #     print(beam[j])            
        # print("*"*30)
        
    answer = []
    for i in range(0,n+1):
        for j in range(0,n+1):
            if col[j][i]:
                answer.append([i,j,0])
            if beam[j][i]:
                answer.append([i,j,1])
    return answer