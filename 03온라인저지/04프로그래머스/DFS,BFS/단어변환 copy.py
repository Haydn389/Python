def check(a,b):
    res=0
    for i in range(len(a)):
        if a[i]!=b[i]:
            res+=1
    if res==1:
        return True
    return False

answer= 1e9
def solution(begin, target, words):
    n=len(words)
    pos=[]
    visited=[False]*n
    def dfs(i,pre):
        global answer
        if pre==target:
            # print(pos)
            answer=min(answer,len(pos))
            return
        if i==n:
            return
        for j in range(n):
            if not visited[j] and check(pre,words[j]):
                pos.append(words[j])
                visited[j]=True
                dfs(i+1,words[j])
                visited[j]=False
                pos.pop()
    dfs(0,begin)
    if answer==1e9:
        return 0
    return answer