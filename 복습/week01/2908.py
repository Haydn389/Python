import sys
input = sys.stdin.readline

a,b=input().split()
print(max(int(a.sort(key=reverse)),int(b[::-1])))