t=int(input())
def solve(n):
    if n == 1:
        return False
    if n == 2 or n==3: return True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
    
for _ in range(t):
    num = int(input())
    a = b = num//2
    while a > 0:
        if solve(a) and solve(b):
            print(a, b)
            break
        a -= 1
        b += 1
        # print("현재 a,b",a,b)

# print(solve(9))

