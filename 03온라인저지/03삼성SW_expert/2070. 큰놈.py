n=int(input())

for i in range(n):
    a,b=map(int, input().split())
    if a>b:
        c=">"
    elif a<b:
        c="<"
    else:
        c="="
    print(f"#{i+1} {c}")
