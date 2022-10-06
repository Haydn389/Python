import sys
input = sys.stdin.readline
x,y,z = map(int, input().split()) #3개들어올 경우
def multi(x,y,z):
    if y==1:
        return x%z
    temp=multi(x,y//2,z)
    if y%2==0:
        return (temp**2)%z
    else:
        return (temp**2*x)%z

print(multi(x,y,z))