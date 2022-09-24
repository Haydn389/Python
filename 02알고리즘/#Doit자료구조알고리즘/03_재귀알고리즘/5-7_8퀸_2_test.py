#행과 열에 퀸을 1개 배치하는 조합
# print("test")
pos = [0]*3
flag=[0]*3
print(flag)
print("-------")
def put():
    for i in range(3):
        print(f"{pos[i]:2}", end="")
    print()


def set(i):  # i열에 퀸 배치
    for j in range(3):
        if flag[j] ==0: #j행에 퀸 배치안했으면
            pos[i] = j  # j행에 퀸 배치
            if i == 2:
                put()
            else:
                flag[j]=1 # 플래그 채우기
                print("True 넣기\t",flag)
                set(i+1)  # 다음열에 퀸 배치
                flag[j]=0
                print("False 넣기\t",flag)
set(0)
