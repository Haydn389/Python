#각 열에 퀸을 1개 배치하는 조합
pos = [0]*4


def put():
    for i in range(4):
        print(f"{pos[i]:2}", end="")
    print()


def set(i):  # i열에 퀸 배치
    for j in range(3):
        pos[i] = j  # j행에 퀸 배치
        if i == 3:
            put()
        else:
            set(i+1)  # 다음열에 퀸 배치


set(0)
