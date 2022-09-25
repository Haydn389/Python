n=int(input())
def h(n,a,b):#(원반개수,시작,목표)
    if n==1:
        print(a,"-->",b)
        return 
    else:
        h(n-1,a,6-a-b)
        print(a,"-->",b)
        h(n-1,6-a-b,b)
print(2**n-1)
if n<=20:h(n,1,3)