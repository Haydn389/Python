#N_Queen 정답
import sys
n = int(sys.stdin.readline())
pos = [0]*n
flag_a = [0]*n
flag_b = [0]*((n-1)*2+1)
flag_c = [0]*((n-1)*2+1)
cnt = 0


def put():
    for i in range(n):
        print(f"{pos[i]:2}", end="")
    print()

def set(i):  # i열에 퀸 배치
    global cnt
    for j in range(n):
        if (flag_a[j] == 0 and flag_b[i+j] == 0 and flag_c[i-j+(n-1)] == 0):  # j행에 퀸 배치안했으면
            pos[i] = j  # j행에 퀸 배치
            if i == n-1:
                # put()
                cnt += 1
            else:
                flag_a[j] = flag_b[i+j] = flag_c[i-j+(n-1)] = 1  # 플래그 채우기
                set(i+1)  # 다음열에 퀸 배치
                flag_a[j] = flag_b[i+j] = flag_c[i-j+(n-1)] = 0
set(0)
print(cnt)
