def bin_search(a, target, pl, pr):
    if pl > pr:
        return None
    pc = (pl+pr)//2
    if a[pc] == target:
        return pc
    elif a[pc] > target:
        return bin_search(a, target, pl, pc-1)
    else:
        return bin_search(a, target, pc+1, pr)


n, target = list(map(int, input().split()))

a = list(map(int, input().split()))

result = bin_search(a, target, 0, n-1)

if result == None:
    print("없음")
else:
    print(result+1)
