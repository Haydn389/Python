n=int(input())
c1,c2,c3=1,2,3
# h(갯수, 시작(1), 목표(3), 보조(2))
# print(n,start,target,assist)
cnt=0
def h(n,c1,c3,c2):
    global cnt
    if n==1:
        print(c1,c3)
        cnt+=1
        return 
    else:
        h(n-1,c1,c2,c3)
        print(c1,c3)
        cnt+=1
        h(n-1,c2,c3,c1)


h(n,c1,c3,c2)
print(cnt)