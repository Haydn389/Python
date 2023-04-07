import sys
input = sys.stdin.readline

a=input().rstrip()

print(ord('A'))
print(ord('Z'))
left=[]
right=0
for i in a:
    if 65<= ord(i)<=90:
        left.append(i)
    else:
        right+=int(i)

print("".join(sorted(left))+str(right))