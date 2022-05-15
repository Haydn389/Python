import sys

s=sys.stdin.readline().strip()
if sum(list(map(int,s[:len(s)//2])))==sum(list(map(int,s[len(s)//2:]))):print('LUCKY')
else: print('READY')