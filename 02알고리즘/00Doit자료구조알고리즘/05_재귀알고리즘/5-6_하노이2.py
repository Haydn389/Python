n=int(input())
# h(갯수, 시작(1), 목표(3), 보조(2))
# print(n,start,target,assist)
# cnt=0
def h(n,a,b):
    # global cnt
    if n==1:
        print(a,b)
        # cnt+=1
        return 
    else:
        h(n-1,a,6-a-b) #n-1개를 보조기둥(a도 b도아닌 기둥 즉 6-a-b)에 이동
        print(a,b) #가장 큰 원판 1개를 시작기둥(a)에서 목표기둥(b)로 이동
        # cnt+=1
        h(n-1,6-a-b,b) #n-1개를 다시 보조기둥에서 목표기둥(b)로 이동

print(2**n-1)
if n<=20:h(n,1,3)