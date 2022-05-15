import sys

# k=sys.stdin.readline().strip()
# n,m=map(int,sys.stdin.readline().split())

# array=list(map(int,sys.stdin.readline().split()))

# k=k.strip('"')
# print(k)

# new=[int(n) for n in k]
# INF=1e9
# print(new)
# print(sum(new))
# print(INF)

# n=10
a=[]
b=[]

for i in range(10):
    a.append(i)
    b.append(i)
    
# print(a.sort(reverse))
print(a[::-1])
b.sort(reverse=True)
print(b)

# array=[[0]*m for _ in range(n)]
# print(array)