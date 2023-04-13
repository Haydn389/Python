#시간초과
from itertools import permutations

def solution(begin, target, words):
    n=len(words)

    if target not in words:
        return 0

    answer=1e9

    for p in list(permutations(range(n))):#조합 생성
        # print(p)
        next=begin
        cnt=0
        for i in p: # case) hot dot dog lot log cog
            # print(words[i],end=" ")
            # print(len(set(words[i])-set(next)))
            if len(set(words[i])-set(next))==1:
                next=words[i]
                cnt+=1
                if next==target:
                    # print("======성공=====")
                    answer= min(cnt,answer)
                    break 
            else:
                break
                
    # if answer==1e9:
    #     answer=0

    return answer