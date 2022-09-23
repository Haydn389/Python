T = int(input())  # Test case
for _ in range(T):
    data = list(map(int, input().split()))
    count = 0
    for i in data[1:]:
        if i > sum(data[1:])/data[0]:
            count += 1
    print("{:.3f}%".format(count/data[0]*100,3))

    # num = data[0]
    # val = data[1:]
    # total = sum(val)
    # avg = total/num
    # count = 0
    # for i in val:
    #     if i > avg:
    #         count += 1

    # print("{:.3f}%".format(count/num*100,3))

