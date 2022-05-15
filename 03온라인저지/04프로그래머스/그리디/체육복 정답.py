import sys

n=int(sys.stdin.readline().strip())

lost=list(map(int,sys.stdin.readline().split()))
reserve=list(map(int,sys.stdin.readline().split()))


def solution(n, lost, reserve):
    new_lost = set(lost) - set(reserve)
    # print("new_lost=",new_lost)
    new_reserve = set(reserve) - set(lost)
    # print("new_reserve=",new_reserve)

    for i in new_lost:
        if i + 1 in new_reserve:
            new_reserve.remove(i + 1)
            # print("new_reserve=",new_reserve)
        elif i - 1 in new_reserve:
            new_reserve.remove(i - 1)
            # print("new_reserve=",new_reserve)
        else:
            n-=1
    return n
print(solution(n, lost, reserve))