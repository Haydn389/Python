cnt=0
def gcd(x,y):
    global cnt
    if y==0:
        # print("마지막")
        return x
    else:
        # cnt+=1
        # print(cnt)
        return gcd(y,x%y)

print(gcd(128,96))