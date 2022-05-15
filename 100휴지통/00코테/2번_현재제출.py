def solution(N,K,T):
    data=[[0]*K for _ in range(N)]
    for i in range(len(T)):
        x,y=T[i][0],T[i][1]
        for j in range(x-1,y):
            data[i][j]=1
            
    cnt=0
    for i in range(K):
        for j in range(N):
            if data[j][i]!=0:
                cnt+=1
                break
    return cnt