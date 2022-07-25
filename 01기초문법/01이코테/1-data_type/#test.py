# 리스트 컴프리헨션 초기화
# n=3
# m=4
# a=[[0]*m for _ in range(n)]
# a[1][1]=5
# print(a)

# b=[[0]*m]*n
# b[1][1]=5
# print(b)

# # 특정원소 제거
# a=[1,1,2,5,8,7,5,8,7,8]
# b=7,8
# result=[i for i in a if i not in b]
# print(result)


a=[2,1,8,7,1,2,3]
# a.append(123)
a.sort()
print(a)
