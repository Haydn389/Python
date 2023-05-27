from collections import deque

def solution(operations):    
    answer = deque()
    for i in operations:
        oper,num=i.split()
        num=int(num)
        # print(oper,num)
            
        if oper=="I":
            answer.append(num)
            answer=list(answer)
            answer.sort()
            answer=deque(answer)
        elif answer:
            if num==1:
                answer.pop()
            else :#num==-1
                answer.popleft()
        # print(answer)
    if answer:
        return [answer[-1],answer[0]]
    else:
        return [0,0]