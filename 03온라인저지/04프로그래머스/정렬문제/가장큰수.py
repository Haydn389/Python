import sys
num=list(map(int,sys.stdin.readline().split()))

def solution(num): 
    num = list(map(str, num)) 
    print(num)
    num.sort(key = lambda x : x*3, reverse = True)
    print(num)
    print("조인함수",''.join(num))
    return str(int(''.join(num)))



print(solution(num))