import sys
answer = 100
def solution(begin, target, words):
    n=len(words)
    m=len(begin)
    pos=['']*(n)
    visited=[False]*n
    def check(pos): # hit : "hot" -> "dot" -> "dog" -> "cog"
        global answer            # hit : 'hot', 'dot', 'dog', 'lot', 'log', 'cog'
        cur=begin
        i=1
        for next in pos:
            if i >= answer:
                return
            cnt=0 # 문자 차이 갯수 세기
            for j in range(m):
                if cur[j]!=next[j]:
                    cnt+=1
            if cnt==1: #차이나는 문자 수개 1개라면 
                if next==target:
                    # print(pos)
                    answer =min(i,answer)
                    return
                else: 
                    cur=next
            else: #차이나는 문자갯수가 1개가 아니라면
                return
            i+=1
    
    def back(i):
        if i==n:
            # print(pos)
            check(pos)
            return
        for j in range(n):
            if not visited[j]:
                pos[i]=words[j]
                visited[j]=True
                back(i+1)
                visited[j]=False
    back(0)
    if answer == 100:
        return 0
    else: 
        return answer