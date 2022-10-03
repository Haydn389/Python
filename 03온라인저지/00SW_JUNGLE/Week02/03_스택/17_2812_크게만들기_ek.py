# 차이0) stack[:n-k]를 꼭 해야하는 이유?
         # --> pop을 꼭 k번 하리라는 법은없음
         # ex) 9 3 987654321 의 경우 pop을 한번도 안함 --> 마지막에 [:n-k] 필수
# 차이1) cnt 대신 cnt 삭제 후 k --> 마지막에 k 활용하기 위함
# 차이2) del stack[-1] 대신 stack.pop() --> (ok)

import sys
input=sys.stdin.readline
# n,k=map(int,input().split())
# a=list(input().rstrip())
n,k=10,4
a='8177252841'

stack=[]
cnt=k
for num in a:
    print("(전)",stack)
    while stack and cnt>0 and stack[-1] < num:
        #왜 if가 아니라 while일까 : 현재 num 보다 top값이 작은동안 계속해서 pop해주기위해서
        print(f">>>비교 stack[-1]={stack[-1]}, num={num}")
        test=stack.pop()
        cnt-=1
        print(f">>>{test}제거됨")
        print(f">>>{stack}")
        print(f">>>현재 cnt={cnt}")    
    stack.append(num)
    print("(후)",stack)

print("".join(stack))