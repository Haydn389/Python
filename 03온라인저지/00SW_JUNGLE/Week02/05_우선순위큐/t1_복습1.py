import sys
import heapq
input = sys.stdin.readline

# k,n=map(int,input().split())
# a=list(map(int, input().split()))
k, n = 4, 19
a = [2, 3, 5, 7]
h = [*a]
heapq.heapify(h)
res=[]
for _ in range(n):
    print("현재힙:", h)
    num = heapq.heappop(h)
    print("num", num)
    for i in range(k):
        temp = num*a[i]
        print("**a[i]", a[i])
        print(">>temp : ", temp)
        heapq.heappush(h, temp)
        res.append(temp)
        # if num % a[i] == 0: #딱 나누어 떨어지는 곳 까지만 push, 가장 마지막에 곱해졌던 소수보다 작거나 같은 소수까지만 곱해주면 됩
        #     print("나누어떨어짐 num", num, "% a[i]", a[i])
        #     break
    
print(num)
print(list(set(sorted(a+res)))[18])

