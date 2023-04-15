import sys
input=sys.stdin.readline

def solution(A):
    # Counter 클래스 -> 어떤 데이터가 몇번 등장했는지 쉽게 계수
    # 문자열, 딕셔너리, 배열 등 가능 
    import collections # collections 모듈의 Counter 클래스
    # Counter()는 생성자 함수로 dict를 반환
    ans=collections.Counter(A).most_common()
    # most_common()함수는 빈도수가 높은 원소부터 내림차순 정렬된 리스트 반환, 
    # 원소는 값과 빈도수로 이루어진 튜플, 정렬이 필요하기 때문에 nlogn 시간복잡도
    # most_common()함수는 인자로 정수(출력할 원소 수)를 받을 수 있으며 인자가 없을때는 정렬, 인자가 있으면 heap 자료구조 사용
    ans=collections.Counter(A)
    print(ans)
    for i in ans:
        if i[0]==i[1]:
            return i[0]
    return 0

A=list(map(int,input().split()))
print(solution(A))