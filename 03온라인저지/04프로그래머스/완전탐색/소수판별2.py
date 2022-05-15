#https://dev-note-97.tistory.com/99

from itertools import permutations
import sys
numbers = sys.stdin.readline().strip()
# numbers = input()

def solution(numbers):
    numbers=numbers.strip('"') #양쪽 따옴표 제거
    answer = []

    nums=[n for n in numbers] #number를 하나 씩 자르기
    print(nums)
    per=[]

    for i in range(1,len(numbers)+1):  #예) 325라고하면 i를 1~3까지 변화시키며 각각 1개, 2개, 3개 일때의 순열을 모두 출력
        per+=list(permutations(nums,i))
    print(per)
    # new_nums=list(map(int,per))
    new_nums=[int("".join(p)) for p in per] #각각의 순열을 int형으로 변환
    print(new_nums)

    res=0
    for n in new_nums:
        if n<2: continue
        res=True
        for i in range(2,n):
            if n%i==0:
                res=False
                break
        if res==True:
            answer.append(n)
    # print(answer)
    return len(set(answer))

print(solution(numbers))
