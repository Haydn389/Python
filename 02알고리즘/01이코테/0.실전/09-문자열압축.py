import sys
input = sys.stdin.readline

s=input().rstrip()
def solution(s):
    answer=n=len(s)
    for num in range(1,n//2+1):#절반 길이까지 반복
        old=s[:num]
        compressed=""
        cnt=1
        for i in range(num,n,num):
            new = s[i:i+num]
            if old == new:
                cnt+=1
            else:
                compressed+=str(cnt)+old if cnt>1 else old
                cnt=1
                old=new

            # print(s[i:i+num])
        compressed+=str(cnt)+old if cnt>1 else old
        # print(">>>",compressed)
        answer =min(answer,len(compressed))
    return answer
print(solution(s))
