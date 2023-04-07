def rotate(a):
    n=len(a)
    res=[[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            res[c][n-1-r]=a[r][c]
    return res

def check(m,n,add,lock):
    for i in range(n):
        for j in range(n):
            if add[m-1+i][m-1+j]+lock[i][j]!=1:
                return False
    return True

def solution(key, lock):
    m=len(key)
    n=len(lock)
    a=[[0]*(m+n+1) for _ in range(m+n+1)]

    for _ in range(4):  
        #key 슬라이딩
        for x in range(m+n-1):
            for y in range(m+n-1):
                #대입
                for i in range(m):
                    for j in range(m):
                        if m-1<=x+i<=m+n-2 and m-1<=y+j<=m+n-2:
                            a[x+i][y+j]=key[i][j]
                # for f in a:
                #     print(f)
                # print("----")
                answer=check(m,n,a,lock)
                # print(answer)
                if answer:
                    return answer
                a=[[0]*(m+n+1) for _ in range(m+n+1)]
        key=rotate(key)

        answer = False 
    return answer