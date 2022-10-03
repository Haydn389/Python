import sys
n = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
white = blue = 0  # count하기 위한 변수 초기화

def div(a, n):
    global white, blue
    if sum([sum(i) for i in a]) == 0:  # 현재단계 블럭 내의 값을 모두 더한다.
        white += 1  # 만약 합이 0이라면 white +=1
        return
    elif sum([sum(i) for i in a]) == n**2:  # 현재단계 블럭 내의 값을 모두 더한다.
        blue += 1  # 만약 그 값이 면적과 같다면 blue+=1
        return
        # 둘 다 아닌경우는 종이의 한변의 길이를 절반으로 다시 나눈다.
    half = n//2
    div([x[:half] for x in a[:half]], half)  # 1) 1구역 나눈 후 함수호출
    div([x[half:] for x in a[:half]], half)  # 2) 2구역 나눈 후 함수호출
    div([x[:half] for x in a[half:]], half)  # 3) 3구역 나눈 후 함수호출
    div([x[half:] for x in a[half:]], half)  # 4) 4구역 나눈 후 함수호출

div(a, n)
print(white)
print(blue)
