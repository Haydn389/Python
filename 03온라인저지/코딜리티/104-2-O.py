import sys
input=sys.stdin.readline

def solution(S):
    last_seen = {}  # 문자열이 마지막으로 등장한 위치를 저장할 딕셔너리
    max_gap = -1  # 가장 큰 간격을 저장할 변수
    for i in range(len(S) - 1):
        current_gram = S[i:i+2]  # 현재 2-gram
        if current_gram in last_seen:  # 이미 등장한 2-gram인 경우
            gap = i - last_seen[current_gram]  # 간격 계산
            max_gap = max(max_gap, gap)  # 최댓값 업데이트
        else:
            last_seen[current_gram] = i  # 처음 등장한 2-gram인 경우, 위치 저장
    return max_gap



A=input().rstrip()
print(solution(A))