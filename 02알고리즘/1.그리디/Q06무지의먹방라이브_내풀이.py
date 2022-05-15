import sys
from typing import AnyStr

food_times=list(map(int,input().split()))
k=int(sys.stdin.readline())

def solution(food_times,k):
    foods=[]
    for i in range(len(food_times)):
        foods.append((food_times[i],i+1))
    # print(foods)
    foods.sort()
    print(foods)
    pretime=0
    spend=0
    n=len(foods)
    
    # for i, f in enumerate(foods):
        # diff=f[0]-pretime
    for i in range(len(foods)):
        # print(foods[i][0])
        diff=foods[i][0]-pretime
        if diff!=0:
            spend=diff*n
            if spend<=k:
                k-=spend
                pretime=foods[i][0]
            else:
                k%=n
                new=sorted(foods[i:],key=lambda x:x[1]) 
                return new[k][1]
        n-=1

    answer=0
    return answer

print(solution(food_times,k))
