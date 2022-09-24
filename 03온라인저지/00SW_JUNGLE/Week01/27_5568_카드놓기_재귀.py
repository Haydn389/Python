import string


n=int(input())
k=int(input())

card=[]
dp=[0]*n

result=0

for _ in range(n):
    card.append(int(input()))

string=""
result=set()

def select(cnt):
    global string

    if cnt==k:
        