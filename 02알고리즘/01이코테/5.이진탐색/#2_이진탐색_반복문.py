def bin_search(a,key,pl,pr):
    while pl<=pr:
        pc=(pl+pr)//2
        if a[pc]==key:
            return pc
        elif a[pc]<key:
            pl=pc+1
        else:
            pr=pc-1
    return None
        
n, key = list(map(int, input().split()))

a = list(map(int, input().split()))

result = bin_search(a, key, 0, n-1)

if result == None:
    print("없음")
else:
    print(result+1)
