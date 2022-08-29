n=int(input())
data=[]
for i in range(n):
    data=list(map(int, input().split()))
    print(f"#{i+1} {max(data)}")
