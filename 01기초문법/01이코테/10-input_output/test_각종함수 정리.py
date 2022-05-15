# a=[1,2,3,4,5]

# b=[i for i in range(20) if i %2==0]
# # print(b)
#여러가지 리스트 함수
# # a.reverse()
# # a.insert(2,10)
# # print(a)
# # a.remove(10)
# # print(a)

# remove={4,6}
# 리스트 컴프리헨션
# res=[i for i in b if i not in remove]
# print(res)
# res.reverse()
# print(res)
# print(a[1:4])

# a=[1,2,3,4,5]
# remove={3,5}
# b=[i for i in a if i not in remove]

# print(b)

###튜플데이터 원하는 대로 정렬하기
# student_tuples = [
#     ('john', '10', 15),
#     ('jane', '10', 12),
#     ('dave', '10', 10),
# ]
# sorted(student_tuples, key=lambda student: student[2])
# for c in student_tuples:
#         i,j,k=c
#         j=int(j)
#         print(i,j+k)

#map 함수
a=[str(i) for i in range(1,11)]
print(a)

a=list(map(int,a))
print(a)