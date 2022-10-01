import sys
from itertools import permutations
min = 1e9
if __name__ =="__main__":
    N = int(sys.stdin.readline())
    # array2d = [[0 for i in range(N)] for j in range(N)]
    array2d = []
    for _ in range(N):
        array2d.append(list(map(int, sys.stdin.readline().split())))
    
    # city = [None] * N
    # for i in range(N):
    #     city[i] = i
    # route = []
    # print(city)
    # for i in permutations(range(4)):
    #     route.append(list(i))
    # print(route)
    # print(route[0][0])
    # print(route[0][1])
    # print(route[0][2])
    # print(route[0][3])
    # print(len(route))
    # 다시 출발지로 돌아온다.

    route=list(map(list,permutations(range(4))))

    # print (route)
    for i in range(len(route)):
        route[i].append(route[i][0])
    
    # print(route)
    min_cost = 1e9
    for i in range(len(route)):
        flag=True
        total_cost = 0
        for j in range(N):
            start = route[i][j]
            end = route[i][j+1]
            cost = array2d[start][end]
            if cost == 0:
                flag=False
                break
            total_cost += cost
        if flag and total_cost < min_cost:
            min_cost = total_cost
    print(min_cost)
