import sys
answer=[]
answers=list(map(int,sys.stdin.readline().split()))
a1=[1, 2, 3, 4, 5]
a2=[2, 1, 2, 3, 2, 4, 2, 5]
a3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

def solution(answers):
    cnt1=cnt2=cnt3=0
    res = answers
    for i in range(len(answers)):
        if a1[i%5]==answers[i]:
            cnt1+=1
        if a2[i%8]==answers[i]:
            cnt2+=1
        if a3[i%10]==answers[i]:
            cnt3+=1
    res=[cnt1,cnt2,cnt3]

    for person, score in enumerate(res):
        if score==max(res):
            answer.append(person+1)

    return answer

print(solution(answers)) 
