def solution(tickets):
    n=len(tickets)
    answer=[]
    def back(i):
        if i==1 and pos[0][0]!='ICN':
            return
        if i==n:
            temp=[pos[0][0],pos[0][1]]
            for i in range(1,n):
                temp.append(pos[i][1])
            answer.append(temp)
            # print(answer)
            
            return
        for j in range(n):
            if not visited[j] and ((len(pos)==0) or (pos[-1][1]==tickets[j][0])):
                visited[j]=True
                pos.append(tickets[j])
                back(i+1)
                visited[j]=False
                pos.pop()
    pos=[]
    visited=[False]*(n)
    back(0)
    answer.sort()
    return answer[0]