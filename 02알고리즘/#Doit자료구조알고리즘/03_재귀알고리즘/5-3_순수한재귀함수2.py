# def recur(n):
#     if n>0:
#         recur(n-2)
#         print(n)
#         recur(n-1)
# x=int(input())

def recur(n):
    while n>0:
        recur(n-2)
        print(n)
        n=n-1
x=int(input())
recur(x)