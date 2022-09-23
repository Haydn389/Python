T = int(input()) #Test case
for _ in range(T):
    sum=0
    data=list(input().split("X"))
    for i in data:
        if "O" in i:
            n=len(i)
            sum+=n*(n+1)/2
    print(int(sum))