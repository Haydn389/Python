import sys

def med3(a,b,c):
    # return a
    if a>=b:
        if b>=c: return b
        elif a>=c:return c
        else: return a
    elif a>=c:
        return a
    elif b>=c:
        return c
    else: return b


print("세 정수의 중앙값을 구합니다.",end=" ")
a,b,c=map(int,sys.stdin.readline().split())
# print(a)
print("중앙값은 : {}".format(med3(a,b,c)))