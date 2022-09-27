import sys

N = int(input())
words = []
for _ in range(N):
    words.append(sys.stdin.readline().rstrip())
print(words)

words_set = list(set(words))
print(words_set)

words_set.sort()
print(words_set)

words_set.sort(key = lambda x : len(x))
#sort(key=lambda x(매개변수):f(X)함수)
#sort할때 원소를 람다함수에 넣은 결과값을 기준으로 srot 수행
print(words_set)
# for i in words_set:
#     print(i)
