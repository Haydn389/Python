a=[1.3,3.2,2.1,2.1,2.1]
print("기본 리스트:",a)

for i in range(5):
    a.append(2)
print("삽입:",a)

a.sort()
print("오름차순 정렬:",a)

a.sort(reverse = True)
print("내림차순 정렬:",a)

a.reverse()
print("원소 뒤집기:",a)

a.insert(2,3)
print("인덱스 2에 3 추가:",a)

print("값이 2인 데이터 개수:",a.count(2))

a.remove(2.1)
print("값이 2.1인 데이터 삭제:",a)