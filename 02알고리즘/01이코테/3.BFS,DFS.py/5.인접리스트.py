#인접 행렬 방식
INF = 999999999

graph=[
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
    ]

print(graph)

#행이 세 개인 2차원 리스트로 인접 리스트 표현
graph2=[[] for _ in range(3)]

graph2[0].append((1,7))
graph2[0].append((2,7))

graph2[1].append((0,7))

graph2[2].append((0,5))

print(graph2)