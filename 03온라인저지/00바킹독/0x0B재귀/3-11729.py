import sys
input=sys.stdin.readline

n=int(input())

#n개의 판을 a에서b로 옮기는법
def func(a,b,n):
    if n==1:
        print(a,b)
        return
    func(a,6-a-b,n-1)
    func(a,b,1)
    func(6-a-b,b,n-1)

print((1<<n)-1)
func(1,3,n)