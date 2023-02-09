import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a=list(map(int,input().split()))
    num=a[0]
    score_list=a[1:]
    avg=sum(score_list)/num
    # print(avg)
    cnt=0
    for i in score_list:
        if i > avg: cnt+=1
    print("{:.3f}%".format(cnt/num*100))