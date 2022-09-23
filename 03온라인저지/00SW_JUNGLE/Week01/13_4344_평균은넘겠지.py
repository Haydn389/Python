T = int(input())  # Test case
for _ in range(T):
    data = list(map(int, input().split()))

    num = data[0]
    val = data[1:]
    total = sum(val)
    avg = total/num
    count = 0
    for i in val:
        if i > avg:
            count += 1

    print(round(count/num*100,3))
