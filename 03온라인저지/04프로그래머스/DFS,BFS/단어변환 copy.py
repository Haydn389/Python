answer = 1e9

def check(a,b): #한 자리만 다른지 확인
    res=0
    for i in range(len(a)):
        if a[i]!=b[i]:
            res+=1
            if res>=2:
                return False
    if res==1:
        return True
    return False

def solution(begin, target, words):
    n=len(words)
    pos=[]
    visited=[False]*n
    def dfs(i,pre):
        global answer
        if pre==target: #target과 일치하는 경우에만 업데이트
            print(pos,len(pos))
            answer=min(answer,len(pos))
            return
    
        if i==n: #자리 모두 차면 반환
            return
        for j in range(n):
            if not visited[j] and check(pre,words[j]):
                pos.append(words[j])
                visited[j]=True
                dfs(i+1,words[j])
                pos.pop()
                visited[j]=False
    dfs(0,begin)
    if answer == 1e9:
        return 0
    return answer

begin="aab"
target="aba"
words= ["abb", "aba"] 
print(solution(begin, target, words))