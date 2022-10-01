import sys
n, m = map(int, sys.stdin.readline().split())
a = [1, 3, 5, 7, 8, 10, 12]  # a그룹 : 31일인 월
b = [4, 6, 9, 11]  # b그룹 : 30일인 월
x = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
tot = 0
for i in range(1, n):
    if i in a:      #a 그룹일 때
        tot += 31
    elif i in b:    #b 그룹일 때
        tot += 30
    else:           #둘 다 아닐때
        tot += 28
print(x[(tot+m) % 7])
