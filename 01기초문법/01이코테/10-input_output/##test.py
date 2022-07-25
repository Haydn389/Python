# #리스트 컴프리헨션
# n=4
# m=3
# array1=[[0]*m for _ in range(n)]
# array2=[[0]*m]*n
# array1[1][1]=5
# array2[1][1]=5
# print(array1,array2)


# # 키, 값 추출
# a=dict()
# a["사과"]="apple"
# a["바나나"]="Banana"
# print(a)
# print(list(a.keys()))
# print(list(a.values()))

# # 집합자료형 : 어떤 정수가 나왔는지 안나왔는지 체크
# a={1,2,3}
# print(1 in a) # 결과 값 boolen #사전이나 집합 자료형의 경우 시간복잡도 O(1)\
# b=[1,2,3,4,5,6]
# print(3 in a) #시간복잡도 O(n) # 튜플역시 O(n)

#===============입출력================#

#입력:1 2 3 4 5 했을때
# input().split() --> ['1','2','3','4','5'] #split : 공백기준으로 문자를 나눠주는 함수
#a,b,c,d,e=map(int, input().split()) #map함수는 리스트 각각의 원소를 각각 어떤 함수에 적용시킬 때 사용
#data=list(map(int, input().split())) #이를 다시 리스트화 시킴

# data=list(map(int, input().split()))
# print(data)

# #예시 1 : n,m,k를 공백 기준으로 구분하여 입력
# n,m,k=map(int,input().split())
# print(n,m,k)

# # 예시 2 : 데이터 개수 입력, 각 데이터를 공백기준으로 구분하여 입력
# n=int(input())
# data=list(map(int,input().split())) 
# print(n)
# print(data)

# # 예시 3 : 2차원 데이터 입력
# '''
# 3
# 4
# 0000
# 0000
# 0000
# '''
# n=int(input())
# m=int(input())

# array=[]
# for i in range(n):
#     array.append(list(map(int,input().split())))

# print(array)

# # 입력팁 : readline() , 보통 많이는 사용 안하고 그래프나 정렬쪽에서 많은수가 들어올 때 사용
# import sys
# data= sys.stdin.readline().rstrip()
# print(data)


