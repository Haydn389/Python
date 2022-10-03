import sys
n = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# n=8
# a=[[1, 1, 0, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0],
#     [1, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1]]
# a=[[1, 1, 0, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1]]

# print(a[:len(a)//2])
# ha=[x[:len(a)//2] for x in a[:len(a)//2]]
# print(ha)
# tot=0
# for i in a:
#     tot+=sum(i)
# t=[sum(i) for i in a]
# print(sum([sum(i) for i in a]))

sum_0=0
sum_1=0

def div(a,n):
    global sum_0,sum_1
    if sum([sum(i) for i in a]) == 0:
        sum_0+=1
        return
    elif sum([sum(i) for i in a]) ==n**2:
        sum_1+=1
        return
    half=n//2
    div([x[:half] for x in a[:half]],half)
    div([x[half:] for x in a[:half]],half)
    div([x[:half] for x in a[half:]],half)
    div([x[half:] for x in a[half:]],half)
    
div(a,n)
print(sum_0)
print(sum_1)
