cnt=0    
def solution(numbers, target):
    n=len(numbers)
    def dfs(i,tot,add,sub):
        global cnt
        if i==n:
            if tot==target:
                cnt+=1
            return
        if add!=0:
            dfs(i+1,tot+numbers[i],add-1,sub)
        if sub!=0:
            dfs(i+1,tot-numbers[i],add,sub-1)

            
    dfs(0,0,n,n)
    answer = cnt
    return answer