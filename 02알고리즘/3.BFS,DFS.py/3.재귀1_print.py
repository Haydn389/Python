def recur(i):
    if i==3:
        return
    else:
        print(i,"번째 재귀 함수에서",i+1,"번째 재귀함수 호출")
        recur(i+1)
        print(i,"번째 재귀함수 종료" )
recur(1)