ct=list(map(int,input().split()))


def solution(ct):
    ct.sort()
    # 0 1 3 5 6
    max=0
    front=[]
    end=[]    
    for i in range(len(ct)):
        front=ct[0:i]
        end=ct[i:len(ct)]
        print("front=",front,"end=",end)
        print("ct[",i,"]=",ct[i])
        if (ct[i]<=len(end)) and (ct[i]>=max):
            max=ct[i]
            print("max=",max)

    return max          
        # for j in range(i,len(ct)):

            
            
print(solution(ct))
    # answer = 0
    # return answer

