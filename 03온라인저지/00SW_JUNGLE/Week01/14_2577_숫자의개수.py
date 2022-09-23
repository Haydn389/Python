a=int(input())
b=int(input())
c=int(input())
n=str(a*b*c)
# print(str(n))
for i in range(10):
    print(n.count(str(i)))