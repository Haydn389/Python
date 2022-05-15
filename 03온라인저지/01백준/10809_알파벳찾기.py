import sys

s=sys.stdin.readline().strip()
for i in range(26):
    print(s.find(chr(i+97)),end=" ")
