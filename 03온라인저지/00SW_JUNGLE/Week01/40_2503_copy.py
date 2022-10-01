from itertools import permutations
import sys

n = int(sys.stdin.readline())
m = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

per = list(permutations(range(1, 10), 3))
cnt = 0
for p in per:
    temp = 0
    for i in m:
        check = False    
        flag = 0
        strike=set()
        for k in range(3):
            if str(p[k])==str(i[0])[k]:
                flag += 1
                strike|=set(str(p[k]))
        if flag != i[1]:
            break
        elif len((set(str(i[0])) & set(map(str,p)))-strike) != i[2]:
            break
        else:
            check = True  
    if check:
        cnt += 1
print(cnt)
