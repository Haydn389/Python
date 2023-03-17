import sys
input = sys.stdin.readline
n = m = int(input())
pos=[0]*m
visited_1=[False]*n
visited_2=[False]*(2*n-1)
visited_3=[False]*(2*n-1)
cnt=0
def solve(i):
    if i==m:
        global cnt
        cnt+=1
        return
    for j in range(n):
        if not visited_1[j] and not visited_2[i+j] and not visited_3[i-j+n-1]:
            pos[i]=j
            visited_1[j]=visited_2[i+j]=visited_3[i-j+n-1]=True
            solve(i+1)
            visited_1[j]=visited_2[i+j]=visited_3[i-j+n-1]=False
            
solve(0)
print(cnt)