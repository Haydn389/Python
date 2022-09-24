n=int(input())

def solve(x):
    if x<100: return 1
    elif x<1000:
        x=str(x)
        if (int(x[0])-int(x[1])) == ((int(x[1])-int(x[2]))):
            return 1
        return 0
    else: 
        return 0

cnt=0
for i in range(1,n+1):
    cnt+=solve(i)

print(cnt)
